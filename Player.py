from data import *
# from data import image
# from data import screen
# from data import mode
# from main import pygame



class Player:
    def __init__(self, mode):
        self.player_Image = pygame.image.load(image[mode])
        self.player_X = 400
        self.player_Y = 746 - mode * 746
        self.level = 1
        self.visible = True
        self.speed = 5 * self.level

    def position_update(self):
        screen.blit(self.player_Image, (self.player_X, self.player_Y))

    def move(self):
        self.player_X += self.speed
        self.player_Y += self.speed

    def cross_level(self):
        self.level += 1

    def change_visibility(self):
        self.visible = not self.visible
        if self.visible == False:
            screen.blit(self.player_Image, (-100, -100))
        else:
            self.position_update()

    def set_coordinates(self, x=400, y=746):
        self.player_X = x
        self.player_Y = y - mode * 746

    def check(self):
        if self.player_X > 746:
            self.player_X = 746
        elif self.player_X < 0:
            self.player_X = 0

        if self.player_Y > 746:
            self.player_Y = 746
        elif self.player_Y < 0:
            self.player_Y = 0

    def checkEnd(self):
        if self.player_Y <= 40 and mode == 0:
            self.level += 1
            self.set_coordinates()
            return True

        elif self.player_Y >= 746 and mode == 1:
            self.level += 1
            self.set_coordinates()
            return True
        return False
