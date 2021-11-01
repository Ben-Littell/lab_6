import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
AZURE = (55, 198, 255)
CERULEAN = (0, 171, 240)
COLORS = [RED, GREEN, BLUE, BLACK]

# Math Constants
PI = math.pi

# Game Constants
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
FPS = 60


##############################################################################
class Background:
    def __init__(self, player_color, b_color, c_color, c_start):
        self.player_color = player_color
        self.b_color = b_color
        self.c_color = c_color
        self.c_start = c_start

    def draw_back(self):
        # fill color
        pygame.draw.rect(screen, self.b_color, (0, 0, WIDTH, HEIGHT))
        # clouds
        cloud_x1 = self.c_start
        cloud_x2 = self.c_start + 10
        cloud_x3 = self.c_start - 10
        cloud_x4 = self.c_start + 25
        change_x = 0
        for numb in range(5):
            pygame.draw.ellipse(screen, self.c_color, (cloud_x1 + change_x, 30, 50, 30))
            pygame.draw.ellipse(screen, self.c_color, (cloud_x2 + change_x, 45, 50, 30))
            pygame.draw.ellipse(screen, self.c_color, (cloud_x3 + change_x, 35, 50, 30))
            pygame.draw.ellipse(screen, self.c_color, (cloud_x4 + change_x, 33, 50, 30))
            change_x += 140
        change_x = 70
        for numb in range(4):
            pygame.draw.ellipse(screen, self.c_color, (cloud_x1 + change_x, 100, 50, 30))
            pygame.draw.ellipse(screen, self.c_color, (cloud_x2 + change_x, 115, 50, 30))
            pygame.draw.ellipse(screen, self.c_color, (cloud_x3 + change_x, 105, 50, 30))
            pygame.draw.ellipse(screen, self.c_color, (cloud_x4 + change_x, 103, 50, 30))
            change_x += 140


##############################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Collision Detection Intro')

clock = pygame.time.Clock()
###################################
background = Background(BLACK, CERULEAN, WHITE, 30)
###################################
running = True
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    background.draw_back()
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
