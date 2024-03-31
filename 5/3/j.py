# J. P2P обновление
# нет тайпингов из-за Python 3.9 (PyPy 7.3.11)

class Device:
    def __init__(self, n, k):
        self.values = [0] * n
        self.updates = [False] * k
        self.upd_cntr = 0
        self.request = None

    def get_request(self, updates):
        # Каждое устройство выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего.
        # Если таких частей несколько, то выбирается отсутствующая на устройстве часть обновления с наименьшим номером.

        if self.updated:
            return None
        new_updates = (i for i in range(len(self.updates)) if not self.updates[i])
        return min(new_updates, key=lambda x: updates[x])

    def add_request(self, dev_no, upd_no, to_device):
        # Устройство A удовлетворяет тот запрос, который поступил от наиболее ценного для A устройства.
        # Ценность устройства B для устройства A определяется как количество частей обновления, ранее полученных устройством A от устройства B.
        # Если на устройство A пришло несколько запросов от одинаково ценных устройств, то удовлетворяется запрос того устройства, на котором меньше всего скачанных частей обновления.
        # Если и таких запросов несколько, то среди них выбирается устройство с наименьшим номером.

        if (
            self.request is None
            or self.values[dev_no] > self.request[0]
            or self.values[dev_no] == self.request[0] and to_device.upd_cntr < self.request[1]
            or self.values[dev_no] == self.request[0] and to_device.upd_cntr == self.request[1] and dev_no < self.request[2]
        ):
            self.request = self.values[dev_no], to_device.upd_cntr, dev_no, upd_no

    def get_update(self):
        if self.request is None:
            return None, None
        _, _, dev_no, upd_no = self.request
        self.request = None
        return upd_no, dev_no

    def install(self, upd_no, source_dev):
        self.values[source_dev] += 1
        self.updates[upd_no] = True
        self.upd_cntr += 1

    @property
    def updated(self) -> bool:
        return self.upd_cntr == len(self.updates)


class LoRaWAN:
    def __init__(self, n, k):
        self.updates = [1] * k
        self.updates_on_device = [(0, k)] * k

        self.devices = [Device(n, k) for _ in range(n)]
        self.devices[0].upd_cntr = k
        self.devices[0].updates = [True] * k

        self.update_time = [0] * n

    def _add_requests(self):
        for i in range(n):
            from_device = self.devices[i]
            upd_no = from_device.get_request(self.updates)
            if upd_no is None:
                continue
            to_device, _ = self.updates_on_device[upd_no]
            self.devices[to_device].add_request(i, upd_no, from_device)
            # print(f'{i} req {upd_no} from {to_device}')

    def _install_updates(self, time):
        updated = 0

        for i in range(n):
            upd_no, dev_no = self.devices[i].get_update()
            if upd_no is None:
                continue
            # print(f'{upd_no} installed to {dev_no} from {i}')
            device = self.devices[dev_no]
            device.install(upd_no, i)
            if device.updated:
                updated += 1
                self.update_time[dev_no] = time
            self.updates[upd_no] += 1

        return updated

    def _refresh_updates(self):
        # После этого устройство делает запрос выбранной части обновления у одного из устройств, на котором такая часть обновления уже скачана.
        # Если таких устройств несколько — выбирается устройство, на котором скачано наименьшее количество частей обновления.
        # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.
        for i in range(k):
            for j in range(n):
                device = self.devices[j]
                if not device.updates[i]:
                    continue
                dev_no, upd_cntr = self.updates_on_device[i]
                if (
                    self.devices[dev_no].upd_cntr != upd_cntr
                    or device.upd_cntr < upd_cntr
                    or device.upd_cntr == upd_cntr and j < dev_no
                ):
                    self.updates_on_device[i] = j, device.upd_cntr

    def update(self):
        time = 1
        updated = 1
        while updated < len(self.devices):
            # print(f'---{time}---')
            self._add_requests()
            updated += self._install_updates(time)
            self._refresh_updates()
            time += 1

        return self.update_time[1:n]


n, k = map(int, input().split())

lorawan = LoRaWAN(n, k)
answer = lorawan.update()

print(*answer)
