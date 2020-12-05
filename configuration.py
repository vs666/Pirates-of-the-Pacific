# import pygame
# import random
# # from main import *
# from pygame import mixer
# #initialize the pygame
# pygame.init()

# #  This is not inherited from pygame but created by the develper

# image = ['ship.png', 'frigate.png']
# time = [0, 0]


# class Player:
#     def __init__(self, mode):
#         self.player_Image = pygame.image.load(image[mode])
#         self.player_X = 400
#         self.player_Y = 746 - mode * 746
#         self.level = 1
#         self.visible = True
#         self.speed = 5 * self.level

#     def position_update(self):
#         screen.blit(self.player_Image, (self.player_X, self.player_Y))

#     def move(self):
#         self.player_X += self.speed
#         self.player_Y += self.speed

#     def cross_level(self):
#         self.level += 1

#     def change_visibility(self):
#         self.visible = not self.visible
#         if self.visible == False:
#             screen.blit(self.player_Image, (-100, -100))
#         else:
#             self.position_update()

#     def set_coordinates(self, x=400, y=746):
#         self.player_X = x
#         self.player_Y = y - mode * 746

#     def check(self):
#         if self.player_X > 746:
#             self.player_X = 746
#         elif self.player_X < 0:
#             self.player_X = 0

#         if self.player_Y > 746:
#             self.player_Y = 746
#         elif self.player_Y < 0:
#             self.player_Y = 0

#     def checkEnd(self):
#         if self.player_Y <= 40 and mode == 0:
#             self.level += 1
#             self.set_coordinates()
#             return True

#         elif self.player_Y >= 746 and mode == 1:
#             self.level += 1
#             self.set_coordinates()
#             return True
#         return False


# life = [True, True]
# #decide which player is playing
# mode = 0
# white = (255, 255, 255)
# green = (0, 255, 0)
# blue = (0, 0, 128)
# black = (0, 0, 0)
# red = (255, 0, 0)

# # create the display surface object
# # of specific dimension..e(X,Y).

# moving_obstacle_grid = [0, 128, 256, 384, 512, 640]
# #load background
# background = pygame.image.load('160.jpg')

# #create the screenenemy
# screen = pygame.display.set_mode((800, 800))
# screen_name = "X-Over"
# pygame.display.set_caption(screen_name)

# #icon variable
# icon = pygame.image.load('road.png')
# pygame.display.set_icon(icon)

# display_surface = pygame.display.set_mode((800, 800))
# stripe_count = 3


# #icon for player
# class Tank:
#     def __init__(self):
#         self.tankcount = 10
#         self.tankImg = []
#         self.tankX = []
#         self.tankY = []
#         self.make_tanks()

#     def make_tanks(self):
#         for i in range(5):
#             if i + 1 == 3 or i + 1 == 5:
#                 self.tankImg.append(pygame.image.load('military.png'))
#                 self.tankImg.append(pygame.image.load('military.png'))
#                 self.tankImg.append(pygame.image.load('military.png'))
#                 self.tankX.append(100)
#                 self.tankX.append(400)
#                 self.tankX.append(700)
#                 self.tankY.append(moving_obstacle_grid[i] + 64)
#                 self.tankY.append(moving_obstacle_grid[i] + 64)
#                 self.tankY.append(moving_obstacle_grid[i] + 64)
#             elif i != 0:
#                 self.tankImg.append(pygame.image.load('military.png'))
#                 self.tankImg.append(pygame.image.load('military.png'))
#                 self.tankX.append(300)
#                 self.tankX.append(600)
#                 self.tankY.append(moving_obstacle_grid[i] + 64)
#                 self.tankY.append(moving_obstacle_grid[i] + 64)

#     def place_tanks(self):
#         for i in range(self.tankcount):
#             screen.blit(self.tankImg[i], (self.tankX[i], self.tankY[i]))

#     def check_tanks(self):
#         for i in range(self.tankcount):
#             pass

#     def tank_collide(self):
#         for i in range(self.tankcount):
#             if abs(self.tankX[i] - player[mode].player_X) <= 45 and abs(
#                     self.tankY[i] - player[mode].player_Y) <= 45:
#                 print("collided")
#                 return True
#         return False


# class Shark:
#     def __init__(self):
#         self.enemy_count = 8
#         self.shark_Image = []
#         self.enemy_X = []
#         self.enemy_Y = []
#         self.mov_x = []
#         self.initialize()

#     def initialize(self):
#         for i in range(self.enemy_count):
#             self.shark_Image.append(pygame.image.load('shark.png'))
#             self.enemy_X.append(random.randint(0, 746))
#             self.enemy_Y.append(moving_obstacle_grid[random.randint(
#                 1,
#                 len(moving_obstacle_grid) - 1)])
#         for i in range(self.enemy_count):
#             self.mov_x.append(random.randint(1, 5))

#     def enemy(self):
#         for i in range(self.enemy_count):
#             screen.blit(self.shark_Image[i],
#                         (self.enemy_X[i], self.enemy_Y[i]))
#             # pygame.time.delay(10)

#     def remake_enemy(self, i):
#         self.enemy_X[i] = 0
#         self.mov_x[i] = random.randint(1, 2 * player[mode].level)
#         self.enemy_Y[i] = moving_obstacle_grid[random.randint(
#             1,
#             len(moving_obstacle_grid) - 1)]
#         screen.blit(self.shark_Image[i], (self.enemy_X[i], self.enemy_Y[i]))

#     def collide(self):
#         # print("In\n")
#         for i in range(self.enemy_count):
#             # print("out")
#             if abs(self.enemy_X[i] - player[mode].player_X) <= 45 and abs(
#                     self.enemy_Y[i] - player[mode].player_Y) <= 45:
#                 print("collided")
#                 return True
#         return False


# #score
# class Score:
#     def __init__(self):
#         self.score_value = [0, 0]
#         self.font = pygame.font.Font('freesansbold.ttf', 32)
#         self.textX = 10
#         self.textY = 10
#         self.score_update()

#     def score_update(self):
#         self.score = self.font.render(
#             "Score : " + str(self.score_value[mode]) + "   Player " +
#             str(mode + 1) + "   Level : " + str(player[mode].level), True,
#             (255, 255, 255))
#         screen.blit(self.score, (self.textX, self.textY))


# change_x = 0
# change_y = 0
# running = True
# cyan = (0, 100, 100)


# class Coin:
#     def __init__(self):
#         self.bitcoin = []
#         self.bcX = []
#         self.bcY = []
#         self.coin_amount = 12
#         self.initialize()

#     def initialize(self):
#         for i in range(self.coin_amount):
#             self.bitcoin.append(pygame.image.load('bitcoin.png'))
#             self.bcX.append(random.randint(32, 746))
#             self.bcY.append(random.randint(32, 746))

#     def coin(self):
#         for i in range(self.coin_amount):
#             screen.blit(self.bitcoin[i], (self.bcX[i], self.bcY[i]))

#     def addCoin(self, i):
#         self.bcX[i] = random.randint(32, 746)
#         self.bcY[i] = random.randint(32, 746)
#         screen.blit(self.bitcoin[i], (self.bcX[i], self.bcY[i]))

#     def coinCollide(self):
#         for i in range(self.coin_amount):
#             # print("HERE")
#             if abs(self.bcX[i] - player[mode].player_X) <= 32 and abs(
#                     self.bcY[i] - player[mode].player_Y) <= 32:
#                 self.addCoin(i)
#                 return True
#         return False


# player = [Player(0), Player(1)]
# fixed_obstacles = Tank()
# dushman = Shark()
# ank = Score()
# paisa = Coin()
