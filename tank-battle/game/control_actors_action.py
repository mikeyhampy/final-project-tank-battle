from game import constants
from game.action import Action
from game.ball import Ball

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self._enter = False
        self.fire_timer = 50
        self.fire_timer2 = 50

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # Tank 1
        fire = False
        direction, fire = self._input_service.get_direction()
        tank = cast["tank"][0] # there's only one in the cast
        tank.set_velocity(direction.scale(constants.TANK_SPEED))
        self.fire_timer += 1
        if fire and self.fire_timer > 30:
            ball = Ball()
            ball.angle = constants.TANK_ANGLE
            ball._x_pos = constants.BALL_X + (constants.BALL_X / 2)
            ball.set_ball()
            ball._angle = ball.angle
            cast["balls"].append(ball._balls[0])
            self.fire_timer = 0

        # Tank 2
        fire2 = False
        direction2, fire2 = self._input_service.get_direction2()
        tank2 = cast["tank"][1] # there's only one in the cast
        tank2.set_velocity(direction2.scale(constants.TANK_SPEED))
        self.fire_timer2 += 1
        if fire2 and self.fire_timer2 > 30:
            ball2 = Ball()
            ball2._x_pos = constants.BALL_X - (constants.BALL_X / 2)
            ball2.angle = constants.TANK_ANGLE2
            ball2.set_ball()
            ball2._angle = ball2.angle
            cast["balls"].append(ball2._balls[0])
            self.fire_timer2 = 0

    def select_end_game(self):
        self._enter = self._input_service.set_choice()
        choice = self._input_service._dx
        if choice == 0:
            return 0
        elif choice == -1:
            return -1
        elif choice == 1:
            return 1