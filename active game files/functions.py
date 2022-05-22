
from neopixel import * #module that facilitates the use of leds

#size of matrix [x,y]
size = [62,62]
#RGB colours to use
red = Color(233,39,68)
green = Color(129,235,65)
blue = Color(65,99,235)
yellow = Color(231,240,55)
orange = Color(247, 166, 45)
grey = Color(211,211,211)
purple = Color(142,74,217)
lightblue =Color(96,216,230)
white = Color(255,255,255)
black = Color(0,0,0)

############################################################       array stuff         ##########################################################################

#initialize main array that stores colour data for each led
pixel = [black] * size[0] * size[1]
#use savestate to be able to check what pixel was last iteration
savestate = [black] * size[0] * size[1]

#function that converts input x and y into the actual array number i
def xy(x,y):
    if x % 2 != 0:
        i = x * size[1] + y
    else:
        i = x * size[1] + size[1] - y - 1
    return i

#functions that convert input i from the array to (x,y) list
def array(i):
    x = int(i/size[1])
    if x % 2 != 0:
        y = i - (x * size[1])
    else:
        y = x * size[1] + size[1] - i - 1
    return [x,y]

#converts from array to just x value
def arrayX(i):
    x = int(i/size[1])
    return x

#converts array to just y value
def arrayY(i):
    if arrayX(i) % 2 != 0:
        y = i - (arrayX(i) * size[1])
    else:
        y = arrayX(i) * size[1] + size[1] - i - 1
    return y

############################################################       draw fundamentals         ##########################################################################

#draws a hollow box of given dimensions and colour at the given position
def drawBox(width, height, x,y, colour):
    global pixel
    for i in range(width):
        pixel[xy(x + i, y)] = colour
        pixel[xy(x + i, y + height - 1)] = colour
    for i in range(height):
        pixel[xy(x, y + i)] = colour
        pixel[xy(x + width -1, y + i)] = colour

#draw a 3x3 solid block. used to create shapes.
def drawBlock(x,y,colour):
    global pixel
    for i in range(3):
        for j in range(3):
            pixel[xy(x-1 + i, y-1 + j)] = colour

#draw a letter - to be used with drawWord()
def drawLetter(letter, x,y, colour):
    global pixel
    if letter == 'n':
        for i in range(5):
            pixel[xy(x, i + y)] = colour
            pixel[xy(x + 4, y + i)] = colour
        for i in range(1,4):
            pixel[xy(x + i, y + i)] = colour

    elif letter == 'e':
        for i in range(5):
            pixel[xy(x, i + y)] = colour
        for i in range(3):
            pixel[xy(x + i, y)] = colour
            pixel[xy(x + i, y + 4)] = colour
        pixel[xy(x+1,y+2)] = colour

    elif letter == 'x':
        for i in range(5):
            pixel[xy(x+i, y+i)] = colour
            pixel[xy(x+i,y+4-i)] = colour

    elif letter == 't':
        for i in range(3):
            pixel[xy(x+i,y)] = colour
        for i in range(5):
            pixel[xy(x+1,y+i)] = colour

    elif letter == 's':
        for i in range(2):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+i,y+4)] = colour
        for i in range(3):
            pixel[xy(x,y+i)] = colour
            pixel[xy(x+1,y+i+2)] = colour

    elif letter == 'c':
        for i in range(5):
            pixel[xy(x, i + y)] = colour
        for i in range(2):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+4)] = colour
    elif letter == 'o':
        for i in range(3):
            pixel[xy(x,y+i+1)] = colour
            pixel[xy(x+2,y+i+1)] = colour
        pixel[xy(x+1,y)] = colour
        pixel[xy(x+1,y+4)] = colour

    elif letter == 'r':
        for i in range(3):
            for j in range(5):
                pixel[xy(x+i,y+j)] = colour
        pixel[xy(x+1,y+1)] = black
        pixel[xy(x+1,y+4)] = black
        pixel[xy(x+2,y+3)] = black

    elif letter == 'h':
        for i in range(5):
            pixel[xy(x, i + y)] = colour
            pixel[xy(x+2, i + y)] = colour
        pixel[xy(x+1,y+2)] = colour

    elif letter == 'i':
        for i in range(5):
            pixel[xy(x, i + y)] = colour

    elif letter == 'g':
        for i in range(3):
            for j in range(5):
                pixel[xy(x+i,y+j)] = colour
        pixel[xy(x+1,y+1)] = black
        pixel[xy(x+1,y+2)] = black
        pixel[xy(x+1,y+3)] = black
        pixel[xy(x+2,y+1)] = black

    elif letter == 'a':
        for i in range(4):
            pixel[xy(x, i + y +1)] = colour
            pixel[xy(x+2, i + y +1)] = colour
        pixel[xy(x+1,y+2)] = colour
        pixel[xy(x+1,y)] = colour

    elif letter == 'm':
        for i in range(4):
            pixel[xy(x,y+i+1)] = colour
            pixel[xy(x+4,y+1+i)] = colour
        pixel[xy(x+1,y)] = colour
        pixel[xy(x+3,y)] = colour
        pixel[xy(x+2,y+1)] = colour
        pixel[xy(x+2,y+2)] = colour

    elif letter == 'v':
        for i in range(3):
            pixel[xy(x,y+i)] = colour
            pixel[xy(x+4,y+i)] = colour
        pixel[xy(x+1,y+3)] = colour
        pixel[xy(x+2,y+4)] = colour
        pixel[xy(x+3,y+3)] = colour

    elif letter == 'u':
        for i in range(5):
            pixel[xy(x,y+i)] = colour
            pixel[xy(x+2,y+i)] = colour
        pixel[xy(x+1,y+4)] = colour

    elif letter == 'p':
        for i in range(5):
            pixel[xy(x,y+i)] = colour
        for i in range(3):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+2,y+i)] = colour

