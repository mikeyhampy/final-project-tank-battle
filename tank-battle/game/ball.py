from game.actor import Actor
from game.point import Point
from game import constants
from math import cos
from math import sin
from math import radians

class Ball():
    def __init__(self):
        self._balls = []
        self.angle = 2
        self._x_pos = 0
    def set_ball(self):
        ball = Actor()
        angle = self.angle - 90
        x_cos = cos(radians(angle))
        y_sin = sin(radians(angle))
        x = self._x_pos - constants.TANK_HEIGHT * x_cos
        y = constants.BALL_Y - constants.TANK_HEIGHT * y_sin
        dx = constants.BALL_DX * x_cos
        dy = constants.BALL_DY * y_sin
        position = Point(x, y)
        velocity = Point(dx, dy)
        ball.set_position(position)
        ball.set_velocity(velocity)
        ball.set_width(constants.BALL_WIDTH)
        ball.set_height(constants.BALL_HEIGHT)
        # ball.set_image(constants.IMAGE_BALL)
        self._balls.append(ball)

    def get_ball(self):
        return self._balls