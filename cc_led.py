from bibliopixel import *                   
from bibliopixel.animation import *
import bibliopixel.colors as colors
#Load driver for the AllPixel
from bibliopixel.drivers.serial.driver import *
#set number of pixels & LED type here 
driver = Serial(num = 100, ledtype = LEDTYPE.APA102, c_order = ChannelOrder.BGR)

sect33 = 33
sect66 = 66
sect100 = 100

led = LEDStrip(driver)