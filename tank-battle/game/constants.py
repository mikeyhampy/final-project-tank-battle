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

TANK_ANGLE_CHANGE1 = (BARREL_HEIGHT)/(170 / 3)
TANK_ANGLE_CHANGE2 = (-(BARREL_HEIGHT))/90
TANK_ANGLE_ADDER1 = 0
TANK_ANGLE_ADDER2 = 0


BALL_X1 = BARREL_X1
BALL_X2 = BARREL_X2
BALL_Y = TANK_Y + (BARREL_HEIGHT/2) - (BALL_HEIGHT / 2)




KEEP_PLAYING = True

RIGHT_PLAYER_LOSES = False
LEFT_PLAYER_LOSES = False