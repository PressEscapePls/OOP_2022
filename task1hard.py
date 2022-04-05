import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

# функция для призраков в небе
def ghost_1(x, y, r, h):
    circle(screen, (255, 255, 255), (x, y), r)
    polygon(screen, (255, 255, 255), ([x + r, y], [x + r * 1.2, y + h], [x - r * 1.2, y + h], [x - r, y]))
    for i in range(6):
        R = int(r // (2.5))
        circle(screen, (255, 255, 255), ((x - r) + R * i, y + h), R)
    for i in range(6):
        R = int(r // (2.5))
        circle(screen, (130, 130,130), ((x - r) + R * i, y + h + R), R)
    # eyes
    ellipse(screen, (0, 191, 255), (x - 0.5 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(screen, (0, 191, 255), (x + 0.25 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(screen, (0, 0, 0), (x - 0.50 * r, y - 0.3 * r, r * 0.25, r * 0.25))
    ellipse(screen, (0, 0, 0), (x + 0.25 * r, y - 0.3 * r, r * 0.25, r * 0.25))

# функция для призраков ниже горизонта неба
def ghost_2(x, y, r, h):
    circle(screen, (255, 255, 255), (x, y), r)
    polygon(screen, (255, 255, 255), ([x + r, y], [x + r * 1.2, y + h], [x - r * 1.2, y + h], [x - r, y]))
    for i in range(6):
        R = int(r // (2.5))
        circle(screen, (255, 255, 255), ((x - r) + R * i, y + h), R)
    for i in range(6):
        R = int(r // (2.5))
        circle(screen, (0, 0,0), ((x - r) + R * i, y + h + R), R)
    # eyes
    ellipse(screen, (0, 191, 255), (x - 0.5 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(screen, (0, 191, 255), (x + 0.25 * r, y - 0.5 * r, r * 0.25, r * 0.5))
    ellipse(screen, (0, 0, 0), (x - 0.50 * r, y - 0.3 * r, r * 0.25, r * 0.25))
    ellipse(screen, (0, 0, 0), (x + 0.25 * r, y - 0.3 * r, r * 0.25, r * 0.25))
# функция для облаков
def cloud(a, b, c, d, e, f, g, ):  # облако
    pygame.draw.ellipse(screen, (a, b, c), (d, e, f, g))

# функция для дома
def house(a, b, c, d):  # отрисовка дома
    pygame.draw.rect(screen, (70, 0, 0), (a, b, c, d), 0)  # корпус дома
    pygame.draw.rect(screen, (0, 0, 50), ((a + c / 13), (b + 3 * d / 7), ((3 * c) / 13), (d / 3)),
                     0)  # левое нижнее окно
    pygame.draw.rect(screen, (0, 0, 50), ((a + (5 * c) / 13), (b + 3 * d / 7), ((3 * c) / 13), (d / 3)),
                     0)  # среднее нижнее окно
    pygame.draw.rect(screen, (250, 240, 0), ((a + (9 * c) / 13), (b + 3 * d / 7), ((3 * c) / 13), (d / 3)),
                     0)  # правое нижнее окно
    pygame.draw.line(screen, (70, 0, 0), ((a + c / 13), (b + 3 * d / 7 + d / 6)),
                     ((a + 12 * c / 13), (b + 3 * d / 7 + d / 6)), 3)  # горизонтальный импост для нижних окон
    for i in range(3):  # вертикальные импосты
        pygame.draw.line(screen, (70, 0, 0), ((a + (5 + 8 * i) * c / 26), (b + 3 * d / 7)),
                         ((a + (5 + 8 * i) * c / 26), (b + d / 3 + 3 * d / 7)), 3)  #

    pygame.draw.rect(screen, (250, 240, 0), ((a + c / 5), (b + d / 20), (3 * c / 5), (5 * d / 30)), 0)  # верхнее окно
    pygame.draw.rect(screen, (0, 0, 0), ((a + c / 10), (b + d / 10), (4 * c / 5), (d / 6)), 3)  # кортур балкончика
    for i in range(10):  # перекладины балкончика
        pygame.draw.line(screen, (0, 0, 0), ((a + c / 10 + i * (4 * c / 5) / 10), (b + d / 10)),
                         ((a + c / 10 + i * (4 * c / 5) / 10), (d / 6 + b + d / 10)), 3)
    pygame.draw.polygon(screen, (40, 0, 0),
                        [[a - c / 10, b], [c + a + c / 10, b], [c + a - c / 10, b - d / 10],
                         [a + c / 10, b - d / 10]])  # крыша
    pygame.draw.rect(screen, (40, 0, 0), ((a + c / 5), (b - d / 5), (c / 10), (d / 10)), 0)  # труба 1
    pygame.draw.rect(screen, (40, 0, 0), ((a + 2 * c / 5), (b - d / 5), (c / 10), (d / 10)), 0)  # труба 2


pygame.draw.rect(screen, (130, 130, 130), (0, 0, 400, 250), 0)  # небо
pygame.draw.circle(screen, (255, 255, 255), (350, 50), 35, 0)  # луна
cloud(50, 50, 50, 100, 50, 300, 60)

house(10, 300, 170, 220)
house(310, 220, 120, 160)

ghost_1(300, 150, 30, 20)
ghost_1(200, 100, 20, 10)
ghost_2(230, 280, 30, 20)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()