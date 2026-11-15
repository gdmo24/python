import pygame
from config import *
from player import Player
from obstacle import Obstacle

# ============================================
# 1. PREPARATION (this part runs only once)
# ============================================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Olgi-Alvaro Atacks")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Font to write text on the screen

# Create the player (moves with the arrow keys)
player = Player(PLAYER1_START_X, PLAYER1_START_Y)

obstacles = []  # List to store the obstacles that are falling

last_obstacle_spawn_time = pygame.time.get_ticks()  # When the last obstacle appeared
spawn_delay = SPAWN_OBSTACLE_DELAY                  # Challenge 7: time between obstacles

score = 0           # Current score
high_score = 0      # Challenge 9: best score while the program is open
game_over = False   # True when an obstacle hits a player
paused = False      # Challenge 4: True when the game is paused

survival_time = 0                           # Challenge 6: milliseconds survived
last_frame_time = pygame.time.get_ticks()   # Challenge 6: time of the previous frame

# ============================================
# 2. GAME LOOP (this part repeats 60 times per second)
# ============================================
running = True
while running:

    # ---------- 2.1 EVENTS (things the user does once: close, press a key) ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # A key has just been pressed

            # Challenge 4: ESC pauses and un-pauses (only while playing)
            if event.key == pygame.K_ESCAPE and not game_over:
                paused = not paused  # True becomes False, False becomes True
                if not paused:
                    # Start counting again, so an obstacle does not appear at once
                    last_obstacle_spawn_time = pygame.time.get_ticks()

            # Challenge 5: R starts a new game (only after Game Over)
            if event.key == pygame.K_r and game_over:
                score = 0                   # Score back to zero
                obstacles = []              # Remove all obstacles
                player.reset_position()     # Player back to the start
                survival_time = 0           # Challenge 6: timer back to zero
                last_obstacle_spawn_time = pygame.time.get_ticks()
                game_over = False           # Play again!
                # high_score is NOT changed (Challenge 9)

            # Challenge 8: "+" makes the player faster, "-" makes it slower
            if event.unicode == "+":
                player.speed = player.speed + 1
                if player.speed > MAX_PLAYER_SPEED:
                    player.speed = MAX_PLAYER_SPEED
            if event.unicode == "-":
                player.speed = player.speed - 1
                if player.speed < MIN_PLAYER_SPEED:
                    player.speed = MIN_PLAYER_SPEED

    # ---------- 2.2 TIME ----------
    current_time = pygame.time.get_ticks()                # Milliseconds since the game started
    time_since_last_frame = current_time - last_frame_time
    last_frame_time = current_time

    # ---------- 2.3 UPDATE (only when playing: not paused and not game over) ----------
    if not game_over and not paused:

        # Challenge 6: add the time of this frame to the survival timer
        survival_time = survival_time + time_since_last_frame

        # Challenge 7: every 10 points, obstacles appear 50 ms sooner (minimum 150 ms)
        level = score // POINTS_PER_LEVEL   # 0-9 points -> 0, 10-19 -> 1, 20-29 -> 2...
        spawn_delay = SPAWN_OBSTACLE_DELAY - level * SPAWN_DELAY_STEP
        if spawn_delay < MIN_SPAWN_DELAY:
            spawn_delay = MIN_SPAWN_DELAY

        # Create a new obstacle when enough time has passed
        if current_time - last_obstacle_spawn_time > spawn_delay:
            obstacles.append(Obstacle())
            last_obstacle_spawn_time = current_time

        # Move each obstacle and check if it hits a player
        for obstacle in obstacles:
            obstacle.move()
            if player.rect.colliderect(obstacle.rect):
                game_over = True

        # Remove obstacles that are off the screen (and give 1 point for each)
        visible_obstacles = []
        for obstacle in obstacles:
            if not obstacle.is_off_screen():
                visible_obstacles.append(obstacle)
            else:
                score += 1
        obstacles = visible_obstacles

        # Challenge 9: save the best score
        if score > high_score:
            high_score = score

        # Move the player
        player.moveArrows()

    # ---------- 2.4 DRAW EVERYTHING ----------
    screen.fill(BACKGROUND_COLOR)
    player.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)

    # Score and best score (Challenge 9)
    score_text = font.render(f"Score: {score}   Best: {high_score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

    # Survival time in seconds (Challenge 6). 1000 milliseconds = 1 second
    time_text = font.render(f"Time: {survival_time // 1000} s", True, TEXT_COLOR)
    screen.blit(time_text, (10, 45))

    # Speed of the player (Challenge 8)
    speed_text = font.render(f"Speed: {player.speed}", True, TEXT_COLOR)
    screen.blit(speed_text, (10, 80))

    # Challenge 4: PAUSE message in the middle of the screen
    if paused:
        pause_text = font.render("PAUSE", True, PAUSE_COLOR)
        screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))

    # Game Over message + how to restart (Challenge 5)
    if game_over:
        game_over_text = font.render("Game Over", True, GAME_OVER_COLOR)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 20))
        restart_text = font.render("Press R to play again", True, TEXT_COLOR)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()   # Show on the screen everything we have drawn
    clock.tick(FPS)         # Wait so the game runs at 60 frames per second

# Quit Pygame
pygame.quit()
