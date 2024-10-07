import math

def distance_from_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def print_closer_point_first(x1, y1, x2, y2):
    if distance_from_center(x1, y1) <= distance_from_center(x2, y2):
        print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1_length = line_length(x1, y1, x2, y2)
    line2_length = line_length(x3, y3, x4, y4)

    if line1_length >= line2_length:
        print_closer_point_first(x1, y1, x2, y2)
    else:
        print_closer_point_first(x3, y3, x4, y4)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

longer_line(x1, y1, x2, y2, x3, y3, x4, y4)