import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SimPixel import *

from BiblioAnimations.BiblioPixelAnimations.strip import *

# causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

# set number of pixels & LED type here http://simpixel.io/
driver = SimPixel(num = 300)

# load the LEDStrip class
ledStrip = Strip(driver)

animations = [
        Alternates.Alternates(),
        BinaryEpochClock.BEClock(),
        ColorChase.ColorChase(),
        ColorFade.ColorFade(),
        ColorPattern.ColorPattern(),
        ColorWipe.ColorWipe(),
        FireFlies.FireFlies(),
        HalvesRainbow.HalvesRainbow(),
        LarsonScanners.LarsonRainbow(),
        LarsonScanners.LarsonScanner(),
        LinearRainbow.LinearRainbow(),
        PartyMode.PartyMode(),
        PixelPingPong.PixelPingPong(),
        RGBClock.RGBClock(),
        Rainbows.Rainbow(),
        Rainbows.RainbowCycle(),
        Searchlights.Searchlights(),
        Wave.Wave(),
        Wave.WaveMove(),
        WhiteTwinkle.WhiteTwinkle(),
        hexclock.HEXClock() ]

animationIndex = 0

try:
    anim = Rainbows.RainbowCycle(ledStrip)
    anim.run()
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    led.all_off()
    led.update()
