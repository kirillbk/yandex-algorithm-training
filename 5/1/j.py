# J. Форматирование документа
from sys import stdin
from re import split, findall, MULTILINE, DOTALL
from abc import ABC, abstractclassmethod
from heapq import heappop, heappush


class Element(ABC):
    @abstractclassmethod
    def __init__(self):
        self.w: int
        self.h: int


class Text(Element):
    def __init__(self, data: str, h, c):
        self.w = len(data) * c
        self.h = h
        self.text = data

    def __str__(self):
        return self.text


class Image(Element):
    def __init__(self, data: str):
        # width — целое положительное число, ширина рисунка в пикселях
        # height — целое положительное число, высота рисунка в пикселях
        # layout — одно из следующих значений:
        # - embedded (в тексте)
        # - surrounded (обтекание текстом)
        #  -floating (свободное), описывает расположение рисунка относительно текста
        params = {}
        for p in data.strip('() ').split()[1:]:
            k, v = p.split('=')
            params[k] = v

        self.h = int(params['height'])
        self.w = int(params['width'])
        self.layout = params['layout']
        self.dx = int(params.get('dx', 0))
        self.dy = int(params.get('dy', 0))

    def __str__(self) -> str:
        return self.layout


class DWord:
    def __init__(self, w, h, c) -> None:
        self.w = w
        self.h = h
        self.c = c

        self.x = 0
        self.y = 0
        self.images = []
        self.last_elem = 0, 0
        self.now_h = h
        self.max_float = 0

    def clear(self):
        self.x = self.y = 0
        self.images.clear()
        self.last_elem = 0, 0
        self.now_h = self.h
        self.max_float = 0

    def run(self, text: str) -> list[tuple[int, int]]:
        paragraphs = split(r"^ *$", text.strip(), flags=MULTILINE)
        for p in paragraphs:
            elements = findall(r"[\w\d\.,:;!?\-']+|\(.*?\)", p, DOTALL)
            elements = [Image(e) if e.startswith('(') else Text(e, self.h, self.c) for e in elements]

            borders = set()
            now_images = []
            for e in elements:
               self._add_element(e, borders, now_images)
            self._end_paragraph(borders, now_images)

    def _add_element(
        self,
        element: Element,
        borders: set[tuple[int, int, int]],
        now_images: list[tuple[int, int]],
    ):
        if isinstance(element, Image):
            match element.layout:
                case 'surrounded':
                    x, y = self._place_element(element, borders, now_images, False)
                    n = len(now_images)
                    left = x
                    right = x + element.w
                    heappush(now_images, (y + element.h, left, right, n))
                    borders.add((left, right, n))
                case 'embedded':
                    x, y = self._place_element(element, borders, now_images)
                    self.now_h = max(self.now_h, element.h)
                case 'floating':
                    x, y = self._add_float(element)
                    self.max_float = max(self.max_float, y + element.h)
                case _:
                    raise ValueError
            self.images.append((x, y))
        else:
            x, y = self._place_element(element, borders, now_images)
        self.last_elem = x + element.w , y
        # print(element, x, y, 'last', self.last_elem)

    def _new_line(
        self,
        borders: set[tuple[int, int, int]],
        now_images: list[tuple[int, int]],
     ):
        self.y += self.now_h
        self.x = 0
        self.now_h = self.h
        while now_images and now_images[0][0] <= self.y:
            _, l, r, i = heappop(now_images)
            borders.remove((l, r, i))

    def _end_paragraph(
        self,
        borders: set[tuple[int, int, int]],
        now_images: list[tuple[int, int]],
    ):
        if self.x != 0:
            self._new_line(borders, now_images)

        max_img = self.y
        while now_images:
            max_img, _, _, _ = heappop(now_images)

        self.y = max(max_img, self.max_float + 2)
        self.last_elem = 0, self.y
        self.max_float = 0
        # print('----------------------------')

    def _place_element(
        self,
        element: Element,
        borders: set[tuple[int, int, int]],
        now_images: list[tuple[int, int]],
        add_space: bool = True
    ):
        def get_width() -> int:
            if not add_space or self.x == 0:
                return element.w
            for _, r, _ in borders:
                if self.x == r:
                    return element.w
            return element.w + self.c

        def check_borders(x0, x1) -> bool:
            for l, r, _ in borders:
                if x0 < r and x1 > l:
                    return False
            return True

        while True:
            while self.x < self.w and self.w - self.x >= element.w:
                width = get_width()
                if self.x + width <= self.w and check_borders(self.x, self.x + width):
                    x = self.x + (width - element.w)
                    y = self.y
                    self.x += width
                    return x, y
                self.x += 1
            self._new_line(borders, now_images)


    def _add_float(
        self,
        element: Image
    ):
        x, y = self.last_elem
        y += element.dy
        x += element.dx

        if x < 0:
            x = 0
        elif x + element.w > self.w:
            x -= (x + element.w) - self.w

        return x, y


dword = DWord(*map(int, input().split()))
dword.run(stdin.read())
for x, y in dword.images:
    print(f'{x} {y}')
