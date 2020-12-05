import pygame
# this is method to store all the data
# as the global variables
pygame.init()

# this is the screen initialization
screen = pygame.display.set_mode((800, 800))

life = [True, True]
running = True
mode = 0

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

moving_obstacle_grid = [0, 128, 256, 384, 512, 640]
level = [1, 1]
objects = {
    "player": None,
    "dushman": None,
    "ank": None,
    "paisa": None,
    "fixed_obstacles": None,
    "mode": 0
}   # variable data
# objects["mode"]
player = []
fixed_obstacles = -1
dushman = -1
ank = -1
paisa = -1

change_x = 0
change_y = 0
running = True
cyan = (0, 100, 100)

change_x = 0
change_y = 0
running = True
cyan = (0, 100, 100)

image = ['ship.png', 'frigate.png']
time = [0, 0]