#draws a number at the given position in the given colour. used with draw score
def drawNumber(number, x,y, colour):
    global pixel
    for i in range(3):
        for j in range(5):
            pixel[xy(x+i,y+j)] = black
    if number == 0:
        for i in range(3):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+4)] = colour
        for i in range(5):
            pixel[xy(x,y+i)] = colour
            pixel[xy(x+2,y+i)] = colour

    elif number == 1:
        for i in range(5):
            pixel[xy(x+1,y+i)] = colour
        for i in range(3):
            pixel[xy(x+i,y+4)] = colour
        pixel[xy(x,y+1)] = colour

    elif number == 2:
        for i in range(3):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+i,y+4)] = colour
            pixel[xy(x+2,y+i)] = colour
            pixel[xy(x,y+i+2)] = colour

    elif number == 3:
        for i in range(3):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+i,y+4)] = colour
        for i in range(5):
            pixel[xy(x+2,y+i)] = colour

    elif number == 4:
        for i in range(3):
            pixel[xy(x,y+i)] = colour
            pixel[xy(x+i,y+2)] = colour
        for i in range(5):
            pixel[xy(x+2,y+i)] = colour

    elif number == 5:
        for i in range(3):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+i,y+4)] = colour
            pixel[xy(x+2,y+i+2)] = colour
            pixel[xy(x,y+i)] = colour

    elif number == 6:
        for i in range(3):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+i,y+4)] = colour
        for i in range(5):
            pixel[xy(x+2,y+i)] = colour
            pixel[xy(x,y+i)] = colour
        pixel[xy(x+2,y+1)] = black

    elif number == 7:
        for i in range(3):
            pixel[xy(x+i,y)] = colour
        for i in range(5):
            pixel[xy(x+2,y+i)] = colour

    elif number == 8:
        for i in range(3):
            pixel[xy(x+i,y)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+i,y+4)] = colour
        for i in range(5):
            pixel[xy(x+2,y+i)] = colour
            pixel[xy(x,y+i)] = colour

    elif number == 9:
        for i in range(3):
            pixel[xy(x,y+i)] = colour
            pixel[xy(x+i,y+2)] = colour
            pixel[xy(x+i,y)] = colour
        for i in range(5):
            pixel[xy(x+2,y+i)] = colour

############################################################       draw specifics        ##########################################################################

#draw the frame
def drawFrame(colour):
    #draw main window
    drawBox(32,62,0,0,colour)
    #draw next shape box
    drawBox(18,12,34,7,colour)
    #draw score boxes
    drawBox(27,9,34,28,colour)
    drawBox(27,9,34,52,colour)

