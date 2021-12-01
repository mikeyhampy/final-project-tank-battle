import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._dx = -1
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0
        fire = False

        if self.is_left_pressed():
            dx = -1
        
        if self.is_right_pressed():
            dx = 1
        
        if self.is_up_pressed():
            fire = True
        else:
            fire = False
        
        # if self.is_down_pressed():
        #     dy = 1

        direction = Point(dx, dy)
        return direction, fire

    def get_direction2(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx2 = 0
        dy2 = 0
        fire2 = False

        if self.is_a_up() and self.is_d_up():
            dx2 = 0
        elif self.is_a_pressed():
            dx2 = -1
        elif self.is_d_pressed:
            dx2 = 1

        if self.is_w_pressed():
            fire2 = True
        else:
            fire2 = False
        
        # if self.is_s_pressed():
        #     dy = 1

        direction2 = Point(dx2, dy2)
        return direction2, fire2    

    def set_choice(self):
        if self.is_left_pressed():
            self._dx = -1
        
        if self.is_right_pressed():
            self._dx = 1

        if self.is_up_pressed():
            return True
        elif self.is_down_pressed():
            return True
        else:
            return False

    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def is_a_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_A)
    
    def is_a_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_A)

    def is_d_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_D)

    def is_d_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_D)

    def is_w_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_W)

    def is_s_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_S)

    def window_should_close(self):
        return raylibpy.window_should_close()
