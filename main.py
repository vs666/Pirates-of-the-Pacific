from data import *
import random
import math
from Players import *
from Coins import *
from Enemy import *
from Enemy import *
from Scores import *

pygame.init()

# make objects of the classes and initialize modifiable global variables
objects["player"] = []
objects["player"].append(Player(0))
objects["player"].append(Player(1))
objects["fixed_obstacles"] = Tank()
objects["dushman"] = Shark()
objects["ank"] = Score()
objects["paisa"] = Coin()
background = pygame.image.load('160.jpg')

# create the screenenemy
screen = pygame.display.set_mode((800, 800))
screen_name = "X-Over"

pygame.display.set_caption(screen_name)
start_ticks = pygame.time.get_ticks()  # starter tick
# calculate how many seconds
initial_time = start_ticks

# screen of the game is here
# this screen runs till exit button is pressed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if objects["mode"] == 0:
                if event.key == pygame.K_UP:  # and objects["mode"] == 0:
                    change_y = -3
                if event.key == pygame.K_DOWN:  # and objects["mode"] == 1:
                    change_y = +3
                if event.key == pygame.K_RIGHT:
                    change_x = +3
                if event.key == pygame.K_LEFT:
                    change_x = -3
            elif objects["mode"] == 1:
                if event.key == pygame.K_w:  # and objects["mode"] == 0:
                    change_y = -3
                if event.key == pygame.K_s:  # and objects["mode"] == 1:
                    change_y = +3
                if event.key == pygame.K_d:
                    change_x = +3
                if event.key == pygame.K_a:
                    change_x = -3
        if event.type == pygame.KEYUP:
            change_x = 0
            change_y = 0

    # background color is set to grey
    screen.fill((128, 128, 128))
    screen.blit(background, (0, 0))
    # change coordinates of players
    objects["player"][objects["mode"]].move(change_x, change_y)
    # update the position of players
    objects["player"][objects["mode"]].check()
    for i in range(objects["dushman"].enemy_count):
        objects["dushman"].enemy_X[i] = (objects["dushman"].enemy_X[i] +
                                         objects["dushman"].mov_x[i])
        if objects["dushman"].enemy_X[i] >= 746:
            # print("AAAH")
            objects["dushman"].remake_enemy(i)

    pygame.draw.rect(screen, cyan, (0, 64, 800, 64))
    pygame.draw.rect(screen, cyan, (0, 192, 800, 64))
    pygame.draw.rect(screen, cyan, (0, 320, 800, 64))
    pygame.draw.rect(screen, cyan, (0, 448, 800, 64))
    pygame.draw.rect(screen, cyan, (0, 576, 800, 64))
    pygame.draw.rect(screen, cyan, (0, 704, 800, 64))
    pygame.draw.rect(screen, cyan, (0, 448, 800, 64))

    objects["paisa"].coin()
    objects["fixed_obstacles"].place_tanks()
    objects["dushman"].enemy()

    # decrease the score at the end of 2 seconds and display the time and
    # update the score
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds > 2:
        start_ticks = seconds
        start_ticks = pygame.time.get_ticks()
        objects["ank"].score_value[objects["mode"]] -= 1

    font = pygame.font.Font('freesansbold.ttf', 25)
    textX = 700
    textY = 745
    a = font.render(
        str(math.floor(
            (pygame.time.get_ticks() - initial_time) / 1000)) + "seconds",
        True, (255, 255, 255))
    screen.blit(a, (textX, textY))

    # check if crossed the margin and hence increase the points accordingly
    objects["player"][objects["mode"]].position_update()
    for i in moving_obstacle_grid:
        if objects["player"][objects["mode"]].player_Y == i + 64:
            objects["ank"].score_value[objects["mode"]] += 3
            objects["player"][objects["mode"]].player_Y += 1
        if objects["player"][objects["mode"]].player_Y == i and i != 0:
            objects["ank"].score_value[objects["mode"]] += 6
            objects["player"][objects["mode"]].player_Y += 1

    # coin is found
    if objects["paisa"].coinCollide():
        objects["ank"].score_value[objects["mode"]] += 1
    objects["ank"].score_update()

    pygame.display.update()

    # check death of the current player
    if objects["dushman"].collide() or objects["fixed_obstacles"].tank_collide(
    ):
        pygame.time.delay(1000)
        life[objects["mode"]] = False
        objects["player"][objects["mode"]].change_visibility()

        # display the death message with score of the dead player
        screen2 = pygame.display.set_mode((800, 800))
        background = pygame.image.load('160.jpg')
        screen_name = "X-Over"
        pygame.display.set_caption(screen_name)
        screen2.fill((155, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', 45)
        headX = 150
        headY = 100
        heading = font.render("Player Dead", True, (255, 255, 255))
        screen2.blit(heading, (headX, headY))
        initial_time = start_ticks = pygame.time.get_ticks()
        font = pygame.font.Font('freesansbold.ttf', 35)
        p1_X = 100
        p1_Y = 200
        score1 = font.render(
            "Player " + str(objects["mode"] + 1) + "  Score on death is : " +
            str(objects["ank"].score_value[objects["mode"]]), True,
            (255, 255, 255))
        screen2.blit(score1, (p1_X, p1_Y))
        pygame.display.update()
        pygame.time.delay(2000)
        initial_time = start_ticks = pygame.time.get_ticks()
        objects["mode"] = 1 - objects["mode"]
        objects["player"][objects["mode"]].change_visibility()

    # check if crossed the level and the other player is alive
    elif objects["player"][objects["mode"]].checkEnd() and life[
            1 - objects["mode"]]:
        pygame.time.delay(1000)
        objects["player"][objects["mode"]].change_visibility()
        # display message on crossing the message
        screen2 = pygame.display.set_mode((800, 800))
        background = pygame.image.load('160.jpg')
        screen_name = "X-Over"
        pygame.display.set_caption(screen_name)
        # screen2.fill((0,0,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        headX = 150
        headY = 100
        heading = font.render("LEVEL OVER", True, (255, 255, 255))
        screen2.fill((0, 155, 0))
        screen2.blit(heading, (headX, headY))
        p1_X = 100
        p1_Y = 200
        score1 = font.render(
            "Player " + str(objects["mode"] + 1) + " CROSSED LEVEL " +
            str(level[objects["mode"]] - 1), True, (255, 255, 255))
        screen2.blit(score1, (p1_X, p1_Y))
        initial_time = start_ticks = pygame.time.get_ticks()
        pygame.display.update()
        pygame.time.delay(2000)

        objects["mode"] = 1 - objects["mode"]
        objects["player"][objects["mode"]].change_visibility()

    # check if crossed the level and the other player is dead

    elif objects["player"][objects["mode"]].checkEnd():
        # print("HAHA")
        start_ticks = pygame.time.get_ticks()
        screen2 = pygame.display.set_mode((800, 800))
        background = pygame.image.load('160.jpg')
        screen_name = "X-Over"
        pygame.display.set_caption(screen_name)
        font = pygame.font.Font('freesansbold.ttf', 45)
        headX = 150
        headY = 100
        heading = font.render("LEVEL OVER", True, (255, 255, 255))
        screen2.fill((0, 255, 0))
        screen2.blit(heading, (headX, headY))
        p1_X = 100
        p1_Y = 200
        score1 = font.render(
            "Player " + str(objects["mode"] + 1) + " CROSSED LEVEL " +
            str(level[objects["mode"] - 1]), True, (255, 255, 255))
        screen2.blit(score1, (p1_X, p1_Y))
        initial_time = start_ticks = pygame.time.get_ticks()
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.time.delay(1000)

    # check if both players are dead to reset them to level 1
    # this basically resets the game except the scores
    if life[0] is False and life[1] is False:
        pygame.time.delay(1000)
        life[0] = True
        life[1] = True
        level[0] = 1
        level[1] = 1
        # objects["mode"] = 1 - objects["mode"]
        objects["mode"] = 0
        objects["player"][0] = Player(0)
        objects["player"][1] = Player(1)
    # print(objects["ank"].score_value)

# this is the closing screen of the game
# it displays the total score of the 2 players and the winner among them
# makes use of a different screen ( pop-up ) to do so

if not running:
    running = True
    while running:
        screen = pygame.display.set_mode((600, 600))
        background = pygame.image.load('160.jpg')
        screen_name = "X-Over"
        pygame.display.set_caption(screen_name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        font = pygame.font.Font('freesansbold.ttf', 45)
        headX = 150
        headY = 100
        heading = font.render("GAME OVER", True, (255, 255, 255))
        screen.fill((125, 125, 125))
        screen.blit(heading, (headX, headY))
        font = pygame.font.Font('freesansbold.ttf', 20)
        p1_X = 100
        p1_Y = 200
        p2_X = 400
        p2_Y = 200
        score1 = font.render(
            "Player 1 : " + str(objects["ank"].score_value[0]), True,
            (255, 255, 255))
        screen.blit(score1, (p1_X, p1_Y))
        score2 = font.render(
            "Player 2 : " + str(objects["ank"].score_value[1]), True,
            (255, 255, 255))
        screen.blit(score2, (p2_X, p2_Y))
        if objects["ank"].score_value[1] > objects["ank"].score_value[0]:
            font = pygame.font.Font('freesansbold.ttf', 30)
            p1_X = 120
            p1_Y = 300
            score1 = font.render("Player 2 Wins", True, (255, 255, 255))
            screen.blit(score1, (p1_X, p1_Y))
        elif objects["ank"].score_value[1] < objects["ank"].score_value[0]:
            font = pygame.font.Font('freesansbold.ttf', 30)
            p1_X = 120
            p1_Y = 300
            score1 = font.render("Player 1 Wins", True, (255, 255, 255))
            screen.blit(score1, (p1_X, p1_Y))
        else:
            font = pygame.font.Font('freesansbold.ttf', 30)
            p1_X = 120
            p1_Y = 300
            score1 = font.render("Game Draw", True, (255, 255, 255))
        screen.blit(score1, (p1_X, p1_Y))

        pygame.display.update()
