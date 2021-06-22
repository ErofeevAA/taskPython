import pygame
import random

direction = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

WIDTH = 400
sum_bomb = 10
W_FIELD = 10
REC_WITH = WIDTH // W_FIELD
field = [[False for i in range(W_FIELD)] for j in range(W_FIELD)]

for i in range(10):
    x = random.randrange(0, W_FIELD)
    y = random.randrange(0, W_FIELD)
    field[x][y] = True


def get_pos_click(pos_click):
    return pos_click[0] // REC_WITH, pos_click[1] // REC_WITH


pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
screen.fill((0, 0, 0))

WHITE = (255, 255, 255)
RED = (255, 0, 0)

running = True

for i in range(W_FIELD):
    for j in range(W_FIELD):
        if not field[i][j]:
            pygame.draw.rect(screen, WHITE, (i * REC_WITH, j * REC_WITH, REC_WITH, REC_WITH), 1)
            continue
        pygame.draw.rect(screen, RED, (i * REC_WITH, j * REC_WITH, REC_WITH, REC_WITH))
        pygame.draw.rect(screen, WHITE, (i * REC_WITH, j * REC_WITH, REC_WITH, REC_WITH), 1)

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = get_pos_click(event.pos)
            print(x, y)
            if field[x][y]:
                continue
            cur_sum = 0
            for d in direction:
                if 0 <= x + d[0] < W_FIELD and 0 <= y + d[1] < W_FIELD:
                    if field[x + d[0]][y + d[1]]:
                        cur_sum += 1
            font = pygame.font.Font(None, 40)
            text = font.render(str(cur_sum), True, WHITE)
            screen.blit(text, (x * REC_WITH + 5, y * REC_WITH + 5))
            pygame.display.flip()
