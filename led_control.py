import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SimPixel import *

# causes frame timing information to be output
# bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

# set number of pixels & LED type here http://simpixel.io/
driver = SimPixel(num = 300)

# load the LEDStrip class
ledStrip = Strip(driver)


class BasicAnimTest(BaseStripAnim):
    def __init__(self, led):
        super(BasicAnimTest, self).__init__(led)
        #do any initialization here
  
    def step(self, amt = 1):
        speed = 15
        for i in range(300):
            self._led.set(i, colors.hue2rgb((i*4+(self._step*speed))%256))
        self._step += amt



try:
    anim = BasicAnimTest(ledStrip)
    anim.run(fps=45)
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    led.all_off()
    led.update()
