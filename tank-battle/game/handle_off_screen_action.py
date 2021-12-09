from game import constants
from game.action import Action

class HandleOffScreenAction(Action):
    """
    Bounces the ball off the walls
    """

    def execute(self, cast):
        #get ball data
        balls = cast["balls"]
        tank1 = cast["tank"][0]
        tank2 = cast["tank"][1]
        barrel1 = cast["barrel"][0]
        barrel2 = cast["barrel"][1]
        for ball in balls:
            x = ball._position.get_x()
            y = ball._position.get_y()

            #bounces horizontal
            if( x <= 0 or x >= constants.MAX_X - constants.BALL_WIDTH or y >= constants.MAX_Y - constants.BALL_HEIGHT):
                balls.remove(ball)

        #get tank data
        tank_x1 = tank1._position.get_x()

        tank_x2 = tank2._position.get_x()
        # barrel_x1 = barrel1._position.get_x()
        # barrel_x2 = barrel2._position.get_x()
        #tank won't go off screen
        if(tank_x2 < 0):
            tank2._position._x = 0
            # barrel2._velocity._x = 0
            barrel2._position._x += 1
        if(tank_x1 > constants.MAX_X - constants.TANK_WIDTH):
            tank1._position._x = constants.MAX_X - constants.TANK_WIDTH
            barrel1._position._x += -1
