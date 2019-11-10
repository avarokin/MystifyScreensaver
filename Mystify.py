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

Line = [random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(0, WIDTH), random.randint(0, HEIGHT)]

LineD = [random.randint(-SPEED,SPEED),random.randint(-SPEED,SPEED),random.randint(-SPEED,SPEED),random.randint(-SPEED,SPEED)]

surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def changeDirection(Line, LineD):
    if Line[0] < 0 or Line[0] > WIDTH:
        LineD[0] = -LineD[0]
    if Line[1] < 0 or Line[1] > HEIGHT:
        LineD[1] = -LineD[1]
    if Line[2] < 0 or Line[2] > WIDTH:
        LineD[2] = -LineD[2]
    if Line[3] < 0 or Line[3] > HEIGHT:
        LineD[3] = -LineD[3]


def update(Line,LineD):
    Line[0] += LineD[0]
    Line[1] += LineD[1]
    Line[2] += LineD[2]
    Line[3] += LineD[3]


end = False

while not end:

    # Close window button to end program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    surface.fill(BACKGROUND_COLOR)

    pygame.draw.line(surface, RED, (Line[0], Line[1]), (Line[2], Line[3]), THICKNESS)

    update(Line,LineD)
    changeDirection(Line,LineD)

    clock.tick(30)
    pygame.display.update()
