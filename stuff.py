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
enemy_list = []


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


class Player:
    def __init__(self, display, x, y, width, height, x_speed=0, y_speed=0):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_speed = x_speed
        self.y_speed = y_speed

    def draw_player(self):
        pygame.draw.rect(self.display, RED, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.x += -1 * self.x_speed
        if self.y <= 0 or self.y >= HEIGHT - self.height:
            self.y += -1 * self.y_speed


class Enemies:
    def __init__(self, e_height, e_width, s_width, velocity=5):
        self.e_height = e_height
        self.e_width = e_width
        self.s_width = s_width
        self.velocity = velocity

    def draw_enemies(self):
        s_place = random.randrange(self.s_width - self.e_width)
        pygame.draw.rect(screen, BLACK, (s_place, 10, self.e_height, self.e_width))

    def update(self):
        self.e_height += self.velocity


##############################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Collision Detection Intro')

clock = pygame.time.Clock()
###################################
background = Background(BLACK, CERULEAN, WHITE, 30)
player1 = Player(screen, 200, HEIGHT - 80, 45, 45)
for numb in range(50):
    enemy = Enemies(10, -10, WIDTH - 20)
    enemy_list.append(enemy)
enemy1 = Enemies(10, 10, WIDTH)
###################################

running = True
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player1.x_speed = 0
                # player.y_speed = 0
            if event.key == pygame.K_LEFT:
                player1.x_speed = 0
                # player.y_speed = 0
            # if event.key == pygame.K_UP:
            #     player1.y_speed = 0
            #     # player.x_speed = 0
            # if event.key == pygame.K_DOWN:
            #     player1.y_speed = 0
            #     # player.x_speed = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1.x_speed = 10
                # player.y_speed = 0
            if event.key == pygame.K_LEFT:
                player1.x_speed = -10
                # player.y_speed = 0
            # if event.key == pygame.K_UP:
            #     player1.y_speed = -5
            #     # player.x_speed = 0
            # if event.key == pygame.K_DOWN:
            #     player1.y_speed = 5
            #     # player.x_speed = 0
            if event.key == pygame.K_SPACE:
                player1.x_speed = 0
                player1.y_speed = 0

    screen.fill(WHITE)
    background.draw_back()
    player1.draw_player()
    player1.update()
    for item in enemy_list:
        item.draw_enemies()
        item.update()
    enemy1.draw_enemies()
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
