import time, pygame
from functions import *
from game import *
from logo import *
from david import *
from greg import *
from kurtis import *
from davina import *
from alex import *
from andrew import *
from neopixel import *
from PIL import Image

#####################################################################       LED Info        ##################################################################

NUM_LEDS       = 1922
LED_PIN        = 18
LED_PIN2       = 13
LED_CHANNEL    = 0
LED_CHANNEL2   = 1
LED_FREQ       = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 255
STRIP_TYPE     = ws.WS2811_STRIP_GRB

leftBoard = Adafruit_NeoPixel(NUM_LEDS, LED_PIN2, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS, LED_CHANNEL2, STRIP_TYPE)
rightBoard = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS, LED_CHANNEL, STRIP_TYPE)

leftBoard.begin()
rightBoard.begin()

quit = False

##################################################################         Functions       ######################################################################

def update():
    for i in range(len(pixel)):
        if i < 1922:
            leftBoard.setPixelColor(i, pixel[i])
        else:
            rightBoard.setPixelColor(i - 1922, pixel[i])
    leftBoard.show()
    rightBoard.show()


pygame.init()
screen = pygame.display.set_mode((620,620))

boxLength = 0
boxHeight = 14
option1 = 'game()'
option2 = 'logo()'
option3 = 'david()'
option4 = 'greg()'
option5 = 'kurtis()'
option6 = 'davina()'
option7 = 'alex()'
option8 = 'andrew()'

def mainMenu():
    boxPosition = [1,0]
    line = 1
    page = 0

    def findBoxLength():
        for i in range(5,62):
            if pixel[xy(i,boxPosition[1] + 5)] == black and pixel[xy(i+1,boxPosition[1] + 5)] == black \
             and pixel[xy(i+2,boxPosition[1] + 5)] == black and pixel[xy(i+3,boxPosition[1] + 5)] == black \
             and pixel[xy(i+4,boxPosition[1] + 5)] == black:
                return i +1
        return i -5

    ######################################################################       start       ############################################################################

    im = Image.open('mainMenu.jpg')
    pix = im.load()
    while True:
        for i in range(62):
            for j in range(62):
                pixel[xy(i,j)] = Color(pix[i,j + (62*page)][0],pix[i,j + (62*page)][1],pix[i,j + (62*page)][2])

        drawBox(findBoxLength(),boxHeight,boxPosition[0],boxPosition[1],white)
        update()
        drawBox(findBoxLength() -2,boxHeight,boxPosition[0],boxPosition[1],black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_DOWN and line != 8:
                    if line == 4:
                        page +=1
                        boxPosition = [1,-15]
                    line += 1
                    boxPosition[1] += 15
                if event.key == pygame.K_UP and line != 1:
                    if line == 5:
                        page += -1
                        boxPosition[1] += 60
                    line += -1
                    boxPosition[1] += -15
                if event.key == pygame.K_RETURN:
                    if line == 1:
                        game()
                    elif line == 2:
                        logo()
                    elif line == 3:
                        david()
                    elif line == 4:
                        greg()
                    elif line == 5:
                        kurtis()
                    elif line == 6:
                        davina()
                    elif line == 7:
                        alex()
                    elif line == 8:
                        andrew()
                    end = False
                    while not end:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    end = True
                                    return

if __name__ == "__main__":

    while True:
        mainMenu()
