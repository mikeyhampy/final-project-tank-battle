from game.actor import Actor
from game.point import Point
from game import constants

class Tank():
    def __init__(self):
        self._tanks = []

    def set_tank(self):
        tank = Actor()
        position = Point(constants.TANK_X, constants.TANK_Y)
        tank.set_position(position)
        tank.set_width(constants.TANK_WIDTH)
        tank.set_height(constants.TANK_HEIGHT)
        #tank.set_image(constants.IMAGE_TANK)
        self._tanks.append(tank)

    def get_tank(self):
        return self._tanks