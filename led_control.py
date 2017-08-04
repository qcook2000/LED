import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SimPixel import *

from BiblioAnimations.BiblioPixelAnimations.strip import Rainbows

# causes frame timing information to be output
# bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

# set number of pixels & LED type here http://simpixel.io/
driver = SimPixel(num = 300)

# load the LEDStrip class
ledStrip = Strip(driver)

try:
    anim = Rainbows.RainbowCycle(ledStrip)
    anim.run()
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    led.all_off()
    led.update()
