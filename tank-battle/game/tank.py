from game.actor import Actor
from game.point import Point
from game import constants

class Tank():
    def __init__(self):
        self._tanks = []

    def set_tank(self):
        #right barrel
        tank = Actor()
        tank._angle = constants.TANK_ANGLE
        tank_x = (constants.TANK_X / 2) + constants.TANK_X
        position = Point(tank_x, constants.TANK_Y)
        tank.set_position(position)
        tank.set_width(constants.TANK_WIDTH)
        tank.set_height(constants.TANK_HEIGHT)
        #tank.set_image(constants.IMAGE_TANK)
        self._tanks.append(tank)

        #left barrell
        tank2 = Actor()
        tank2._angle = constants.TANK_ANGLE2
        tank_x2 = constants.TANK_X - (constants.TANK_X / 2)
        position = Point(tank_x2, constants.TANK_Y)
        tank2.set_position(position)
        tank2.set_width(constants.TANK_WIDTH)
        tank2.set_height(constants.TANK_HEIGHT)
        #tank.set_image(constants.IMAGE_TANK)
        self._tanks.append(tank2)

         #right tank
        tank3 = Actor()
        tank_x3 = (constants.TANK_X / 2) + constants.TANK_X - (constants.TANK_HEIGHT / 2)
        position = Point(tank_x3, constants.TANK_Y)
        tank3.set_position(position)
        tank3.set_width(constants.TANK_HEIGHT)
        tank3.set_height(constants.TANK_HEIGHT)
        #tank.set_image(constants.IMAGE_TANK)
        self._tanks.append(tank3)

        #left tank
        tank4 = Actor()
        tank_x4 = constants.TANK_X - (constants.TANK_X / 2) - (constants.TANK_HEIGHT / 2)
        position = Point(tank_x4, constants.TANK_Y)
        tank4.set_position(position)
        tank4.set_width(constants.TANK_HEIGHT)
        tank4.set_height(constants.TANK_HEIGHT)
        #tank.set_image(constants.IMAGE_TANK)
        self._tanks.append(tank4)

    def get_tank(self):
        return self._tanks