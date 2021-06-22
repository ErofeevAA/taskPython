import pygame

screen = pygame.display.set_mode((400, 400))

screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
list_of_figure = []
drawing = False  # режим рисования выключен
running = True


def redraw_fig():
    screen2.fill((0, 0, 0))
    for f in list_of_figure:
        pygame.draw.rect(screen2, (0, 0, 255), f, 5)


ctrl_flag, z_flag = False, False
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                ctrl_flag = True
            if event.key == pygame.K_z:
                z_flag = True
            if list_of_figure and ctrl_flag and z_flag:
                list_of_figure.pop()
                redraw_fig()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                ctrl_flag = False
            if event.key == pygame.K_z:
                z_flag = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # сохраняем нарисованное (на втором холсте)
            screen2.blit(screen, (0, 0))
            drawing = False
            list_of_figure.append((x1, y1, w, h))
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            w, h = event.pos[0] - x1, event.pos[1] - y1
    # рисуем на экране сохранённое на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:  # и, если надо, текущий прямоугольник
        pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
    pygame.display.flip()
