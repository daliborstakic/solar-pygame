import pygame
from pygame.math import Vector2

class Planet():
    def __init__(self, mass, x, y, dx, dy, radius, color):
        self._x = x
        self._y = y
        self._mass = mass
        self._radius = radius
        self.color = color
        self._velocity = Vector2(dx, dy)

    @property
    def mass(self):
        """ Mass getter """
        return self._mass

    @property
    def velocity(self):
        """ Velocity getter """
        return self._velocity
    
    @velocity.setter
    def velocity(self, velocity):
        """ Velocity setter """
        self._velocity = velocity

    @property
    def radius(self):
        """ Radius getter """
        return self._radius
    
    @property
    def coordinates(self):
        """ Returns the coordinates """
        return self._x, self._y

    @property.setter
    def x(self, x):
        """ X coordinate setter """
        self._x = x

    @property.setter
    def y(self, y):
        """ Y coordinate setter """
        self._y = y

    def draw(self, win):
        """ Draws the planet """
        pygame.draw.circle(win, self.color, (self.x + self.radius // 2, self.y + self.radius // 2))
