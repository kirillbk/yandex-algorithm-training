# J. P2P обновление

from heapq import heappush, heappushpop


class Device:
    def __init__(self) -> None:
        self.values = [0] * Device.n
        self.updates = [False] * Device.k
        self.upd_cntr = 0
        self.requests = []

    def get_request(self, updates: list[int]) -> int | None:
        # Каждое устройство выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего.
        # Если таких частей несколько, то выбирается отсутствующая на устройстве часть обновления с наименьшим номером.

        if self.updated:
            return None
        new_updates = (i for i in range(len(self.updates)) if not self.updates[i])
        return min(new_updates, key=lambda x: updates[x])

    def add_request(self, dev_no: int, upd_no: int, to_device: 'Device'):
        r = -self.values[dev_no], to_device.upd_cntr, dev_no, upd_no
        self.requests.append(r)

    def get_update(self) -> tuple[int | None, int | None]:
        # Устройство A удовлетворяет тот запрос, который поступил от наиболее ценного для A устройства.
        # Ценность устройства B для устройства A определяется как количество частей обновления, ранее полученных устройством A от устройства B.
        # Если на устройство A пришло несколько запросов от одинаково ценных устройств, то удовлетворяется запрос того устройства, на котором меньше всего скачанных частей обновления.
        # Если и таких запросов несколько, то среди них выбирается устройство с наименьшим номером.

        if not self.requests:
            return None, None
        _, _, dev_no, upd_no = min(self.requests)
        self.requests.clear()
        return upd_no, dev_no

    def install(self, upd_no, source_dev):
        self.values[source_dev] += 1
        self.updates[upd_no] = True
        self.upd_cntr += 1

    @property
    def updated(self) -> bool:
        return self.upd_cntr == len(self.updates)


def find_device(updates_on_dev, devices: list[Device]) -> int:
    # После этого устройство делает запрос выбранной части обновления у одного из устройств, на котором такая часть обновления уже скачана.
    # Если таких устройств несколько — выбирается устройство, на котором скачано наименьшее количество частей обновления.
    # Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.

    upd_n, dev_no = updates_on_dev[0]
    while upd_n != devices[dev_no].upd_cntr:
        heappushpop(updates_on_dev, (devices[dev_no].upd_cntr, dev_no))
        upd_n, dev_no = updates_on_dev[0]

    return dev_no


def solution(n, k):
    updates = [1] * k
    updates_on_devices = [[] for _ in range(k)]

    Device.n = n
    Device.k = k
    devices = [Device() for _ in range(n)]
    devices[0].upd_cntr = k
    devices[0].updates = [True] * k
    for i in range(k):
        updates_on_devices[i].append((k, 0))

    answer = [0] * n
    time = 1
    updated = 1

    while updated < n:
        for i in range(n):
            dev = devices[i]
            req_upd = dev.get_request(updates)
            if req_upd is None:
                continue

            req_device = find_device(updates_on_devices[req_upd], devices)
            devices[req_device].add_request(i, req_upd, dev)
            # print(f'{i} req {req_upd} from {req_device}')

        for i in range(n):
            upd_no, dev_no = devices[i].get_update()
            if upd_no is None:
                continue

            # print(f'{upd_no} installed to {dev_no} from {i}')
            device = devices[dev_no]
            device.install(upd_no, i)
            if device.updated:
                updated += 1
                answer[dev_no] = time

            updates[upd_no] += 1
            heappush(updates_on_devices[upd_no], (device.upd_cntr, dev_no))

        time += 1

    return answer[1:n]


n, k = map(int, input().split())

a = solution(n, k)

print(*a)
