import pygame as pg
from math import cos, sin, radians

WIDTH = 400
RADIUS = 200

pg.init()
screen = pg.display.set_mode((WIDTH, WIDTH))
screen.fill((0, 0, 0))
color = pg.Color(0, 255, 0)

running = True
pause = False
fps = 120
clock = pg.time.Clock()
mull = 1
while running:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = not pause
    if not pause:
        for point in range(1, 361):
            x = int(cos(radians(point)) * RADIUS) + WIDTH // 2
            y = int(sin(radians(point)) * RADIUS) + WIDTH // 2
            point1 = point * mull
            x1 = int(cos(radians(point1)) * RADIUS) + WIDTH // 2
            y1 = int(sin(radians(point1)) * RADIUS) + WIDTH // 2
            pg.draw.line(screen, color, (x, y), (x1, y1), 1)
        clock.tick(fps)
        pg.display.flip()
        mull += 0.001
        hsv = color.hsva
        h = hsv[0] + 0.5
        if h > 360:
            h = 0
        color.hsva = (h, hsv[1], hsv[2], hsv[3])

pg.quit()
