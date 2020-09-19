from typing import AwaitableGenerator
import pygame
from math import atan2, sin, cos
from planet import Planet

# Screen size
WIDTH = 500
H_WIDTH = WIDTH // 2

# Colors
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock
clock = pygame.time.Clock()

def draw_planets(surface, planets):
    """ Draws the planets """
    for planet in planets:
        planet.draw(surface)

    pygame.display.update()

def calculate_angle(p1, p2):
    """ Calculates the angle between two points """
    x1, y1 = p1
    x2, y2 = p2

    return atan2((y2 - y1), (x2 - x1))

def main(surface):
    """ Main function """
    run = True

    # Yes, I know that the Sun is a star but it's easier this way
    sun = Planet(50, H_WIDTH, H_WIDTH, 0, 0, 20, YELLOW)
    earth = Planet(5, 100, H_WIDTH, 0.5, 0.5, 4, BLUE)

    # Planet list
    planets = [sun, earth]

    while run:
        draw_planets(surface, planets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

# The screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Solar System")

if __name__ == '__main__':
    main(win)