#input a phrase with top left starting coordinates and colour
def drawWord(word, x,y, colour):
    string = list(word)
    size = []
    for i in range(len(string)):
        if string[i] == 'i':
            size.extend([2])
        elif string[i] == 's' or string[i] == 'c':
            size.extend([3])
        elif string[i] == 'n' or string[i] == 'x' or string[i] == 'm' or string[i] == 'v':
            size.extend([6])
        else:
            size.extend([4])
        drawLetter(string[i],x + sum(size) - size[i] ,y, colour)

#draw a series of numbers at a given position
def drawScore(givenScore, x,y, colour):
    for i in range(len(givenScore)):
        drawNumber(givenScore[i],x + 4*i ,y, colour)

############################################################       score keeping stuff        ##########################################################################

#arrays to store score and highscore -1 is an empty placeholder
score = [-1,-1,-1,-1,-1,0]
timeLeft = [6,0] #not used

#read the highscore from file and set new highscore
def getHighscore():
    file = open('highscore.txt', 'r+')
    highscore = []
    for i in file.read().split():
        highscore.append(int(i))
    file.close()
    for i in range(len(score)):
        if score[i] > highscore[i]:
            highscore = score
            file = open('highscore.txt', 'w+')
            file.truncate(0)
            for i in range(len(highscore)):
                file.write('%d '%highscore[i])
            file.close()
        elif score[i] < highscore[i]:
            break
    return highscore

#add a given value to the given score
def addScore(givenScore,amount):
    givenScore.reverse()
    givenScore[0] += amount
    for i in range(len(givenScore)):
        if givenScore[i] >= 10:
            if givenScore[i+1] == -1:
                givenScore[i+1] = 0
            while givenScore[i] >= 10:
                givenScore[i] += -10
                givenScore[i+1] += 1
        else:
            break
    givenScore.reverse()

############################################################        edge detection      #######################################################################

#saves the current pixel array so that it can be compared.
def saveState():
    global savestate
    for i in range(36):
        for j in range(62):
            savestate[xy(i,j)] = pixel[xy(i,j)]

#returns true if the current shape is in contact with a block below it.
def checkContact():
    for i in range(1,30):
        for j in reversed(range(1,60)):
            if savestate[xy(i,j)] == black and pixel[xy(i,j)] != black:
                if pixel[xy(i,j+1)] != black:
                    return True
                break
    return False

#input which side to check and return true if the current shape is in contact with something on that side
def checkEdge(side):
    if side == 'right':
        for j in range(1,61):
            for i in reversed(range(1,30)):
                if savestate[xy(i,j)] == black and pixel[xy(i,j)] != black:
                    if pixel[xy(i+1,j)] != black:
                        return True
                    break
        return False

    elif side == 'left':
        for j in range(1,61):
            for i in range(1,30):
                if savestate[xy(i,j)] == black and pixel[xy(i,j)] != black:
                    if pixel[xy(i-1,j)] != black:
                        return True
                    break
        return False

############################################################       shape stuff        ##########################################################################

