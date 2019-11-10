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

Line1 = [random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(0, WIDTH), random.randint(0, HEIGHT)]
Line2 = [Line1[2],Line1[3], random.randint(0, WIDTH), random.randint(0, HEIGHT)]
Line3 = [Line2[2],Line2[3], random.randint(0, WIDTH), random.randint(0, HEIGHT)]
Line4 = [Line3[2],Line3[3], Line1[0], Line1[1]]

Line1D = [random.randint(-SPEED, SPEED), random.randint(-SPEED, SPEED), random.randint(-SPEED, SPEED), random.randint(-SPEED, SPEED)]
Line2D = [Line1D[2],Line1D[3], random.randint(-SPEED, SPEED), random.randint(-SPEED, SPEED)]
Line3D = [Line2D[2],Line2D[3], random.randint(-SPEED, SPEED), random.randint(-SPEED, SPEED)]
Line4D = [Line3D[2],Line3D[3], Line1D[0], Line1D[1]]

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

    pygame.draw.line(surface, RED, (Line1[0], Line1[1]), (Line1[2], Line1[3]), THICKNESS)
    pygame.draw.line(surface, RED, (Line2[0], Line2[1]), (Line2[2], Line2[3]), THICKNESS)
    pygame.draw.line(surface, RED, (Line3[0], Line3[1]), (Line3[2], Line3[3]), THICKNESS)
    pygame.draw.line(surface, RED, (Line4[0], Line4[1]), (Line4[2], Line4[3]), THICKNESS)

    update(Line1, Line1D)
    update(Line2, Line2D)
    update(Line3, Line3D)
    update(Line4, Line4D)

    changeDirection(Line1, Line1D)
    changeDirection(Line2, Line2D)
    changeDirection(Line3, Line3D)
    changeDirection(Line4, Line4D)

    clock.tick(30)
    pygame.display.update()
