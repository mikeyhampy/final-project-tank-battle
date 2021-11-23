from game import constants
from game.action import Action

class HandleOffScreenAction(Action):
    """
    Bounces the ball off the walls
    """

    def execute(self, cast):
        #get ball data
        # ball = cast["balls"][0]
        # x = ball._position.get_x()
        # y = ball._position.get_y()

        #bounces horizontal
        # if( x <= 0 or x >= constants.MAX_X - constants.BALL_WIDTH):
        #     ball._velocity._x = ball._velocity._x * -1

        #bounces vertical
        # if(y <= 0 or y >= constants.MAX_X - constants.BALL_HEIGHT):
        #     ball._velocity._y = ball._velocity._y * -1

        #get tank data
        tank = cast["tank"][0]
        tank_x = tank._position.get_x()

        #tank won't go off screen
        if(tank_x <= 0):
            tank._position._x = 0
        if(tank_x >= constants.MAX_X - constants.TANK_WIDTH):
            tank._position._x = constants.MAX_X - constants.TANK_WIDTH