#define shape class with properties shape, position and rotation
class shape:
    def __init__(self, shape, position, rotation):
        self.shape = shape
        self.position = position
        self.rotation = rotation

    #draws the shape at its position and rotation
    def draw(self):
        if self.shape == 'L':
            drawBlock(self.position[0],self.position[1],orange)
            if self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,orange)
                drawBlock(self.position[0],self.position[1] - 3,orange)
                drawBlock(self.position[0] + 3,self.position[1] + 3,orange)
            elif self.rotation == 1:
                drawBlock(self.position[0]+3,self.position[1],orange)
                drawBlock(self.position[0]-3,self.position[1],orange)
                drawBlock(self.position[0] - 3,self.position[1] + 3,orange)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] + 3,orange)
                drawBlock(self.position[0],self.position[1] - 3,orange)
                drawBlock(self.position[0] - 3,self.position[1] - 3,orange)
            elif self.rotation == 3:
                drawBlock(self.position[0]+3,self.position[1],orange)
                drawBlock(self.position[0]-3,self.position[1],orange)
                drawBlock(self.position[0] + 3,self.position[1] - 3,orange)

        elif self.shape == 'J':
            drawBlock(self.position[0],self.position[1],blue)
            if self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,blue)
                drawBlock(self.position[0],self.position[1] - 3,blue)
                drawBlock(self.position[0] - 3,self.position[1] + 3,blue)
            elif self.rotation == 1:
                drawBlock(self.position[0] + 3,self.position[1],blue)
                drawBlock(self.position[0] - 3,self.position[1],blue)
                drawBlock(self.position[0] - 3,self.position[1] - 3,blue)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] + 3,blue)
                drawBlock(self.position[0],self.position[1] - 3,blue)
                drawBlock(self.position[0] + 3,self.position[1] - 3,blue)
            elif self.rotation == 3:
                drawBlock(self.position[0] + 3,self.position[1],blue)
                drawBlock(self.position[0] - 3,self.position[1],blue)
                drawBlock(self.position[0] + 3,self.position[1] + 3,blue)

        elif self.shape == 'S':
            drawBlock(self.position[0],self.position[1],green)
            if self.rotation == 1:
                drawBlock(self.position[0],self.position[1] + 3,green)
                drawBlock(self.position[0] + 3,self.position[1],green)
                drawBlock(self.position[0] - 3,self.position[1] + 3,green)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] + 3,green)
                drawBlock(self.position[0] - 3,self.position[1],green)
                drawBlock(self.position[0] - 3,self.position[1] - 3,green)
            elif self.rotation == 3:
                drawBlock(self.position[0],self.position[1] - 3,green)
                drawBlock(self.position[0] - 3,self.position[1],green)
                drawBlock(self.position[0] + 3,self.position[1] - 3,green)
            elif self.rotation == 4:
                drawBlock(self.position[0],self.position[1] - 3,green)
                drawBlock(self.position[0] + 3,self.position[1],green)
                drawBlock(self.position[0] + 3,self.position[1] + 3,green)

        elif self.shape == 'Z':
            drawBlock(self.position[0],self.position[1],red)
            if self.rotation == 1:
                drawBlock(self.position[0],self.position[1] + 3,red)
                drawBlock(self.position[0] - 3,self.position[1],red)
                drawBlock(self.position[0] + 3,self.position[1] + 3,red)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] - 3,red)
                drawBlock(self.position[0] - 3,self.position[1],red)
                drawBlock(self.position[0] - 3,self.position[1] + 3,red)
            elif self.rotation == 3:
                drawBlock(self.position[0],self.position[1] - 3,red)
                drawBlock(self.position[0] + 3,self.position[1],red)
                drawBlock(self.position[0] - 3,self.position[1] - 3,red)
            elif self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,red)
                drawBlock(self.position[0] + 3,self.position[1],red)
                drawBlock(self.position[0] + 3,self.position[1] - 3,red)

        elif self.shape == 'T':
            drawBlock(self.position[0],self.position[1],purple)
            if self.rotation == 1:
                drawBlock(self.position[0] + 3,self.position[1],purple)
                drawBlock(self.position[0] - 3,self.position[1],purple)
                drawBlock(self.position[0],self.position[1] - 3,purple)
            elif self.rotation == 2:
                drawBlock(self.position[0] + 3,self.position[1],purple)
                drawBlock(self.position[0],self.position[1] + 3,purple)
                drawBlock(self.position[0],self.position[1] - 3,purple)
            elif self.rotation == 3:
                drawBlock(self.position[0] + 3,self.position[1],purple)
                drawBlock(self.position[0] - 3,self.position[1],purple)
                drawBlock(self.position[0],self.position[1] + 3,purple)
            elif self.rotation == 4:
                drawBlock(self.position[0] - 3,self.position[1],purple)
                drawBlock(self.position[0],self.position[1] + 3,purple)
                drawBlock(self.position[0],self.position[1] - 3,purple)

        elif self.shape == 'I':
            drawBlock(self.position[0],self.position[1],lightblue)
            if self.rotation == 2:
                drawBlock(self.position[0],self.position[1] - 3,lightblue)
                drawBlock(self.position[0],self.position[1] + 3,lightblue)
                drawBlock(self.position[0],self.position[1] + 6,lightblue)
            elif self.rotation == 1:
                drawBlock(self.position[0] - 3,self.position[1],lightblue)
                drawBlock(self.position[0] + 3,self.position[1],lightblue)
                drawBlock(self.position[0] + 6,self.position[1],lightblue)
            elif self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,lightblue)
                drawBlock(self.position[0],self.position[1] - 3,lightblue)
                drawBlock(self.position[0],self.position[1] - 6,lightblue)
            elif self.rotation == 3:
                drawBlock(self.position[0] + 3,self.position[1],lightblue)
                drawBlock(self.position[0] - 3,self.position[1],lightblue)
                drawBlock(self.position[0] - 6,self.position[1],lightblue)

        elif self.shape == 'O':
            drawBlock(self.position[0],self.position[1],yellow)
            drawBlock(self.position[0] + 3,self.position[1],yellow)
            drawBlock(self.position[0],self.position[1] + 3,yellow)
            drawBlock(self.position[0] + 3,self.position[1] + 3,yellow)

    def erase(self):
        if self.shape == 'L':
            drawBlock(self.position[0],self.position[1],black)
            if self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] + 3,self.position[1] + 3,black)
            elif self.rotation == 1:
                drawBlock(self.position[0]+3,self.position[1],black)
                drawBlock(self.position[0]-3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1] + 3,black)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] - 3,self.position[1] - 3,black)
            elif self.rotation == 3:
                drawBlock(self.position[0]+3,self.position[1],black)
                drawBlock(self.position[0]-3,self.position[1],black)
                drawBlock(self.position[0] + 3,self.position[1] - 3,black)

        elif self.shape == 'J':
            drawBlock(self.position[0],self.position[1],black)
            if self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] - 3,self.position[1] + 3,black)
            elif self.rotation == 1:
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1] - 3,black)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] + 3,self.position[1] - 3,black)
            elif self.rotation == 3:
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] + 3,self.position[1] + 3,black)

        elif self.shape == 'S':
            drawBlock(self.position[0],self.position[1],black)
            if self.rotation == 1:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1] + 3,black)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1] - 3,black)
            elif self.rotation == 3:
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] + 3,self.position[1] - 3,black)
            elif self.rotation == 4:
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] + 3,self.position[1] + 3,black)

        elif self.shape == 'Z':
            drawBlock(self.position[0],self.position[1],black)
            if self.rotation == 1:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] + 3,self.position[1] + 3,black)
            elif self.rotation == 2:
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1] + 3,black)
            elif self.rotation == 3:
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1] - 3,black)
            elif self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] + 3,self.position[1] - 3,black)

        elif self.shape == 'T':
            drawBlock(self.position[0],self.position[1],black)
            if self.rotation == 1:
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0],self.position[1] - 3,black)
            elif self.rotation == 2:
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] - 3,black)
            elif self.rotation == 3:
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0],self.position[1] + 3,black)
            elif self.rotation == 4:
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] - 3,black)

        elif self.shape == 'I':
            drawBlock(self.position[0],self.position[1],black)
            if self.rotation == 2:
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] + 6,black)
            elif self.rotation == 1:
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] + 6,self.position[1],black)
            elif self.rotation == 4:
                drawBlock(self.position[0],self.position[1] + 3,black)
                drawBlock(self.position[0],self.position[1] - 3,black)
                drawBlock(self.position[0],self.position[1] - 6,black)
            elif self.rotation == 3:
                drawBlock(self.position[0] + 3,self.position[1],black)
                drawBlock(self.position[0] - 3,self.position[1],black)
                drawBlock(self.position[0] - 6,self.position[1],black)

        elif self.shape == 'O':
            drawBlock(self.position[0],self.position[1],black)
            drawBlock(self.position[0] + 3,self.position[1],black)
            drawBlock(self.position[0],self.position[1] + 3,black)
            drawBlock(self.position[0] + 3,self.position[1] + 3,black)

    #moves the shape one block in the given direction
    def move(self,direction):

        if direction == 'left' and not checkEdge(direction):
            self.erase()
            self.position[0] += -3
            self.draw()

        elif direction == 'right' and not checkEdge(direction):
            self.erase()
            self.position[0] += 3
            self.draw()

        elif direction == 'down':
            if  not checkContact():
                self.erase()
                self.position[1] += 3
                self.draw()

    #rotate the shape 90 degrees clockwise
    def rotate(self):
        global pixel
        if self.position[1] < 59:
            if checkEdge('left'):#move it away from edges if there's anough room.
                self.move('right')
                if self.shape == 'I' and self.rotation == 2:
                    self.move('right')
            elif checkEdge('right'):
                self.move('left')
                if self.shape == 'I' and self.rotation == 4:
                    self.move('left')

            self.erase()
            if self.rotation == 4:
                self.rotation = 1
            else:
                self.rotation += 1
            self.draw()

            self.erase()
            for i in range(32):
                for j in reversed(range(60)):
                    if savestate[xy(i,j)] != black and pixel[xy(i,j)] == black:
                        for i in range(0,32):
                            for j in reversed(range(0,60)):
                                pixel[xy(i,j)] = savestate[xy(i,j)]
                        if self.rotation == 1:
                            self.rotation = 4
                        else:
                            self.rotation += -1
            self.draw()

