import pygame
from math import atan2, sin, cos, hypot

from pygame import surface
from planet import Planet

# Screen size
WIDTH = 600
H_WIDTH = WIDTH // 2

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
JUPITER = (191, 177, 119)
URANUS = (78, 160, 163)

# Clock
clock = pygame.time.Clock()

def draw_planets(surface, planets, sun):
    """ Draws the planets """
    win.fill(BLACK)
    
    # Easier without the sun in the list
    sun.draw(surface)

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
    gravitational_pull = 0.7 * (pl1.mass * pl2.mass) / (_distance ** 2)

    dx, dy = return_direction(angle)
    gravity_vector = gravitational_pull * pygame.Vector2(dx, dy)

    # Calculating the new direction vector
    pl1.velocity += gravity_vector

    pl1.move()

def main(surface):
    """ Main function """
    run = True

    # Yes, I know that the Sun is a star but it's easier this way
    sun = Planet(400, H_WIDTH, H_WIDTH, 0, 0, 15, YELLOW)
    mercury = Planet(2, H_WIDTH - 50, H_WIDTH, 0, 1, 1, ORANGE)
    venus = Planet(3, H_WIDTH - 75, H_WIDTH, 0, 1, 2, ORANGE)
    earth = Planet(2, H_WIDTH - 100, H_WIDTH, 0, 1, 1, BLUE)
    mars = Planet(2, H_WIDTH - 125, H_WIDTH, 0, 1, 1, RED)
    jupiter = Planet(10, H_WIDTH - 150, H_WIDTH, 0, 1, 7, JUPITER)
    saturn = Planet(10, H_WIDTH - 185, H_WIDTH, 0, 1, 6, GRAY)
    uranus = Planet(8, H_WIDTH - 220, H_WIDTH, 0, 1, 5, URANUS)
    neptune = Planet(8, H_WIDTH - 250, H_WIDTH, 0, 1, 5, PURPLE)

    # Planet list
    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    while run:
        clock.tick(60)

        draw_planets(surface, planets, sun)
        #move_planets(earth, sun)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

# The screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Solar System")

if __name__ == '__main__':
    main(win)
