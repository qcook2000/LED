from __future__ import division

import bibliopixel.colors as colors
from bibliopixel.animation import BaseStripAnim

import random


class Searchlights2(BaseStripAnim):
    """X search lights sweeping at different speeds. X is defined by # colors passed"""

    def __init__(self, layout, colors, tail=5, start=0, end=-1):
        # =[colors.MediumSeaGreen, colors.MediumPurple, colors.MediumVioletRed, colors.Red, colors.Blue]
        super(Searchlights2, self).__init__(layout, start, end)

        self._color = colors
        self._colorcount = len(self._color)
        self._tail = tail + 1
        if self._tail >= self._size // 2:
            self._tail = (self._size // 2) - 1

    def pre_run(self):
        stepsrand = []
        dirrand = []
        for i in range(0, self._colorcount):
            randomint = random.randint(self._start,self._end)
            stepsrand.append(randomint)
            if randomint % 2 == 0:
                dirrand.append(-1)
            else:
                dirrand.append(1)
        self._direction = [1] * self._colorcount
        self._currentpos = [1] * self._colorcount
        self._steps = stepsrand
        self._fadeAmt = 256 / self._tail

    def step(self, amt=1):
        self._ledcolors = [(0, 0, 0) for i in range(self._size)]
        self.layout.all_off()

        for i in range(0, self._colorcount):
            self._currentpos[i] = self._start + self._steps[i]

            # average the colors together so they blend
            self._ledcolors[self._currentpos[i]] = map(lambda x, y: (x + y) // 2, self._color[i], self._ledcolors[self._currentpos[i]])
            for j in range(1, self._tail):
                if self._currentpos[i] - j >= 0:
                    self._ledcolors[self._currentpos[i] - j] = map(lambda x, y: (x + y) // 2, self._ledcolors[self._currentpos[i] - j], colors.color_scale(self._color[i], 255 - (self._fadeAmt * j)))
                if self._currentpos[i] + j < self._size:
                    self._ledcolors[self._currentpos[i] + j] = map(lambda x, y: (x + y) // 2, self._ledcolors[self._currentpos[i] + j], colors.color_scale(self._color[i], 255 - (self._fadeAmt * j)))
            if self._start + self._steps[i] >= self._end:
                self._direction[i] = -1
            elif self._start + self._steps[i] <= 0:
                self._direction[i] = 1

            # advance each searchlight at a slightly different speed
            self._steps[i] += self._direction[i] * amt * int(random.random() > (i * 0.05))

        for i, thiscolor in enumerate(self._ledcolors):
            self.layout.set(i, thiscolor)