# C. Путешествие по Москве

from math import atan2, dist


x_a, y_a, x_b, y_b = map(int, input().split())

r_a = dist((0, 0), (x_a, y_a))
r_b = dist((0, 0), (x_b, y_b))
angle = atan2(y_a, x_a) - atan2(y_b, x_b)
arc_length = min(r_a, r_b) * abs(angle)

via_arc_distance = arc_length + abs(r_a - r_b)
via_center_distance = r_a + r_b

print(min(via_center_distance, via_arc_distance))
