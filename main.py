from EgorHW import *

# вызов функций для рисования пейзажа
sun(255,255,0,250,100,20)
land(207,204,196,50)
cloud(244,193,193,100)
rock(238,118,0)
rock2(139,0,0)
pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()