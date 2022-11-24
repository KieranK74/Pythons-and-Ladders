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


def createsnake1(x_val, y_val, angle, scale, flip=False):
    '''loads a snake onto the board
    :param x_val = the x value where the snake will be loaded
    :param y_val = the y value where the snake will be loaded
    :param angle = the angle where the snake will be tilted
    :param scale = the scale of the image
    :param flip = will determine if the images'''
    snake = pygame.image.load("snake1.png")
    snake = pygame.transform.smoothscale(snake, (scale, scale*1.5))
    snake = pygame.transform.rotate(snake, angle)
    snake = pygame.transform.flip(snake, flip, False)
    screen.blit(snake, (x_val, y_val))


def createsnake2(x_val, y_val, angle, scale, flip=False):
    '''loads a snake onto the board
        :param x_val = the x value where the snake will be loaded
        :param y_val = the y value where the snake will be loaded
        :param angle = the angle where the snake will be tilted
        :param scale = the scale of the image
        :param flip = will determine if the images'''
    snake = pygame.image.load("snake2.png")
    snake = pygame.transform.smoothscale(snake, (scale, scale))
    snake = pygame.transform.rotate(snake, angle)
    snake = pygame.transform.flip(snake, flip, False)
    screen.blit(snake, (x_val, y_val))


def createsnake3(x_val, y_val, angle, scale, flip=False):
    '''loads a snake onto the board
        :param x_val = the x value where the snake will be loaded
        :param y_val = the y value where the snake will be loaded
        :param angle = the angle where the snake will be tilted
        :param scale = the scale of the image
        :param flip = will determine if the images'''
    snake = pygame.image.load("snake3.png")
    snake = pygame.transform.smoothscale(snake, (scale, scale*1.5))
    snake = pygame.transform.rotate(snake, angle)
    snake = pygame.transform.flip(snake, flip, False)
    screen.blit(snake, (x_val, y_val))


def createsnake4(x_val, y_val, angle, scale, flip=False):
    '''loads a snake onto the board
        :param x_val = the x value where the snake will be loaded
        :param y_val= the y value where the snake will be loaded
        :param angle = the angle where the snake will be tilted
        :param scale = the scale of the image
        :param flip = will determine if the images'''
    snake = pygame.image.load("snake4.png")
    snake = pygame.transform.smoothscale(snake, (scale, scale*1.5))
    snake = pygame.transform.rotate(snake, angle)
    snake = pygame.transform.flip(snake, flip, False)
    screen.blit(snake, (x_val, y_val))


def createsnake5(x_val, y_val, angle, scale, flip=False):
    '''loads a snake onto the board
        :param x_val = the x value where the snake will be loaded
        :param y_val = the y value where the snake will be loaded
        :param angle = the angle where the snake will be tilted
        :param scale = the scale of the image
        :param flip = will determine if the images'''
    snake = pygame.image.load("snake5.png")
    snake = pygame.transform.smoothscale(snake, (scale, scale*1.5))
    snake = pygame.transform.rotate(snake, angle)
    snake = pygame.transform.flip(snake, flip, False)
    screen.blit(snake, (x_val, y_val))


