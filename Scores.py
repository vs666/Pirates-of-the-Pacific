from data import *
# this imports all the globally used variables shared among all classes

# score


class Score:
    # this is a compulsary constructor sort of function
    def __init__(self):
        self.score_value = [0, 0]
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textX = 10
        self.textY = 10
        self.score_update()

    # this is to update scores and display them on screen
    def score_update(self):
        self.score = self.font.render(
            "Score : " + str(self.score_value[objects["mode"]]) +
            "   Player " + str(objects["mode"] + 1) + "   Level : " +
            str(level[objects["mode"]]), True, (255, 255, 255))
        screen.blit(self.score, (self.textX, self.textY))

# score class is used to update the score of players whenever the only
# method in it is invoked
