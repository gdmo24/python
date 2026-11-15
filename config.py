# ============================================
# GAME SETTINGS (all the fixed numbers of the game)
# ============================================

# Window size
WIDTH = 1000
HEIGHT = 600
FPS = 60  # How many times per second the screen is redrawn

# Colors (Red, Green, Blue)
BACKGROUND_COLOR = (0, 0, 0)      # Black background
PLAYER_COLOR = (60, 140, 255)     # Blue player
TEXT_COLOR = (255, 255, 255)      # White text
GAME_OVER_COLOR = (255, 0, 0)     # Red text
PAUSE_COLOR = (255, 255, 0)       # Yellow text

OBSTACLES_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Player
PLAYER_SPEED = 6        # Starting speed of the player
MIN_PLAYER_SPEED = 2    # Challenge 8: lowest speed allowed
MAX_PLAYER_SPEED = 12   # Challenge 8: highest speed allowed

# Starting position of the player (Challenge 5: used when restarting)
PLAYER1_START_X = 375
PLAYER1_START_Y = 530

# Obstacles
MIN_OBSTACLE_SIZE = 20  # Challenge 2: smallest obstacle
MAX_OBSTACLE_SIZE = 70  # Challenge 2: biggest obstacle

SPAWN_OBSTACLE_DELAY = 500  # Milliseconds between new obstacles at the start
SPAWN_DELAY_STEP = 50       # Challenge 7: milliseconds removed every 10 points
MIN_SPAWN_DELAY = 150       # Challenge 7: the delay can never go below this
POINTS_PER_LEVEL = 10       # Challenge 7: every 10 points the game gets harder
