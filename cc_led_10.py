import time
import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SPI.APA102 import *
import bibliopixel.colors as colors

bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)
 
driver = APA102(num = 10, c_order = ChannelOrder.BGR)

# load the LEDStrip class
led = Strip(driver)
leds = [led]

def show():
    for i in leds:
        i.update()

def turnoff():
    for i in leds:
        i.all_off()
    show()

def blink ():
    leds.fill(colors.Red, 0, 4)
    show()
    time.sleep(1)
    turnoff()