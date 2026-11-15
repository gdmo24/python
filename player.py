import pygame
from config import *


class Player:
    """The player controlled by the user"""

    def __init__(self, x, y, color=PLAYER_COLOR, speed=PLAYER_SPEED):
        """Initialize the player with a position and size"""
        self.rect = pygame.Rect(x, y, 50, 50)  # Square of 50x50 pixels
        self.color = color
        self.speed = speed
        # Remember where the player started (Challenge 5: restart)
        self.start_x = x
        self.start_y = y

    def moveArrows(self):
        """Update the player's position using the arrow keys"""
        keys = pygame.key.get_pressed()  # Get the state of all keyboard keys

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.keep_inside_screen()  # Challenge 1: do not leave the window

    def keep_inside_screen(self):
        """Challenge 1: if the player goes out of the window, put it back on the edge"""
        if self.rect.left < 0:          # Too far to the left
            self.rect.left = 0
        if self.rect.right > WIDTH:     # Too far to the right
            self.rect.right = WIDTH
        if self.rect.top < 0:           # Too far up
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:   # Too far down
            self.rect.bottom = HEIGHT

    def reset_position(self):
        """Challenge 5: move the player back to where it started"""
        self.rect.x = self.start_x
        self.rect.y = self.start_y

    def draw(self, surface):
        """Draw the player on the given surface"""
        pygame.draw.rect(surface, self.color, self.rect)
