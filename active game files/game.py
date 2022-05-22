#!/usr/bin/env python
###############################################################################
#     MtekTris - an interactive led Tetris Game.                              #
#     Author: Jonah Hansen for Mtek Digital/Microtek summer 2019              #
#                                                                             #
#     This is a Tetris game programmed from scratch to play on a 62x62 LED    #
#  matrix board controlled from the website https://www.mtekdigital.ca/tetris #
#                                                                             #
#     *Edit turnOff() to incorporate relay cut off when it's ready            #
###############################################################################
import time, pygame, requests
import RPi.GPIO as GPIO
from functions import *
from neopixel import *
from socketServer import *

key = 'none'
#####################################################################       LED Info        ##################################################################

NUM_LEDS       = 1922
LED_PIN        = 18
LED_PIN2       = 13
LED_CHANNEL    = 0
LED_CHANNEL2   = 1
LED_FREQ       = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 75
STRIP_TYPE     = ws.WS2811_STRIP_GRB

leftBoard = Adafruit_NeoPixel(NUM_LEDS, LED_PIN2, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS, LED_CHANNEL2, STRIP_TYPE)
rightBoard = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS, LED_CHANNEL, STRIP_TYPE)



##################################################################         Functions       ######################################################################

#set leds to stored colours
def update():
    for i in range(len(pixel)):
        if i < 1922:
            leftBoard.setPixelColor(i, pixel[i])
        else:
            rightBoard.setPixelColor(i - 1922, pixel[i])
    leftBoard.show()
    rightBoard.show()


#communication between website and web server
def serverLoop():
    global key
    key = 'none'
    fdVsEvent = pollerObject.poll(100)

    for descriptor, Event in fdVsEvent:

        connection,address = sock.accept()

        print('Connected by', address)

        data = connection.recv(1024)
        query = data.split()[1]
        key = query.split('=')[-1]
        print(key)
        response = b"""\
HTTP/1.1 200 OK


"""
        connection.sendall(response)

#send game over request to boot the current player
def sendGameOver():
    r = requests.get('https://www.mtekdigital.ca/tetris/endgame.php')
    print(r)

relay_pin = 26
def turnOff():
    global key
    #setBlack()#these can be removed once relay is set up
    #update()
    #turn off relay goes here
    GPIO.output(relay_pin, 0)
    while key != 'Ctrl':
        serverLoop()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                key = 'Ctrl'
                break
    #turn relay back on goes here
    GPIO.output(relay_pin, 1)
    #drawFrame(grey) # this can also all be removed once relay is set up
    #drawWord('next',34,1,white)
    #drawWord('score',34,22,white)
    #drawWord('high',34,40,white)
    #drawWord('score',43,46,white)
    #from functions import score
    #drawScore(score,36,30,white)
    #drawScore(getHighscore(),36,54,white)
    #currentShape.draw()
    #nextShape.draw()
    #update()

