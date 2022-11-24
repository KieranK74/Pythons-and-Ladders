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

# the modules and other interfaces used
import random
import sys
from pygame.locals import *
from ladders import *
from snakes import *
from dice import diceroll

# pygame and the font module are initiated
pygame.init()
pygame.font.init()

# this determines the frame rate of the game
clock = pygame.time.Clock()

# this creates the game window and background
pygame.display.set_caption("PYTHONS AND LADDERS DEMO")
size = [1440, 800]
bg = pygame.image.load("forest.jpeg")
bg = pygame.transform.smoothscale(bg, size)
screen = pygame.display.set_mode(size)

# initiations of the colors
black = (0, 0, 0)
pale_green = (92, 186, 78)
red = (171, 34, 24)
blue = (25, 75, 168)
COLOR1 = (255, 207, 63)
COLOR2 = (55, 110, 157)


# the font used for some of the text
font = pygame.font.SysFont('freesansbold.ttf', 100)
font2 = pygame.font.SysFont('freesansbold.ttf', 50)
font3 = pygame.font.SysFont('freesansbold.ttf', 30)
title = pygame.font.SysFont('freesansbold.ttf', 150)

# these empty dictionaries will be used to sort and store the number of moves and there locations
moves = {}
sortedmoves = {}
keys = []

# this is the starting number for the original key dictionaries
num = 100

# this is the location and scale of the first square of the game board
x_dim = 670
y_dim = 30
scale = 75

# this gets the locations and scale of each numbered square
for i in range(0, (scale * 9) + 1, scale * 2):
    k = 1
    odd = 19
    for j in range(0, (scale * 9) + 1, scale):
        moves.update({num: (x_dim + j, y_dim + i)})
        moves.update({num - odd: ((x_dim + j), (y_dim + i + scale))})
        k = k + 1
        num -= 1
        odd -= 2
    num -= 10

for key in moves.keys():
    keys.append(key)

# here are the moves sorted by key from 1-100
keys.sort()
for key in keys:
    sortedmoves.update({key: moves[key]})

# the move numbers / locations of the snake heads and the ladder bottoms
snakeheads = {33: (1195, 480),
              35: (1045, 480),
              41: (670, 405),
              85: (970, 105),
              93: (1195, 30)}

ladderbottoms = {3: (820, 705),
                 27: (1120, 555),
                 44: (895, 405),
                 51: (1345, 330)}


def checksnake(movenum):
    '''checks if the player landed on a snake head and has to go to the tail
    :param movenum = move number that is checked for a snake head
    :returns movenum '''
    if movenum in snakeheads.keys():
        if movenum == 33:
            return 7
        elif movenum == 35:
            return 16
        elif movenum == 41:
            return 17
        elif movenum == 85:
            return 39
        elif movenum == 93:
            return 69
    else:
        return movenum


def checkladder(movenum):
    '''checks if the player landed on a ladder bottom and can climb to the top
        :param movenum = move number that is checked for a ladder bottom
        :returns movenum '''
    if movenum in ladderbottoms.keys():
        if movenum == 3:
            return 22
        elif movenum == 27:
            return 54
        elif movenum == 44:
            return 88
        elif movenum == 51:
            return 68
    else:
        return movenum


def rightmove(move):
    '''this automatically checks if the player moves forward, up a ladder, or down a snake
    :param move = move number checked that is '''
    checkladder(move)
    checksnake(move)
    if checksnake(move) < move:
        return checksnake(move)
    elif checkladder(move) > move:
        return checkladder(move)
    else:
        return move


def squareone(x_val, y_val, side_num):
    '''This makes a yellow square for the board
    :param x_val = the x value where the square will be placed
    :param y_val = the y value where the square will be placed
    :param side_num = the side length of the square'''
    squareOne = pygame.Rect(x_val, y_val, side_num, side_num)
    pygame.draw.rect(screen, COLOR1, squareOne)


def squaretwo(x_val2, y_val2, side_num2):
    '''This makes a blue square for the board
    :param x_val2 = the x value where the square will be placed
    :param y_val2 = the y value where the square will be placed
    :param side_num2 = the side length of the square'''
    squareTwo = pygame.Rect(x_val2, y_val2, side_num2, side_num2)
    pygame.draw.rect(screen, COLOR2, squareTwo)


def draw_text(text, fonty, color, surface, x, y):
    '''renders text and a font
    :param text = the text that will be rendered to the screen
    :param fonty =  the font that the text will be in
    :param color = the color the text will be in
    :param surface = the surface that the text will be written in
    :param x = the x value of the text box
    :param y = the y value of the text box'''
    tex_obj = fonty.render(text, 1, color)
    textrect = tex_obj.get_rect()
    textrect.topleft = x, y
    surface.blit(tex_obj, textrect)


