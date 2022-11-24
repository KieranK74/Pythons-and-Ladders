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
size = [1440, 800]
screen = pygame.display.set_mode(size)


def createladder(x_val, y_val, angle, scale):
    '''loads a ladder onto the board
        :param x_val = the x value where the ladder will be loaded
        :param y_val = the y value where the ladder will be loaded
        :param angle = the angle which the ladder will be tilted
        :param scale = the scale of the image'''
    ladder = pygame.image.load('ladder.png')
    ladder = pygame.transform.smoothscale(ladder, (scale / 1.5, scale))
    ladder = pygame.transform.rotate(ladder, angle)
    screen.blit(ladder, (x_val, y_val))


def createbigladder(x_val, y_val, angle, scale):
    '''loads a big ladder onto the board
            :param x_val = the x value where the ladder will be loaded
            :param y_val = the y value where the ladder will be loaded
            :param angle = the angle which the ladder will be tilted
            :param scale = the scale of the image'''
    ladder = pygame.image.load('bigladder.png')
    ladder = pygame.transform.smoothscale(ladder, (scale / 2, scale))
    ladder = pygame.transform.rotate(ladder, angle)
    screen.blit(ladder, (x_val, y_val))


def createsuperbigladder(x_val, y_val, angle, scale):
    '''loads a super big ladder onto the board
            :param x_val = the x value where the ladder will be loaded
            :param y_val = the y value where the ladder will be loaded
            :param angle = the angle which the ladder will be tilted
            :param scale = the scale of the image'''
    ladder = pygame.image.load('superbigladder.png')
    ladder = pygame.transform.smoothscale(ladder, (scale / 2, scale))
    ladder = pygame.transform.rotate(ladder, angle)
    screen.blit(ladder, (x_val, y_val))

