from game.actor import Actor
from game.point import Point
from game import constants

class Tank():
    def __init__(self):
        self._tanks = []

    def set_tank(self):
        tanks2 = []
        tank = Actor()
        tank._angle = constants.TANK_ANGLE
        tank_x = (constants.TANK_X / 2) + constants.TANK_X
        position = Point(tank_x, constants.TANK_Y)
        tank.set_position(position)
        tank.set_width(constants.TANK_WIDTH)
        tank.set_height(constants.TANK_HEIGHT)
        #tank.set_image(constants.IMAGE_TANK)
        tanks2.append(tank)

        tank2 = Actor()
        tank2._angle = constants.TANK_ANGLE2
        tank_x2 = constants.TANK_X - (constants.TANK_X / 2)
        position = Point(tank_x2, constants.TANK_Y)
        tank2.set_position(position)
        tank2.set_width(constants.TANK_WIDTH)
        tank2.set_height(constants.TANK_HEIGHT)
        #tank.set_image(constants.IMAGE_TANK)
        tanks2.append(tank2)
        self._tanks = tanks2

    def get_tank(self):
        return self._tanks