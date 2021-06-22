import pygame as pg


def check_click(start_x, start_y, width, pos_click):
    if pos_click[0] < start_x or pos_click[1] < start_y:
        return False
    if pos_click[0] > start_x + width or pos_click[1] > start_y + width:
        return False
    return True


def sign(val):
    if val < 0:
        return -1
    if val == 0:
        return 0
    return 1


pg.init()

rect_width = 70
color = (255, 255, 0)

screen = pg.display.set_mode((300, 300))
screen.fill((0, 0, 0))
pg.draw.rect(screen, color, (0, 0, rect_width, rect_width))

pg.display.flip()
running = True

mouse_x = 0
mouse_y = 0

rect_x = 0
rect_y = 0

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            continue
        if pg.mouse.get_pressed()[0]:
            try:
                if not check_click(rect_x, rect_y, rect_width, event.pos):
                    continue
                x, y = event.pos
                rect_x += (x - mouse_x)
                rect_y += (y - mouse_y)
                mouse_x, mouse_y = x, y
                screen.fill((0, 0, 0))
                pg.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_width))
                pg.display.update()
            except AttributeError:
                pass


pg.quit()
