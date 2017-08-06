import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SPI.APA102 import *

import logging, sys

import click

bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

driver = APA102(num = 100)

# load the LEDStrip class
ledStrip = Strip(driver)

# load channel test animation
from bibliopixel.animation import StripChannelTest
anim = StripChannelTest(ledStrip)

# load the LEDStrip class
ledStrip = Strip(driver)
try:
    # run the animation
    anim.run()
except KeyboardInterrupt:
    # Ctrl+C will exit the animation and turn the LEDs offs
    ledStrip.all_off()
    ledStrip.update() 
