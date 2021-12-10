import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

TANK_TOP_WIDTH = 65
TANK_FRONT_WIDTH = 73
TANK_WIDTH = 96
TANK_HEIGHT = 45

BARREL_WIDTH = 71
BARREL_HEIGHT = 17

WALL_WIDTH = 20
WALL_HEIGHT = 275

BALL_WIDTH = 5
BALL_HEIGHT = 5
BALL_DX = -8
BALL_DY = -8

TANK_SPEED = 1
TANK_ANGLE = 180
TANK_ANGLE2 = 360

FULL_TANK_WIDTH = 144
FULL_TANK_HEIGHT = 45
SELECTOR_Y = 120
SELECTOR_X = 92
SELECTOR_LINE_WIDTH = 0

FULL1_TANK_FILE_PATH = "./tank-battle/assets/full1_"
RED = "red.png"
GRAY = "gray.png"
BLUE = "blue.png"
ORANGE = "orange.png"
YELLOW = "yellow.png"
GREEN = "green.png"

IMAGE_FULL1_RED = os.path.join(os.getcwd(), FULL1_TANK_FILE_PATH + RED)
IMAGE_FULL1_GRAY = os.path.join(os.getcwd(), FULL1_TANK_FILE_PATH + GRAY)
IMAGE_FULL1_BLUE = os.path.join(os.getcwd(), FULL1_TANK_FILE_PATH + BLUE)
IMAGE_FULL1_ORANGE = os.path.join(os.getcwd(), FULL1_TANK_FILE_PATH + ORANGE)
IMAGE_FULL1_YELLOW = os.path.join(os.getcwd(), FULL1_TANK_FILE_PATH + YELLOW)
IMAGE_FULL1_GREEN = os.path.join(os.getcwd(), FULL1_TANK_FILE_PATH + GREEN)

IMAGE_BARREL1 = os.path.join(os.getcwd(), "./tank-battle/assets/barrel_blue.png")
IMAGE_TANK1 = os.path.join(os.getcwd(), "./tank-battle/assets/tank1_blue.png")
IMAGE_BARREL2 = os.path.join(os.getcwd(), "./tank-battle/assets/barrel_red.png")
IMAGE_TANK2 = os.path.join(os.getcwd(), "./tank-battle/assets/tank2_red.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./tank-battle/assets/ball_red_10.png")

SOUND_START = os.path.join(os.getcwd(), "./tank-battle/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./tank-battle/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./tank-battle/assets/over.wav")
SOUND_VICTORY = os.path.join(os.getcwd(), "./tank-battle/assets/ff_vii_victory.wav")



TANK_X1 = (MAX_X * (1 / 2)) + (MAX_X * (1 / 4))
TANK_X2 = (MAX_X * (1 / 2)) - (MAX_X * (1 / 4)) - TANK_WIDTH
TANK_Y = MAX_Y - TANK_HEIGHT

BARREL_X1 = TANK_X1 + (TANK_WIDTH - TANK_FRONT_WIDTH)
BARREL_X2 = TANK_X2 + (TANK_FRONT_WIDTH)
BARREL_Y1 = TANK_Y + BARREL_HEIGHT
BARREL_Y2 = TANK_Y

TANK_ANGLE_CHANGE = (BARREL_HEIGHT)/(170 / 3)

BALL1_POS = BARREL_X1 + (BALL_WIDTH * 1.4)
BALL2_POS = BARREL_X2 - (BALL_WIDTH * 1.4)
BALL_Y = TANK_Y + (BARREL_HEIGHT) - (BALL_HEIGHT * 1.4)
BALL_Y1 = TANK_Y + (BARREL_HEIGHT) - (BALL_HEIGHT * 2.1)
BALL_CHANGE_X1 = 0
BALL_CHANGE_X2 = 0




KEEP_PLAYING = True

RIGHT_PLAYER_LOSES = False
LEFT_PLAYER_LOSES = False