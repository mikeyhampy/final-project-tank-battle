import sys
from game import constants
import raylibpy

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        None
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        self._textures = {}
        self._color_number = 0

    def open_window(self, title):
        """
        Opens a new window with the provided title.
        """
        raylibpy.init_window(constants.MAX_X, constants.MAX_Y, title)
        raylibpy.set_target_fps(constants.FRAME_RATE)
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.begin_drawing()
        raylibpy.clear_background(raylibpy.BLACK)

    def draw_box(self, x, y, width, height):
        """
        Draws at rectangular box with the provided specifications.
        """
        raylibpy.draw_rectangle(x, y, width, height, raylibpy.BLUE)

    def draw_text(self, x, y, text, text_color):
        """
        Outputs the provided text at the desired location.
        """
        color = raylibpy.WHITE

        if text == "YES" and text_color == -1:
            color = raylibpy.GREEN
        elif text == "NO" and text_color == 1:
            color = raylibpy.RED

        raylibpy.draw_text(text, x + 5, y + 5, constants.DEFAULT_FONT_SIZE, color)

    def draw_image(self, x, y, image):
        """
        Outputs the provided image on the screen.
        """
        if image not in self._textures.keys():

            loaded = raylibpy.load_texture(image)
            self._textures[image] = loaded

        texture = self._textures[image]
        raylibpy.draw_texture(texture, x, y, raylibpy.WHITE)

    def draw_actor(self, actor, if_tank):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()

        vc = raylibpy.Vector2(width / 2, 0)
        tangle = raylibpy.Rectangle(x, y, width, height)

        if actor.has_image():
            image = actor.get_image()
            self.draw_image(x, y, image)
            #self.draw_image(x - width / 2, y - height / 2, image)
        elif actor.has_text():
            text = actor.get_text()
            self.draw_text(x, y, text, self._color_number)
        elif width > 0 and height > 0:
            if if_tank:
                raylibpy.draw_rectangle_pro(tangle, vc, actor._angle, raylibpy.RED)
            else:
                self.draw_box(x, y, width, height)
        
    def draw_actors(self, actors, color_number, if_tank):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        self._color_number = color_number
        for actor in actors:
            self.draw_actor(actor, if_tank)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.end_drawing()
        #raylibpy.close_window()