############################################################       scoring        ##########################################################################

rowsCleared = 0
#check if row is full, then turn full rows white
def highlightLines():
    global rowsCleared, pixel
    for j in reversed(range(1,61,3)):
        filled = False
        for i in range(1,31):
            if pixel[xy(i,j)] != black:
                filled = True
            else:
                filled = False
                break
        if filled:
            for i in range(1,31):
                pixel[xy(i,j)] = white
                pixel[xy(i,j+2)] = white
                pixel[xy(i,j+1)] = white
            rowsCleared += 1

tetris = 0
#returns 1 if 4 or more rows cleared at once, 2 if multiple tetris in a row
def checkTetris():
    global tetris
    if rowsCleared > 3:
        if tetris > 0:
            tetris = 2
        elif tetris == 0:
            tetris = 1
    else:
        tetris = 0
    return tetris

#clear lines and add up the score
def removeLines():
    global rowsCleared,pixel
    if rowsCleared > 0:
        for j in reversed(range(5,61)):
            row = j
            while(pixel[xy(1,row)] == white):
                for j in reversed(range(5,row+1)):
                    for i in range(1,31):
                        pixel[xy(i,j)] = pixel[xy(i,j-1)]
                        pixel[xy(i,j-1)] = black

        addScore(score,100*rowsCleared)
        if checkTetris() == 1:
            addScore(score,400)
        elif checkTetris() == 2:
            addScore(score,800)
        rowsCleared = 0

