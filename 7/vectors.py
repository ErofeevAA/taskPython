from PIL import Image, ImageDraw
from random import randint
import math


def get_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y1 - y2
    angle = math.degrees(math.atan2(dy, dx))
    return angle if angle > 0 else 360 + angle


def rotate(x, y, angle):
    angle = math.radians(angle)
    res_x = round(x * math.cos(angle) + y * math.sin(angle))
    res_y = round(-x * math.sin(angle) + y * math.cos(angle))
    return res_x, res_y


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def convert_coords(x, y, spread):
    return (x + 1) * spread, (y + 1) * spread


def sum_vector(x1, y1, x2, y2):
    return x1 + x2, y1 + y2


def draw_point(x, y, im_draw):
    size = 4
    x_s = x - size
    y_s = y - size
    im_draw.ellipse((x_s, y_s, x + size, y + size), "red")


def draw_vector(x, y, angle, im_draw):
    length = 10
    line = rotate(-length, 0, angle), rotate(length, 0, angle)
    triangle = (rotate(length // 3, length // 4, angle),
                rotate(length // 3, -length // 4, angle),
                rotate(length, 0, angle))
    line = sum_vector(*line[0], x, y), sum_vector(*line[1], x, y)
    triangle = sum_vector(*triangle[0], x, y), sum_vector(*triangle[1], x, y), sum_vector(*triangle[2], x, y)
    im_draw.line(line, "white")
    im_draw.polygon(triangle, "white", "white")


SIZE_IMG = int(input())
SPREAD = 40
SIZE_FIELD = SIZE_IMG // SPREAD

new_image = Image.new("RGB", (SIZE_IMG, SIZE_IMG), (0, 0, 0))
draw = ImageDraw.Draw(new_image)

sum_point = randint(1, SIZE_FIELD // 2)
points = [(randint(0, SIZE_FIELD - 2), randint(0, SIZE_FIELD - 2)) for i in range(sum_point)]

for i in range(0, SIZE_FIELD - 1):
    for j in range(0, SIZE_FIELD - 1):
        if (i, j) in points:
            draw_point(*convert_coords(i, j, SPREAD), draw)
            continue
        x_nearest = points[0][0]
        y_nearest = points[0][1]
        for point in points:
            if distance(i, j, point[0], point[1]) < distance(i, j, x_nearest, y_nearest):
                x_nearest = point[0]
                y_nearest = point[1]
        x_nearest, y_nearest = convert_coords(x_nearest, y_nearest, SPREAD)
        x_start, y_start = convert_coords(i, j, SPREAD)
        draw_vector(x_start, y_start, get_angle(x_start, y_start, x_nearest, y_nearest), draw)

new_image.save("img.png", "PNG")