def text_objects(text, font_kind):
    '''renders text and a font
    :param text = the text that will be rendered to the screen
    :param font_kind =  the font that the text will be in'''
    textSurface = font_kind.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def message_display(text, x_val, y_val):
    '''this loads the image of the trophy and places it
        :param text = the text that will be displayed
        :param x_val = the x value where the trophy will be placed
        :param y_val = the y value where the trophy will be placed'''
    largeText = pygame.font.Font('freesansbold.ttf', 15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.topright = (x_val, y_val)
    screen.blit(TextSurf, TextRect)


def button(msg, x, y, w, h, ic, ac, action=None):
    '''This creates a button that does a task like running the game
    :param msg = the message that is displayed on the button
    :param x = the x value for the button
    :param y = the y value for the button
    :param w = the width of the button
    :param h = the height of the body
    :param ic = the passive color of the button
    :param ac = the active color of the button
    :param action = the action that determines what the function of the button is'''
    mouse = pygame.mouse.get_pos()
    clickit = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        # if the button is clicked and there is an action associated with the button
        if clickit[0] == True and action is not None:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "gamewith2":
                gamewithtwo()
            elif action == "game":
                game()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def placetrophy(x_val, y_val, trophy_scale):
    '''this loads the image of the trophy and places it
    :param x_val = the x value where the trophy will be placed
    :param y_val = the y value where the trophy will be placed
    :param trophy_scale = the scale of the image based on number of pixels'''

    trophy = pygame.image.load('trophy-png-23.png')
    trophy = pygame.transform.smoothscale(trophy, (trophy_scale, trophy_scale))
    screen.blit(trophy, (x_val, y_val))


def winnersnake(x_val, y_val):
    '''this loads the image of the winner snake and places it
        :param x_val = the x value where the winner snake will be placed
        :param y_val = the y value where the winner snake will be placed'''
    winsnake = pygame.image.load("winnersnake.png")
    winsnake = pygame.transform.smoothscale(winsnake, (400, 400))
    screen.blit(winsnake, (x_val, y_val))


def snakepal(x_val, y_val):
    snakefriend = pygame.image.load("snakefriend.png")
    snakefriend = pygame.transform.smoothscale(snakefriend, (550, 450))
    screen.blit(snakefriend, (x_val, y_val))


def makegrid():
    '''this draws a 10*10 game board and uses functions from the snake and ladder pyfiles to add snakes and ladders'''
    x_grid = 670
    y_grid = 30
    grid_scale = 75

    num = 100
    for i in range(0, (grid_scale * 9) + 1, grid_scale * 2):
        k = 1
        odd = 19
        for j in range(0, (grid_scale * 9) + 1, grid_scale):
            if k % 2 == 1:
                squareone(x_grid + j, y_grid + i, grid_scale)
                squaretwo((x_grid + j), (y_grid + i + grid_scale), grid_scale)
                message_display(str(num), (x_grid + j + grid_scale - 5), y_grid + i + 5)
                message_display(str(num - odd), (x_grid + j + grid_scale - 5), y_grid + i + grid_scale + 5)

            elif k % 2 == 0:
                squaretwo((x_grid + j), (y_grid + i), grid_scale)
                squareone((x_grid + j), (y_grid + i + grid_scale), grid_scale)
                message_display(str(num), (x_grid + j + grid_scale - 5), y_grid + i + 5)
                message_display(str(num - odd), (x_grid + j + grid_scale - 5), y_grid + i + grid_scale + 5)

            moves.update({num: (x_grid + j, y_grid + i)})
            moves.update({num - odd: ((x_grid + j), (y_grid + i + grid_scale))})
            k = k + 1
            num -= 1
            odd -= 2
        num -= 10

    placetrophy(x_grid, y_grid, grid_scale)

    createsnake1(750, 100, 0, 300)
    createsnake2(1150, 485, 0, 260, False)
    createsnake3(680, 370, 10, 210)
    createsnake4(1220, 40, 0, 170)

    createladder(715, 550, 25, 200)
    createbigladder(1095, 375, 0, 250)

    createsnake5(900, 460, 20, 150, True)

    createladder(1210, 240, 65, 175)
    createsuperbigladder(845, 65, 315, 440)


def drawplayer1(x_val, y_val):
    '''This makes a red player for the board
        :param x_val = the x value where the player will be placed
        :param y_val = the y value where the player will be placed'''
    player = pygame.image.load("player1.png")
    player = pygame.transform.smoothscale(player, (75, 75))
    screen.blit(player, (x_val, y_val))


def drawplayer2(x_val, y_val):
    '''This makes a blue player for the board
        :param x_val = the x value where the player will be placed
        :param y_val = the y value where the player will be placed'''
    player = pygame.image.load("player2.png")
    player = pygame.transform.smoothscale(player, (75, 75))
    screen.blit(player, (x_val, y_val))


def winnerwinner(player):
    '''this displays a winning screen based on who won the game
    :param player = determines which screen will be displayed when a player wins'''
    if player == 1:
        screen.blit(bg, (0, 0))
        pygame.transform.smoothscale(bg, size)
        draw_text("PLAYER ONE WINS!!!", font, COLOR1, screen, 350, 200)
        draw_text("press backspace or the close button to exit", font2, black, screen, 352, 285)
        winnersnake(520, 300)
    elif player == 2:
        screen.blit(bg, (0, 0))
        pygame.transform.smoothscale(bg, size)
        draw_text("PLAYER TWO WINS!!!", font, COLOR1, screen, 350, 200)
        draw_text("Press backspace or the close button to exit", font2, black, screen, 352, 285)
        winnersnake(520, 300)


def chickendinner(move1, move2):
    '''This checks whether a player has won the game or not
    :param move1 = move number of the first player
    :param move2 = move number of the second player
    :returns True if either move1 or move2 is greater than or equal to 100
    :returns False if neither player move is greater than or equal to 100'''
    if move1 >= 100:
        winnerwinner(1)
        return True
    elif move2 >= 100:
        winnerwinner(2)
        return True
    else:
        return False


def mainmenu():
    """This displays the main menu to play the games or exit"""
    while True:
        # The main menu is displayed with the title and credits
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, COLOR1, [290, 215, 800, 100])
        draw_text("PYTHONS & LADDERS", font, COLOR2, screen, 305, 230)
        pygame.draw.rect(screen, pale_green, [20, 750, 650, 30])
        draw_text("By Kieran Kahler, Zachary Martin, Jinghan Xue, & Ashlyn Nobles", font3, black, screen, 20, 755)

        pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # the three buttons go to different functions
        # the first one is the 1 v 1 game with another player
        # the second one is a game against the computer
        # the third one is the quit button
        button("1 vs 1", 420, 500, 200, 50, COLOR1, COLOR2, "gamewith2")
        button("1 vs Comp", 740, 500, 200, 50, COLOR1, COLOR2, "game")
        button("QUIT", 590, 600, 200, 50, COLOR1, COLOR2, "quit")

        pygame.display.update()
        clock.tick(60)


