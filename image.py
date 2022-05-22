from functions import *
from neopixel import *
from PIL import Image

file = 'logo.jpg'

#####################################################################       LED Info        ##################################################################

NUM_LEDS       = 1922
LED_PIN        = 18
LED_PIN2       = 13
LED_CHANNEL    = 0
LED_CHANNEL2   = 1
LED_FREQ       = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 50
STRIP_TYPE     = ws.WS2811_STRIP_GRB

leftBoard = Adafruit_NeoPixel(NUM_LEDS, LED_PIN2, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS, LED_CHANNEL2, STRIP_TYPE)
rightBoard = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, LED_FREQ, LED_DMA, False, LED_BRIGHTNESS, LED_CHANNEL, STRIP_TYPE)

def update():
    for i in range(len(pixel)):
        if i < 1922:
            leftBoard.setPixelColor(i, pixel[i])
        else:
            rightBoard.setPixelColor(i - 1922, pixel[i])
    leftBoard.show()
    rightBoard.show()

def image():
    im = Image.open(file)
    pix = im.load()
    for i in range(62):
        for j in range(62):
            pixel[xy(i,j)] = Color(pix[i,j][0],pix[i,j][1],pix[i,j][2])

    update()

    
if __name__ == '__main__':
    leftBoard.begin()
    rightBoard.begin()
    image()
