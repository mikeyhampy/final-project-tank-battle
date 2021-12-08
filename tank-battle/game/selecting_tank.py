import os
from game.actor import Actor
from game.point import Point
from game import constants
from game.input_service import InputService

class Selectingtank():
    def __init__(self, color_tank):
        self._input_service = InputService()
        self.color_tank = color_tank

    def select_p1_tank(self):
        pass

    def select_p2_tank(self):
        pass
    
    def get_player_choice(self):
        pass