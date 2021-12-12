import os
from game import constants

def change_path():
    
    constants.IMAGE_BARREL1 = os.path.join(os.getcwd(), "./tank-battle/assets/barrel_blue.png")
    constants.IMAGE_BARREL2 = os.path.join(os.getcwd(), "./tank-battle/assets/barrel_red.png")
    constants.IMAGE_TANK1 = os.path.join(os.getcwd(), "./tank-battle/assets/tank1_blue.png")
    constants.IMAGE_TANK2 = os.path.join(os.getcwd(), "./tank-battle/assets/tank2_red.png")
    constants.IMAGE_BALL1 = os.path.join(os.getcwd(), "./tank-battle/assets/ball_blue.png")
    constants.IMAGE_BALL2 = os.path.join(os.getcwd(), "./tank-battle/assets/ball_red.png")