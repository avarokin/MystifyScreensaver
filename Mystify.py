import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
THICKNESS = 3
SPEED = 2

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

Line1 = [random.randint(0,WIDTH),random.randint(0,HEIGHT),random.randint(0,WIDTH),random.randint(0,HEIGHT)]

Line1d = [random.randint(-SPEED,SPEED),random.randint(-SPEED,SPEED),random.randint(-SPEED,SPEED),random.randint(-SPEED,SPEED)]

surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def changeDirection():
    print("hi")

def update(Line):
    Line[0] += Line1d[0]
    Line[1] += Line1d[1]
    Line[2] += Line1d[2]
    Line[3] += Line1d[3]


end = False

while not end:

    # Close window button to end program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    surface.fill(BACKGROUND_COLOR)

    pygame.draw.line(surface,RED,(Line1[0],Line1[1]),(Line1[2],Line1[3]),THICKNESS)

    update(Line1)

    clock.tick(30)
    pygame.display.update()