shapeSequence = ['L','J','S','Z','T','I','O']
currentShape = shape('L', [14,2], 1)
nextShape = shape('L', [42,11], 1)
sequenceNum = 7

import random
#sets the next shape from sequence. must be run twice on startup.
def selectShape():
    global sequenceNum
    if sequenceNum == 7:
        sequenceNum = 0
        random.shuffle(shapeSequence)
    nextShape.erase()
    currentShape.shape = nextShape.shape
    currentShape.rotation = nextShape.rotation
    if currentShape.shape == 'T' or currentShape.shape == 'J':
        currentShape.position = [17, 5]
    elif currentShape.shape == 'O':
        currentShape.position = [14,2]
    else:
        currentShape.position = [17,2]
    nextShape.shape = shapeSequence[sequenceNum]
    nextShape.rotation = 1
    if nextShape.shape == 'I':
        nextShape.position = [41,12]
    elif nextShape.shape == 'L':
        nextShape.position = [43,11]
    elif nextShape.shape == 'J':
        nextShape.position = [43, 14]
    elif nextShape.shape == 'O':
        nextShape.position = [41,11]
    elif nextShape.shape == 'T':
        nextShape.position = [42, 14]
    else:
        nextShape.position = [42,11]

    saveState()

    currentShape.draw()
    nextShape.draw()

    sequenceNum += 1

######################################################      game over       ###############################################################################

#set all leds black
def setBlack():
    global pixel
    for i in range(len(pixel)):
        pixel[i] = black

#set the gameboard to black and set the score to 0
def clearGameBoard():
    global pixel, score
    for i in range(1,31):
        for j in range(1,61):
            pixel[xy(i,j)] = black
    score = [-1,-1,-1,-1,-1,0]

#sets the area of "time up" and "game over" to black
def clearMenu():
    global pixel
    for i in range(26):
        for j in range(16):
            pixel[xy(i+3,j+18)] = black

#displays game over screen
def gameOver():
    clearMenu()
    drawBox(23,15,4,18,grey)
    drawWord('game', 7, 20, white)
    drawWord('over', 7, 26,white)

#displays time up screen
def timeUp():
    clearMenu()
    drawBox(23,15,4,18,grey)
    drawWord('time', 8, 20, white)
    drawWord('up', 13, 26, white)

#displays the start screen
def startMenu():
    clearMenu()
    drawBox(25,15,3,18,grey)
    drawWord('press', 7, 20, white)
    drawWord('enter', 5, 26,white)
