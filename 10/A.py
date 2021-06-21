import pygame as pg

pg.init()

width, num = map(int, input().split())

rect_width = width / num

screen = pg.display.set_mode((width, width))
screen.fill((0, 0, 0))


def draw():
    for i in range(num):
        for j in range(num):
            if (i + j) % 2 != 0:
                pg.draw.rect(screen, (255, 255, 255), (i * rect_width, j * rect_width, rect_width, rect_width))


draw()
pg.display.flip()
while pg.event.wait().type != pg.QUIT:
    pass

pg.quit()
