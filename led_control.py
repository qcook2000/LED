import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SimPixel import *


# causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

# set number of pixels & LED type here http://simpixel.io/
driver = SimPixel(num = 300)

# load the LEDStrip class
ledStrip = Strip(driver)

# animations = [
#         Alternates.Alternates(), #layout, max_led=-1, color1=(255, 255, 255), color2=(0, 0, 0) 
#         BinaryEpochClock.BEClock(), #layout, onColor=colors.Red, offColor=colors.Off, bitWidth=1, bitSpace=1, reverse=False
#         ColorChase.ColorChase(), #layout, color=[255, 0, 0], width=1, start=0, end=-1
#         ColorFade.ColorFade(), #layout, colors=[colors.Red], step=5, start=0, end=-1
#         ColorPattern.ColorPattern(), #layout, colors=[colors.Red, colors.Green, colors.Blue], width=1, dir=True, start=0, end=-1
#         ColorWipe.ColorWipe(), #layout, color=[255, 0, 0], start=0, end=-1
#         FireFlies.FireFlies(), #layout, colors=[colors.Red], width=1, count=1, start=0, end=-1
#         HalvesRainbow.HalvesRainbow(), #layout, max_led=-1, centre_out=True, rainbow_inc=4
#         LarsonScanners.LarsonRainbow(), #layout, tail=2, start=0, end=-1
#         LarsonScanners.LarsonScanner(), #layout, color=colors.Red, tail=2, start=0, end=-1
#         LinearRainbow.LinearRainbow(), #layout, max_led=-1, individual_pixel=False
#         PartyMode.PartyMode(), #layout, colors=[colors.Red, colors.Green, colors.Blue], start=0, end=-1
#         PixelPingPong.PixelPingPong(), #layout, max_led=None, color=(255, 255, 255), total_pixels=1, fade_delay=1
#         RGBClock.RGBClock(), #layout, hStart=0, hEnd=0, mStart=1, mEnd=1, sStart=2, sEnd=2
#         Rainbows.Rainbow(), #layout, start=0, end=-1
#         Rainbows.RainbowCycle(), #
#         Searchlights.Searchlights(), #layout, colors=[colors.MediumSeaGreen, colors.MediumPurple, colors.MediumVioletRed], tail=5, start=0, end=-1
#         Wave.Wave(), #layout, color=colors.Red, cycles=2, start=0, end=-1
#         Wave.WaveMove(), #layout, color=colors.Red, cycles=2, start=0, end=-1
#         WhiteTwinkle.WhiteTwinkle(), #layout, max_led=None, density=80, speed=2, max_bright=255
#         hexclock.HEXClock() #layout
#         ]

# animationIndex = 0

try:
    anim = RainbowCycle(ledStrip)
    anim.run()
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    ledStrip.all_off()
    ledStrip.update()
