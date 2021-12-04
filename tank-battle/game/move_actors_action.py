from game import constants
from game.action import Action
from game.point import Point
from math import cos
from math import sin

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        choice = True
        right_barrel = None
        left_barrel = None
        for key, group in cast.items():
            if key == "tank":
                choice = False
            else:
                choice = True
            for actor in group:
                if not actor.get_velocity().is_zero():
                    if key == "tank":
                        right_barrel = group[0]
                        left_barrel = group[1]
                    self._move_actor(actor, choice, right_barrel, left_barrel)

    def _move_actor(self, actor, choice, right_barrel, left_barrel):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()

        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()
        
        #checks if we are not in the tank director 
        #if not then run if, then else
        if choice:
            actor._velocity._y = dy + .1
            x = (x + dx) #% constants.MAX_Xconstants.TANK_HEIGHT
            y = (y + dy) #% constants.MAX_Y
        else:  
            if right_barrel == actor:# or self._tank_counter % 2 == 1:
                # if actor._angle < 90:
                #     actor._angle = 90
                # if actor._angle > 170:
                #     actor._angle = 170
                actor._angle += dy
                constants.TANK_ANGLE += dy
            elif left_barrel == actor:
                constants.TANK_ANGLE2 += dy
                actor._angle += dy

            # all tank actors (tank and barrels)
            x = (x + dx) #% constants.MAX_X
        
        position = Point(x, y)
        actor.set_position(position)