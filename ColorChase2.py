from bibliopixel.animation import BaseStripAnim
import math

class ColorChase2(BaseStripAnim):
    """Chase one pixel down the strip."""

    def __init__(self, layout, colors=[[255, 0, 0], [255, 0, 0]], width=1, start=0, end=-1):
        super(ColorChase, self).__init__(layout, start, end)
        self._colors = colors
        self._width = width
        length = math.floor((self._end - self._start) / len(self._colors))
        self._starts = []
        for j in range(len(self._colors)):
            self._starts.append(self._start + (j * length))

    def pre_run(self):
        self._step = 0

    def step(self, amt=1):
        self.layout.all_off()  # because I am lazy

        for j in range(len(self._colors)):
            # Put each color in the strip
            for i in range(self._width):
                self.layout.set(self._starts[j] + self._step + i, self._color)

        self._step += amt
        overflow = (self._start + self._step) - self._end
        if overflow >= 0:
            self._step = overflow