def game():
    '''This is the game function that runs and allows the player to play snakes and ladders'''

    # The game just displays a game board at first
    running = True
    move1 = 1
    move2 = 1
    turncount = 0
    screen.blit(bg, (0, 0))
    makegrid()
    gamewindow = pygame.Rect(50, 50, 550, 250)
    pygame.draw.rect(screen, COLOR2, gamewindow)
    draw_text("PLAYER 1 MOVE: ", font2, COLOR1, screen, 70, 75)
    draw_text("PLAYER 2 MOVE: ", font2, COLOR1, screen, 70, 150)
    draw_text("TURNS: ", font2, COLOR1, screen, 70, 225)
    snakepal(50, 325)
    pygame.draw.rect(screen, pale_green, [20, 750, 350, 30])
    draw_text("Press SPACE to ROLL", font3, black, screen, 20, 755)
    pygame.display.flip()
    while running:
        screen.blit(bg, (0, 0))
        makegrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked the red X button
                running = False  # This exits the loop
            if event.type == KEYDOWN:  # If the user presses a key
                if event.key == K_ESCAPE:
                    pygame.quit()  # the escape key exits the game
                    sys.exit()
                if event.key == K_BACKSPACE:  # the backspace key goes to the main menu
                    mainmenu()
                    running = False
                if event.key == K_SPACE:  # the space game rolls the dice and starts the game
                    pygame.draw.rect(screen, COLOR2, gamewindow)
                    draw_text("PLAYER 1 MOVE: ", font2, COLOR1, screen, 70, 75)
                    draw_text("PLAYER 2 MOVE: ", font2, COLOR1, screen, 70, 150)
                    snakepal(50, 325)

                    roll = random.randint(1, 6)
                    diceroll(430, 55, 75, roll)
                    move1 += roll
                    move1 = rightmove(move1)
                    draw_text(str(move1), font2, COLOR1, screen, 375, 75)

                    roll = random.randint(1, 6)
                    diceroll(430, 130, 75, roll)
                    move2 += roll
                    move2 = rightmove(move2)
                    draw_text(str(move2), font2, COLOR1, screen, 375, 150)

                    turncount += 1
                    draw_text("TURNS: ", font2, COLOR1, screen, 70, 225)
                    draw_text(str(turncount), font2, COLOR1, screen, 375, 225)
                    pygame.draw.rect(screen, pale_green, [20, 750, 350, 30])
                    draw_text("Press SPACE to ROLL", font3, black, screen, 20, 755)
                    # While there is no winner, the pieces are moved to their respective squares
                    # The pieces shift when they are on the same square so they are not covering each other
                    if not chickendinner(move1, move2):
                        if move1 == move2:
                            drawplayer1(sortedmoves.get(move1)[0] + 20, sortedmoves.get(move1)[1] + 10)
                            drawplayer2(sortedmoves.get(move2)[0], sortedmoves.get(move2)[1])
                        else:
                            drawplayer1(sortedmoves.get(move1)[0], sortedmoves.get(move1)[1])
                            drawplayer2(sortedmoves.get(move2)[0], sortedmoves.get(move2)[1])

                    # The game updates each time the SPACE button is pressed

                    pygame.display.update()
                    clock.tick(60)


