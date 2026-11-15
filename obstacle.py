import pygame
import random

from config import *


class Obstacle:
    """An obstacle that the player must avoid"""

    def __init__(self):
        # Challenge 2: random size between 20 and 70 pixels
        size = random.randint(MIN_OBSTACLE_SIZE, MAX_OBSTACLE_SIZE)
        # Random x position, but never outside the window (WIDTH - size)
        x = random.randint(0, WIDTH - size)
        # The obstacle starts just above the top of the window (y = -size)
        self.rect = pygame.Rect(x, -size, size, size)
        self.color = random.choice(OBSTACLES_COLORS)  # Random color
        self.speed = random.randint(2, 7)             # Random falling speed

    def move(self):
        """Move the obstacle down the screen"""
        self.rect.y += self.speed

    def is_off_screen(self):
        """Check if the obstacle has gone below the bottom of the screen"""
        return self.rect.y > HEIGHT

    def draw(self, surface):
        """Draw the obstacle on the given surface"""
        pygame.draw.rect(surface, self.color, self.rect)