#####################################################################      Start Game      ########################################################################
def game():

    setBlack()

    update()
    drawFrame(grey) # set up the game board

    drawWord('next',34,1,white)
    drawWord('score',34,22,white)
    drawWord('high',34,40,white)
    drawWord('score',43,46,white)
    selectShape()
    currentShape.erase()
    selectShape()
    update()

    startTime = time.time()
    currentTime = 0
    lastTime = 0
    downTime = 0
    count = 0

    #####################################################################      Main Loop       ########################################################################

    quit = False
    down = False
    start = False
    timer = False

    while not quit:
        serverLoop()

        drawFrame(grey)

        drawWord('next',34,1,white)
        drawWord('score',34,22,white)
        drawWord('high',34,40,white)
        drawWord('score',43,46,white)

        currentTime = time.time() - startTime
        from functions import score
        drawScore(score,36,30,white)
        drawScore(getHighscore(),36,54,white)

        update()
        timer = False
        while not start: #flashes 'press enter' on screen
            if not timer:
                timeout = time.time()
                timer = True
            if time.time() - timeout > 300:
                turnOff()
                GPIO.output(relay_pin, 1)
                timer = False

            serverLoop()

            time.sleep(0.7)
            startMenu()
            update()
            time.sleep(0.7)
            clearMenu()
            drawBox(25,15,3,18,grey)
            update()

            #web control
            if key == 'Enter':
                start = True
                clearGameBoard()
                saveState()
                update()
                startTime = time.time()
                currentTime = 0
                lastTime = 0
                downTime = 0
                count = 0


            #physical keyboard
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN:
                        start = True
                        clearGameBoard()
                        saveState()
                        update()
                        startTime = time.time()
                        currentTime = 0
                        lastTime = 0
                        downTime = 0
                        count = 0

        if currentTime > 180: #time up after 3 minutes
            timeUp()
            update()
            sendGameOver()
            while not quit and count < 2:
                time.sleep(0.7)
                clearMenu()
                drawBox(23,15,4,18,grey)
                update()
                time.sleep(0.7)
                gameOver()
                update()
                time.sleep(0.7)
                clearMenu()
                drawBox(23,15,4,18,grey)
                update()
                time.sleep(0.7)
                timeUp()
                update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit = True
                count += 1
            count = 0
            start = False
            selectShape()

        #website control for moving shapes
        if key == 'ArrowLeft':
            currentShape.move('left')
        if key == 'ArrowRight':
            currentShape.move('right')
        if key == 'ArrowDown':
            currentShape.move('down')
        if key == 'ArrowUp':
            currentShape.rotate()
        if key == 'Space':
            while not checkContact():
                currentShape.move('down')
            if currentShape.position[1] <= 5:
                gameOver()
                currentShape.erase()
                update()
                time.sleep(0.7)
                sendGameOver()
                while not quit and count < 3:
                    clearMenu()
                    drawBox(23,15,4,18,grey)
                    update()
                    time.sleep(0.7)
                    gameOver()
                    update()
                    time.sleep(0.7)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit = True
                    count += 1
                count = 0
                start = False
                selectShape()

            highlightLines()
            update()
            time.sleep(0.025)
            removeLines()
            update()
            selectShape()
            update()


        #physical keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            #interpret arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_LEFT:
                    currentShape.move('left')
                if event.key == pygame.K_RIGHT:
                    currentShape.move('right')
                if event.key == pygame.K_DOWN:
                    currentShape.move('down')
                    down = True
                    downTime = currentTime
                if event.key == pygame.K_UP:
                    currentShape.rotate()
                if event.key == pygame.K_SPACE:
                    while not checkContact():
                        currentShape.move('down')
                    if currentShape.position[1] <= 5:
                        gameOver()
                        currentShape.erase()
                        update()
                        time.sleep(0.7)
                        sendGameOver()
                        while not quit and count < 3:
                            clearMenu()
                            drawBox(23,15,4,18,grey)
                            update()
                            time.sleep(0.7)
                            gameOver()
                            update()
                            time.sleep(0.7)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    quit = True
                            count += 1
                        count = 0
                        start = False
                        selectShape()

                    highlightLines()
                    update()
                    time.sleep(0.025)
                    removeLines()
                    update()
                    selectShape()
                    update()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    down = False

        #hold down to slide. not used on web control
        if down and currentTime - downTime > 0.3:
            currentShape.move('down')
            update()
            time.sleep(0.03)
        #every 3/4 second
        if (currentTime - lastTime) > 0.75:
            if checkContact():
                if currentShape.position[1] <= 5:
                    gameOver()
                    currentShape.erase()
                    update()
                    time.sleep(0.7)
                    sendGameOver()
                    while not quit and count < 3:
                        clearMenu()
                        drawBox(23,15,4,18,grey)
                        update()
                        time.sleep(0.7)
                        gameOver()
                        update()
                        time.sleep(0.7)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit = True
                        count += 1
                    count = 0
                    start = False
                    selectShape()

                highlightLines()
                update()
                time.sleep(0.025)
                removeLines()
                update()
                selectShape()
                update()
            currentShape.move('down')
            lastTime = currentTime

        update()

if __name__ == '__main__':
    sock.bind((HOST,PORT))
    sock.listen(5)
    print('serving HTTP on port', PORT)

    leftBoard.begin()
    rightBoard.begin()

    pygame.init()
    screen = pygame.display.set_mode((620,620))

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, 1)
    game()
