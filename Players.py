from data import *

# from data import image
# from data import screen
# from data import objects["mode"]
# from main import pygame


# players class will handle the functionality of players
class Player:
    # this is a compulsary method like constructor
    def __init__(self, mode):
        self.player_Image = pygame.image.load(image[mode])
        self.player_X = 400
        self.player_Y = 746 - mode * 746
        # self.level = 1
        self.visible = mode == 0
        self.speed = 10 * level[mode]

    # this is to update the position of the player to the new position
    def position_update(self):
        screen.blit(self.player_Image, (self.player_X, self.player_Y))

    # this is to move the player acoording to speed
    #  not needed in this version of game(v1.0.1)
    def move(self):
        self.player_X += self.speed
        self.player_Y += self.speed

    # this is to increase the level if crossed
    def cross_level(self):
        self.level += 1

    # this is to add or remove the player from screen
    def change_visibility(self):
        self.visible = not self.visible
        if not self.visible:
            screen.blit(self.player_Image, (-100, -100))
        else:
            self.position_update()

    # this is to initialize the coordinates of the players
    def set_coordinates(self, x=400, y=746):
        self.player_X = x
        self.player_Y = y - objects["mode"] * 746

    # this is to shift the player by (x,y)
    def move(self, x=0, y=0):
        self.player_X += x
        self.player_Y += y

    # this is an inspection to that the player doesnot cross the boundaries
    def check(self):
        if self.player_X > 746:
            self.player_X = 746
        elif self.player_X < 0:
            self.player_X = 0

        if self.player_Y > 746:
            self.player_Y = 746
        elif self.player_Y < 0:
            self.player_Y = 0

    # this is to check if player has crossed the level
    def checkEnd(self):
        if self.player_Y <= 40 and objects["mode"] == 0:
            level[objects["mode"]] += 1
            self.set_coordinates()
            return True

        elif self.player_Y >= 746 and objects["mode"] == 1:
            level[objects["mode"]] += 1
            self.set_coordinates()
            return True
        return False
