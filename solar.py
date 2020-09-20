import pygame
from math import atan2, sin, cos, hypot

from pygame import surface
from planet import Planet

# Screen size
WIDTH = 500
H_WIDTH = WIDTH // 2

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

# Clock
clock = pygame.time.Clock()

def draw_planets(surface, planets):
    """ Draws the planets """
    win.fill(BLACK)

    for planet in planets:
        planet.draw(surface)
    
    pygame.display.update()

def calculate_angle(p1, p2):
    """ Calculates the angle between two points """
    x1, y1 = p1
    x2, y2 = p2

    return atan2((y2 - y1), (x2 - x1))

def return_direction(angle):
    """ Returns two values between -1 and 1 which indicate the direction """
    dx = cos(angle)
    dy = sin(angle)

    return dx, dy

def distance(p1, p2):
    """ Returns the distance between two points """
    x1, y1 = p1
    x2, y2 = p2

    return hypot((x2 - x1), (y2 - y1))

def move_planets(pl1, pl2):
    """ Moves one planet to the other """

    # Angle between two planets
    angle = calculate_angle(pl1.coordinates, pl2.coordinates)
    
    # Distance between two points
    _distance = distance(pl1.coordinates, pl2.coordinates)

    # Gravitational vector
    gravitational_pull = (pl1.mass * pl2.mass) / (_distance ** 2)

    dx, dy = return_direction(angle)
    gravity_vector = gravitational_pull * pygame.Vector2(dx, dy)

    # Calculating the new direction vector
    pl1.velocity += gravity_vector

    if _distance != 0:
        pl1.move()

def main(surface):
    """ Main function """
    run = True

    # Yes, I know that the Sun is a star but it's easier this way
    sun = Planet(50, H_WIDTH, H_WIDTH, 0, 0, 20, YELLOW)
    earth = Planet(25, 100, H_WIDTH, 0, 1, 4, BLUE)

    # Planet list
    planets = [sun, earth]

    while run:
        clock.tick(60)

        move_planets(earth, sun)
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
