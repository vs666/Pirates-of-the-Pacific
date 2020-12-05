from data import *
import random


# coin class is used to check all the functionalities of coins in the game
class Coin:

    # this is the compulsary constructor method
    def __init__(self):
        self.bitcoin = []
        self.bcX = []
        self.bcY = []
        self.coin_amount = 12
        self.initialize()
    # this is to initialize the coins on the screen

    def initialize(self):
        for i in range(self.coin_amount):
            self.bitcoin.append(pygame.image.load('bitcoin.png'))
            self.bcX.append(random.randint(32, 746))
            self.bcY.append(random.randint(32, 746))

    # this is to put/draw the coins on the screen
    def coin(self):
        for i in range(self.coin_amount):
            screen.blit(self.bitcoin[i], (self.bcX[i], self.bcY[i]))
    # this is to add a coin if a coin is consumed by the ship

    def addCoin(self, i):
        self.bcX[i] = random.randint(32, 746)
        self.bcY[i] = random.randint(32, 746)
        screen.blit(self.bitcoin[i], (self.bcX[i], self.bcY[i]))

    # this is to check if an object (ship) has collided with a coin and
    # consumed it
    def coinCollide(self):
        for i in range(self.coin_amount):
            # print("HERE")
            if abs(self.bcX[i] -
                   objects["player"][objects["mode"]].player_X) <= 32 and abs(
                       self.bcY[i] -
                       objects["player"][objects["mode"]].player_Y) <= 32:
                self.addCoin(i)
                return True
        return False
