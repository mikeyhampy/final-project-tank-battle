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
        self.global_right = False
 

        jump_right = False
        if self.is_right_up():
            self.global_right = True
 
        if self.is_right_pressed() and self.global_right:
            jump_right = True
            self.global_right = False
 



        if self.is_left_pressed():
            dx = -1
        
        if self.is_right_pressed():
            dx = 1
        
        if self.is_up_pressed():
            dy = 1
        
        if self.is_down_pressed():
            dy = -1

        if self.is_enter_pressed():
            fire = True
        else:
            fire = False
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

        # if self.is_a_up() and self.is_d_up():
        #     dx2 = 0
        if self.is_a_pressed():
            dx2 = -1

        if self.is_d_pressed():
            dx2 = 1

        if self.is_w_pressed():
            dy2 = -1
        
        if self.is_s_pressed():
            dy2 = 1

        if self.is_space_pressed():
            fire2 = True
        else:
            fire2 = False

        direction2 = Point(dx2, dy2)
        return direction2, fire2    

    def set_choice(self):
        if self.is_left_pressed() or self.is_a_pressed():
            self._dx = -1
        
        if self.is_right_pressed() or self.is_d_pressed():
            self._dx = 1

        if self.is_enter_pressed() or self.is_space_pressed():
            return True
        else:
            return False

    # left pressed and not pressed
    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)
    def is_left_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_LEFT)

    # right pressed and not pressed
    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)
    def is_right_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_RIGHT)

    # up pressed and not pressed
    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)
    def is_up_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_UP)

    # down pressed and not pressed
    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)
    def is_down_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_DOWN)

    # a pressed and not pressed
    def is_a_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_A)
    def is_a_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_A)

    # d pressed and not pressed
    def is_d_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_D)
    def is_d_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_D)

    # w pressed and not pressed
    def is_w_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_W)
    def is_w_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_W)

    # s pressed and not pressed
    def is_s_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_S)
    def is_s_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_S)

    # space pressed and not pressed
    def is_space_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_SPACE)
    def is_space_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_SPACE)

    # enter pressed and not pressed
    def is_enter_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_ENTER)
    def is_enter_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_ENTER)


    def window_should_close(self):
        return raylibpy.window_should_close()
