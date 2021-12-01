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
        # check ball and tank collisions
        balls = cast["balls"]
        tank = cast["tank"][0]
        wall = cast["walls"][0]
        # for ball in balls:
        #     if self._physics_service.is_collision(ball, tank):
        #         if self.num_tank_col > 0:
        #             self._audio_service.stop_audio(constants.SOUND_BOUNCE)
        #         self._audio_service.play_sound(constants.SOUND_BOUNCE)
        #         ball._velocity._y = ball._velocity._y * -1
        #         self.num_tank_col = 1

        # check ball and brick collisions
        for ball in balls:
            if self._physics_service.is_collision(ball, wall):
                # if self.num_brick_col > 0:
                #     self._audio_service.stop_audio(constants.SOUND_BOUNCE)
                # self._audio_service.play_sound(constants.SOUND_BOUNCE)
                ball._velocity._y = ball._velocity._y * -1
                balls.remove(ball)
                # self.num_brick_col = 1