def gamewithtwo():
    '''This is the game function that runs and allows 2 players to play snakes and ladders'''

    # The game just displays a game board at first
    running = True

    # the players start at position 1
    move1 = 1
    move2 = 1

    # this counts how many turns have passed
    turncount = 0

    # if playerturn is 1, that means that it is player 1's turn
    # else, it is player 2's turn
    playerturn = 1

    # the screen is initialized to display the board and a game window
    screen.blit(bg, (0, 0))
    makegrid()
    gamewindow = pygame.Rect(50, 50, 550, 250)
    pygame.draw.rect(screen, COLOR2, gamewindow)
    draw_text("PLAYER 1 MOVE: ", font3, COLOR1, screen, 70, 75)
    draw_text("PLAYER 2 MOVE: ", font3, COLOR1, screen, 70, 125)
    draw_text("TURNS: ", font3, COLOR1, screen, 70, 175)
    draw_text("PLAYER TURN: ", font3, COLOR1, screen, 70, 225)
    snakepal(50, 325)
    pygame.draw.rect(screen, pale_green, [20, 750, 350, 30])
    draw_text("Press SPACE to ROLL", font3, black, screen, 20, 755)
    pygame.display.flip()
    while running:
        screen.blit(bg, (0, 0))
        makegrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked the red X button
                running = False  # This exits the loop
            if event.type == KEYDOWN:  # If the user presses a key
                if event.key == K_ESCAPE:
                    pygame.quit()  # the escape key exits the game
                    sys.exit()
                if event.key == K_BACKSPACE:  # the backspace key goes to the main menu
                    mainmenu()
                    running = False
                if event.key == K_SPACE:  # the space game rolls the dice and starts the game
                    # The game updates each time the SPACE button is pressed
                    pygame.draw.rect(screen, COLOR2, gamewindow)
                    draw_text("PLAYER 1 MOVE: ", font3, COLOR1, screen, 70, 75)
                    draw_text("PLAYER 2 MOVE: ", font3, COLOR1, screen, 70, 125)
                    snakepal(50, 325)

                    # the turns go back and forth between the players and changes every roll
                    if playerturn == 1:
                        roll = random.randint(1, 6)
                        diceroll(400, 645, 125, roll)
                        move1 += roll
                        move1 = rightmove(move1)
                        playerturn = 2

                    elif playerturn == 2:
                        roll = random.randint(1, 6)
                        diceroll(400, 645, 125, roll)
                        move2 += roll
                        move2 = rightmove(move2)
                        playerturn = 1

                    draw_text(str(move1), font3, COLOR1, screen, 375, 75)
                    draw_text(str(move2), font3, COLOR1, screen, 375, 125)

                    turncount += 1
                    draw_text("TURNS: ", font3, COLOR1, screen, 70, 175)
                    draw_text(str(turncount//2), font3, COLOR1, screen, 375, 175)
                    draw_text("PLAYER TURN: ", font3, COLOR1, screen, 70, 225)
                    draw_text(str(playerturn), font3, COLOR1, screen, 375, 225)
                    pygame.draw.rect(screen, pale_green, [20, 750, 350, 30])
                    draw_text("Press SPACE to ROLL", font3, black, screen, 20, 755)
                    # While there is no winner, the pieces are moved to their respective squares
                    # The pieces shift when they are on the same square so they are not covering each other
                    if not chickendinner(move1, move2):
                        if move1 == move2:
                            drawplayer1(sortedmoves.get(move1)[0] + 20, sortedmoves.get(move1)[1] + 10)
                            drawplayer2(sortedmoves.get(move2)[0], sortedmoves.get(move2)[1])
                        else:
                            drawplayer1(sortedmoves.get(move1)[0], sortedmoves.get(move1)[1])
                            drawplayer2(sortedmoves.get(move2)[0], sortedmoves.get(move2)[1])

                    # The game updates each time the space bar is placed
                    pygame.display.update()
                    clock.tick(60)


# This is where the game starts
mainmenu()
