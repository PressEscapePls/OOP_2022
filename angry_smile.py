import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000,1000))

rect(screen, (237, 199, 103), (0, 0, 1000, 1000))

# тело смайла
circle(screen, (255, 255, 255), (500, 500), 260)
circle(screen, (255, 255, 0), (500, 500), 250)

# рисует глаз
def Fun_eyes(x, y, r):
    circle(screen, (0, 0, 0), (x, y), r)
    circle(screen, (250, 0, 0), (x, y), r-5)
    circle(screen, (0, 0, 0), (x, y), r / 2)


Fun_eyes(400, 425, 60)
Fun_eyes(600, 425, 40)
polygon(screen, (0, 0, 0), [(560, 400), (550, 385), (755, 300), (765, 315)])  # левая бровь
polygon(screen, (0, 0, 0), [(460, 400), (475, 380), (300, 290), (290, 325)])  # левая бровь

rect(screen, (0, 0, 0), (375, 600, 250, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()