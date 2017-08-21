from bibliopixel import *                   
from bibliopixel.animation import *
import bibliopixel.colors as colors
#Load driver for the AllPixel
from bibliopixel.drivers.serial.driver import *
import time
#set number of pixels & LED type here 
driver1 = Serial(num = 100, ledtype = LEDTYPE.APA102, c_order = ChannelOrder.BGR, device_id = 1)
driver2 = Serial(num = 100, ledtype = LEDTYPE.APA102, c_order = ChannelOrder.BGR, device_id = 2)
driver3 = Serial(num = 100, ledtype = LEDTYPE.APA102, c_order = ChannelOrder.BGR, device_id = 3)

sect33 = 33
sect66 = 66
sect100 = 100

led1 = LEDStrip(driver1)
led2 = LEDStrip(driver2)
led3 = LEDStrip(driver3)

leds = [led1, led2, led3]

def show():
    for i in leds:
        i.update()

def turnoff():
    for i in leds:
        i.all_off()
    show()

led1.fill(colors.Red, 0, 100)
led2.fill(colors.Blue, 0, 100)
led3.fill(colors.Green, 0, 100)

show()

time.sleep(5)

turnoff()

