# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kieran Kahler
#               Zachary Martin
#               Ashlyn Nobles
#               Jinghan Xue
# Section:      418 / 518
# Assignment:   ENGR 102 PROJECT
# Date:         12/8/21
#

#
# YOUR CODE HERE
#

import pygame

pygame.init()
pygame.font.init()
size = [1440, 800]
done = False

# this determines the frame rate of the game
clock = pygame.time.Clock()

# this creates the game window and background
pygame.display.set_caption("PYTHONS AND LADDERS DEMO")
bg = pygame.image.load("forest.jpeg")
bg = pygame.transform.smoothscale(bg, size)
screen = pygame.display.set_mode(size)


def diceroll(x_val, y_val, scale, face):
    '''loads a dice onto the board with a certain face showing up top
    :param x_val = the x value where the dice will be loaded
    :param y_val = the y value where the dice will be loaded
    :param scale = the scale of the dice
    :param face = will determine what dice face is displayed'''

    dice1 = pygame.image.load("dice picture/asset_dice_1.png")
    dice2 = pygame.image.load("dice picture/asset_dice_2.png")
    dice3 = pygame.image.load("dice picture/asset_dice_3.png")
    dice4 = pygame.image.load("dice picture/asset_dice_4.png")
    dice5 = pygame.image.load("dice picture/asset_dice_5.png")
    dice6 = pygame.image.load("dice picture/asset_dice_6.png")

    # there are 6 faces, and one will be displayed faced on the face number
    if face == 1:
        dice1 = pygame.transform.smoothscale(dice1, (scale, scale))
        screen.blit(dice1, (x_val, y_val))
    elif face == 2:
        dice2 = pygame.transform.smoothscale(dice2, (scale, scale))
        screen.blit(dice2, (x_val, y_val))
    elif face == 3:
        dice3 = pygame.transform.smoothscale(dice3, (scale, scale))
        screen.blit(dice3, (x_val, y_val))
    elif face == 4:
        dice4 = pygame.transform.smoothscale(dice4, (scale, scale))
        screen.blit(dice4, (x_val, y_val))
    elif face == 5:
        dice5 = pygame.transform.smoothscale(dice5, (scale, scale))
        screen.blit(dice5, (x_val, y_val))
    elif face == 6:
        dice6 = pygame.transform.smoothscale(dice6, (scale, scale))
        screen.blit(dice6, (x_val, y_val))



