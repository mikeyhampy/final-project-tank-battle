from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service
        self.num_tank_col = 0
        self.num_wall_col = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if len(cast) == 2:
        #beginning of the game
            selector_p1 = cast["selector"][0]
            selector_p2 = cast["selector"][1]
            tank_colors = cast["colors"]
            if selector_p1._color_selected and selector_p2._color_selected:
                for tank_color in tank_colors:
                    if self._physics_service.is_collision(tank_color, selector_p1):
                        selector_p1._color_tank = tank_color._color_tank
                        constants.PLAYER_TANK_COLOR1 = tank_color._color_tank
                        
                    if self._physics_service.is_collision(tank_color, selector_p2):
                        selector_p2._color_tank = tank_color._color_tank
                        constants.PLAYER_TANK_COLOR2 = tank_color._color_tank
        else:
                
            # set variables to check collisions in game
            balls = cast["balls"]
            barrel_right = cast["barrel"][0]
            barrel_left = cast["barrel"][1]        
            tank_right = cast["tank"][0]
            tank_left = cast["tank"][1]
            wall = cast["walls"][0]
            # for ball in balls:
            #     if self._physics_service.is_collision(ball, tank):
            #         if self.num_tank_col > 0:
            #             self._audio_service.stop_audio(constants.SOUND_BOUNCE)
            #         self._audio_service.play_sound(constants.SOUND_BOUNCE)
            #         ball._velocity._y = ball._velocity._y * -1
            #         self.num_tank_col = 1

            # check ball and wall collisions
            for ball in balls:
                if self._physics_service.is_collision(ball, wall):
                    # if self.num_brick_col > 0:
                    #     self._audio_service.stop_audio(constants.SOUND_BOUNCE)
                    # self._audio_service.play_sound(constants.SOUND_BOUNCE)
                    # ball._velocity._y = ball._velocity._y * -1
                    balls.remove(ball)
                    # self.num_brick_col = 1


                    '''
            # check ball and barrel right collisions
            for ball in balls:
                if ball._velocity._y < 0:
                    if self._physics_service.is_collision(ball, barrel_right):
                    # if self.num_brick_col > 0:
                    #     self._audio_service.stop_audio(constants.SOUND_BOUNCE)
                    # self._audio_service.play_sound(constants.SOUND_BOUNCE)
                    # ball._velocity._y = ball._velocity._y * -1
                        balls.remove(ball)
                    # self.num_brick_col = 1'''

                    # check ball and tank right collisions
            for ball in balls:
                if self._physics_service.is_collision(ball, tank_right):
                    # if self.num_brick_col > 0:
                    #     self._audio_service.stop_audio(constants.SOUND_BOUNCE)
                    # self._audio_service.play_sound(constants.SOUND_BOUNCE)
                    # ball._velocity._y = ball._velocity._y * -1
                    balls.remove(ball)
                    constants.RIGHT_PLAYER_LOSES = True
                    x2 = ball.get_position().get_x()
                    y2 = ball.get_position().get_y()
                    width2 = ball.get_width()
                    height2 = ball.get_height()
                    x = tank_right.get_position().get_x()
                    y = tank_right.get_position().get_y()
                    width = tank_right.get_width()
                    height = tank_right.get_height()
                    print(f'Ball position: ({ball._position._x}, {ball._position._x})   ({width2}, {height2})')
                    print(f'tank position: ({tank_right._position._x}, {tank_right._position._x})   ({width}, {height})')
                    # self.num_brick_col = 1



                    '''
            # check ball and barrel left collisions
            for ball in balls:
                if ball._velocity._y > 0:
                    if self._physics_service.is_collision(ball, barrel_left):
                    # if self.num_brick_col > 0:
                    #     self._audio_service.stop_audio(constants.SOUND_BOUNCE)
                    # self._audio_service.play_sound(constants.SOUND_BOUNCE)
                    # ball._velocity._y = ball._velocity._y * -1
                        balls.remove(ball)
                    # self.num_brick_col = 1'''

            # check ball and tank left collisions
            for ball in balls:
                if self._physics_service.is_collision(ball, tank_left):
                    # if self.num_brick_col > 0:
                    #     self._audio_service.stop_audio(constants.SOUND_BOUNCE)
                    # self._audio_service.play_sound(constants.SOUND_BOUNCE)
                    # ball._velocity._y = ball._velocity._y * -1
                    balls.remove(ball)
                    constants.LEFT_PLAYER_LOSES = True
                    # self.num_brick_col = 1
                    x2 = ball.get_position().get_x()
                    y2 = ball.get_position().get_y()
                    width2 = ball.get_width()
                    height2 = ball.get_height()
                    x = tank_right.get_position().get_x()
                    y = tank_right.get_position().get_y()
                    width = tank_right.get_width()
                    height = tank_right.get_height()
                    print(f'Ball position: ({ball._position._x}, {ball._position._x})   ({width2}, {height2})')
                    print(f'tank position: ({tank_right._position._x}, {tank_right._position._x})   ({width}, {height})')