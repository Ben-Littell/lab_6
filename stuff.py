import pygame
import math
import random

# use the arrow keys to move side to side to avoid the falling asteroids
# 3 lives and you are done, press r to restart

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
velo = 5
rounds = 0


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
        self.space_ship = pygame.image.load("Space_ship.png")

    def draw_player(self):
        # pygame.draw.rect(self.display, RED, (self.x, self.y, self.width, self.height))
        screen.blit(self.space_ship, [self.x, self.y])

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.x += -1 * self.x_speed
        if self.y <= 0 or self.y >= HEIGHT - self.height:
            self.y += -1 * self.y_speed


class Enemies:
    def __init__(self, e_height, e_width, s_width, y=10, velocity=5):
        self.e_height = e_height
        self.e_width = e_width
        self.s_width = s_width
        self.velocity = velocity
        self.s_place = random.randrange(self.s_width - self.e_width)
        self.y = y
        self.rounds = 0
        self.color = WHITE
        self.asteroid = pygame.image.load("asteroid.png")

    def draw_enemies(self):
        # pygame.draw.rect(screen, self.color, (self.s_place, self.y, self.e_height, self.e_width))
        screen.blit(self.asteroid, [self.s_place, self.y])

    def update(self):
        self.y += self.velocity
        if self.y >= HEIGHT + 10:
            self.s_place = random.randrange(self.s_width - self.e_width)
            self.y = -10
            self.velocity += 0.1
            if self.velocity > 10:
                self.velocity = 10
        # print(self.velocity)


##############################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Collision Detection Intro')

clock = pygame.time.Clock()
###################################
background = Background(BLACK, CERULEAN, WHITE, 30)
player1 = Player(screen, 200, HEIGHT - 80, 30, 30)
for numb in range(25):
    enemy = Enemies(10, 10, WIDTH - 10, velocity=velo)
    enemy_list.append(enemy)
enemy1 = Enemies(10, 10, WIDTH)
collisions = 3
font_size1 = 50
rounds1 = 0
background_image = pygame.image.load("background-4_resized.png")
collision_sound = pygame.mixer.Sound("rock_breaking.ogg")
###################################

running = True
# game loop
while running:
    collided = False
    enemy_x_r = []
    player_x_r = []
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
                player1.x_speed = 5
                # player.y_speed = 0
            if event.key == pygame.K_LEFT:
                player1.x_speed = -5
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
            if collisions <= 0:
                if event.key == pygame.K_r:
                    collisions = 3
                    for item in enemy_list:
                        item.velocity = 5

    screen.fill(WHITE)

    screen.blit(background_image, [0, 0])
    # background.draw_back()
    player1.draw_player()
    player1.update()
    for item in enemy_list:
        item.draw_enemies()
        item.update()
        if item.y >= HEIGHT:
            rounds1 += 1
        for numb in range(item.s_place, item.s_place + item.e_width):
            enemy_x_r.append(numb)
        for numb in range(player1.x, player1.x + player1.width):
            if numb in enemy_x_r and player1.y <= item.y:
                collided = True

    rounds += rounds1 / 50
    rounds1 = 0

    if collided:
        collisions -= 1
        for item in enemy_list:
            item.y = -10
        rounds += 1
        collision_sound.play()

    font1 = pygame.font.SysFont('Calibri', 25, True, False)
    text1 = font1.render(f"Lives {collisions}", True, WHITE)
    screen.blit(text1, [10, 25])
    font4 = pygame.font.SysFont('Calibri', 25, True, False)
    text4 = font4.render(f"Rounds {int(rounds)}", True, WHITE)
    screen.blit(text4, [500, 25])

    if collisions <= 0:
        screen.fill(BLACK)
        font2 = pygame.font.SysFont('Calibri', font_size1, True, False)
        text2 = font2.render(f"Game Over", True, WHITE)
        font3 = pygame.font.SysFont('Calibri', 20, True, False)
        text3 = font3.render(f"Press r to restart", True, WHITE)
        screen.blit(text2, [225, HEIGHT / 2 - font_size1])
        screen.blit(text3, [225, HEIGHT / 2 + 10])
        rounds = 0
        for item in enemy_list:
            item.velocity = 0
            item.y = -10

    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
