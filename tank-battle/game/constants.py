import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK = os.path.join(os.getcwd(), "./tank-battle/assets/brick-3.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./tank-battle/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./tank-battle/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./tank-battle/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./tank-battle/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./tank-battle/assets/over.wav")
SOUND_VICTORY = os.path.join(os.getcwd(), "./tank-battle/assets/ff_vii_victory.wav")

BALL_X = MAX_X * (1 / 2)
BALL_Y = MAX_Y - 75

BALL_DX = -8
BALL_DY = -8

TANK_WIDTH = 20
TANK_HEIGHT = 75

TANK_X = MAX_X * (1 / 2)
TANK_Y = MAX_Y - TANK_HEIGHT

WALL_WIDTH = 20
WALL_HEIGHT = 275

WALL_SPACE = 5

TANK_SPEED = 1
TANK_ANGLE = 135
TANK_ANGLE2 = 225

BALL_WIDTH = 15
BALL_HEIGHT = 15

KEEP_PLAYING = True