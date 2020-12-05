from data import *
# from data import screen
# from data import player
# from data import objects["mode"]
import random

# from main import pygame

# this python file has 2 classes that have created 2 types of enemies


# this is tank that is a fixed obstacle
# this class is a blueprint of tanks and makes many tanks
class Tank:
    # this is a compulsary method like constructor
    def __init__(self):
        self.tankcount = 10
        self.tankImg = []
        self.tankX = []
        self.tankY = []
        self.make_tanks()

    # this will make tanks on the screen (fixed)
    def make_tanks(self):
        for i in range(5):
            if i + 1 == 3 or i + 1 == 5:
                self.tankImg.append(pygame.image.load('military.png'))
                self.tankImg.append(pygame.image.load('military.png'))
                self.tankImg.append(pygame.image.load('military.png'))
                self.tankX.append(100)
                self.tankX.append(400)
                self.tankX.append(700)
                self.tankY.append(moving_obstacle_grid[i] + 64)
                self.tankY.append(moving_obstacle_grid[i] + 64)
                self.tankY.append(moving_obstacle_grid[i] + 64)
            elif i != 0:
                self.tankImg.append(pygame.image.load('military.png'))
                self.tankImg.append(pygame.image.load('military.png'))
                self.tankX.append(300)
                self.tankX.append(600)
                self.tankY.append(moving_obstacle_grid[i] + 64)
                self.tankY.append(moving_obstacle_grid[i] + 64)

    # this will place/draw the tanks on the screen
    def place_tanks(self):
        for i in range(self.tankcount):
            screen.blit(self.tankImg[i], (self.tankX[i], self.tankY[i]))

    # this will be used in later update of the game
    def check_tanks(self):
        for i in range(self.tankcount):
            pass

    # this is to check if the player has collided with tank
    def tank_collide(self):
        for i in range(self.tankcount):
            if abs(self.tankX[i] -
                   objects["player"][objects["mode"]].player_X) <= 45 and abs(
                       self.tankY[i] -
                       objects["player"][objects["mode"]].player_Y) <= 45:
                print("collided")
                return True
        return False


# this is the class for moving object
# this is for sharks that are in deep water


class Shark:
    # this is a function type constructor
    def __init__(self):
        self.enemy_count = 8
        self.shark_Image = []
        self.enemy_X = []
        self.enemy_Y = []
        self.mov_x = []
        self.initialize()

    # this is to initialize the elements
    def initialize(self):
        for i in range(self.enemy_count):
            self.shark_Image.append(pygame.image.load('shark.png'))
            self.enemy_X.append(random.randint(0, 746))
            self.enemy_Y.append(moving_obstacle_grid[random.randint(
                1,
                len(moving_obstacle_grid) - 1)])
        for i in range(self.enemy_count):
            self.mov_x.append(random.randint(1, 5))

    # this is a method to draw the image of the sharks
    def enemy(self):
        for i in range(self.enemy_count):
            screen.blit(self.shark_Image[i],
                        (self.enemy_X[i], self.enemy_Y[i]))
            # pygame.time.delay(10)

    # this is to remake the sharks in a random position
    #  when it runs out of screen
    def remake_enemy(self, i):
        self.enemy_X[i] = 0
        self.mov_x[i] = random.randint(1, 2 * level[objects["mode"]])
        self.enemy_Y[i] = moving_obstacle_grid[random.randint(
            1,
            len(moving_obstacle_grid) - 1)]
        screen.blit(self.shark_Image[i], (self.enemy_X[i], self.enemy_Y[i]))

    # this is to check if the player has collided with shark or not
    def collide(self):
        # print("In\n")
        for i in range(self.enemy_count):
            # print("out")
            if abs(self.enemy_X[i] -
                   objects["player"][objects["mode"]].player_X) <= 45 and abs(
                       self.enemy_Y[i] -
                       objects["player"][objects["mode"]].player_Y) <= 45:
                print("collided")
                return True
        return False
