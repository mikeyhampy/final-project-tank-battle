from game.actor import Actor
from game.point import Point
from game import constants

class Selectorbox():
    def __init__(self):
        self._selectors = [[], []]

    def set_selector_boxes(self):
        i = 0
        line_width = constants.SELECTOR_LINE_WIDTH
        x = constants.SELECTOR_X - (line_width * 2)
        y = constants.SELECTOR_Y - (line_width * 2)
        width = constants.FULL_TANK_WIDTH + (line_width * 4)
        height = constants.FULL_TANK_HEIGHT + (line_width * 4)
        line_color = "red"
        while(i < 2):
            selector = Actor()
            selector._box_line_width = line_width
            selector._colors_of_lines = line_color
            position = Point(x, y)
            selector.set_position(position)
            selector.set_width(width)
            selector.set_height(height)
            #wall.set_image(constants.IMAGE_WALL)
            # self._selectors[i][0] = selector
            self._selectors[i].append(selector)
            if i ==  0:
                line_color = "blue"
                x -= (line_width * 2)
                y -= (line_width * 2)
                width += (line_width * 4)
                height += (line_width * 4)
                i += 1


    def get_selector_boxes(self):
        return self._selectors