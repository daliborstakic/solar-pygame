from pygame.math import Vector2

class Planet():
    def __init__(self, mass, x, y, dx, dy):
        self._x = x
        self._y = y
        self._mass = mass
        self._initial_velocity = Vector2(dx, dy)

    @property
    def mass(self):
        return self._mass

    @property
    def initial_velocity(self):
        return self._initial_velocity
