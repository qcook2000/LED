# ## Alternates ##
# This animation alternates colours on every other pixel and then animates them flipping between the default
# colours White and Off.
#
# ## Usage ###
# Alternates has 3 optional properties
#
# * max_led - int the number of pixels you want used
# * color1 - (int, int, int) the color you want the odd pixels to be
# * color2 - (int, int, int) the color you want the even pixels to be
#
# In code:
#
#   from Alternates import Alternates
#   ...
#   anim = Alternates(led, max_led=10, color1=(255, 0, 0), color2=(0, 0, 255))
#
# Best run in the region of 5-10 FPS


from bibliopixel.animation import BaseStripAnim
import bibliopixel.colors as colors


class Alternates2(BaseStripAnim):

    def __init__(self, layout, max_led=-1, colors=[colors.Red, colors.PeachPuff, colors.Off]):
        super(Alternates2, self).__init__(layout, 0, -1)
        self._current = 0
        self._colors = colors
        self._colorcount = len(self._colors)
        self._minLed = 0
        self._maxLed = max_led
        if self._maxLed < 0 or self._maxLed < self._minLed:
            self._maxLed = self.layout.numLEDs - 1
        self._positive = True

    def pre_run(self):
        self._step = 0

    def step(self, amt=1):

        while self._current < self._maxLed:
            colorstart = self._current % self._colorcount
            if self._positive == False:
                colorstart = (colorstart + 1) % self._colorcount
            self.layout.fill(self._colors[colorstart], self._current, self._current)
            self._current += amt
        self._current = self._minLed
        self._positive = not self._positive