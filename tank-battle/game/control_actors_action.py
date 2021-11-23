from game import constants
from game.action import Action

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

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["tank"][0] # there's only one in the cast
        paddle.set_velocity(direction.scale(constants.TANK_SPEED))

    def select_end_game(self):
        self._enter = self._input_service.set_choice()
        choice = self._input_service._dx
        if choice == 0:
            return 0
        elif choice == -1:
            return -1
        elif choice == 1:
            return 1