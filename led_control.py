import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SPI import *
from bibliopixel.drivers.SimPixel import *

import logging, sys
from sys import platform

import click

from BiblioAnimations.BiblioPixelAnimations.strip.Alternates import *
from BiblioAnimations.BiblioPixelAnimations.strip.BinaryEpochClock import *
from BiblioAnimations.BiblioPixelAnimations.strip.ColorChase import *
from BiblioAnimations.BiblioPixelAnimations.strip.ColorFade import *
from BiblioAnimations.BiblioPixelAnimations.strip.ColorPattern import *
from BiblioAnimations.BiblioPixelAnimations.strip.ColorWipe import *
from BiblioAnimations.BiblioPixelAnimations.strip.FireFlies import *
from BiblioAnimations.BiblioPixelAnimations.strip.HalvesRainbow import *
from BiblioAnimations.BiblioPixelAnimations.strip.LarsonScanners import *
from BiblioAnimations.BiblioPixelAnimations.strip.LinearRainbow import *
from BiblioAnimations.BiblioPixelAnimations.strip.PartyMode import *
from BiblioAnimations.BiblioPixelAnimations.strip.PixelPingPong import *
from BiblioAnimations.BiblioPixelAnimations.strip.RGBClock import *
from BiblioAnimations.BiblioPixelAnimations.strip.Rainbows import *
from BiblioAnimations.BiblioPixelAnimations.strip.Searchlights import *
from BiblioAnimations.BiblioPixelAnimations.strip.Wave import *
from BiblioAnimations.BiblioPixelAnimations.strip.WhiteTwinkle import *
from BiblioAnimations.BiblioPixelAnimations.strip.hexclock import *

# set number of pixels & LED type here http://simpixel.io/
if platform == "linux" or platform == "linux2":
    driver = SPI(9 , num = 100, interface = 1) # 9 is the code for APA102s: https://github.com/ManiacalLabs/BiblioPixel/blob/master/bibliopixel/drivers/SPI/driver.py#L20
else:
    driver = SimPixel(num = 100)

# load the LEDStrip class
ledStrip = Strip(driver)

animationIndex = 0
activeAnim = None
aK = list("1234567890wertyuiop")
animations = {
        aK[0]: { "c": Alternates, "args": dict(max_led=-1, color1=(255, 255, 255), color2=(0, 0, 0)) },
        aK[1]: { "c": ColorChase, "args": dict(color=[255, 0, 0], width=1) },
        aK[2]: { "c": ColorFade, "args": dict(colors=[colors.Red], step=5) },
        aK[3]: { "c": ColorPattern, "args": dict(colors=[colors.Red, colors.Green, colors.Blue], width=1, dir=True) },
        aK[4]: { "c": ColorWipe, "args": dict(color=[255, 0, 0]) },
        aK[5]: { "c": FireFlies, "args": dict(colors=[colors.White], width=1, count=1) },
        aK[6]: { "c": HalvesRainbow, "args": dict(max_led=-1, centre_out=True, rainbow_inc=4) },
        aK[7]: { "c": LarsonRainbow, "args": dict(tail=2) },
        aK[8]: { "c": LarsonScanner, "args": dict(color=colors.Red, tail=2) },
        aK[9]: { "c": LinearRainbow, "args": dict(max_led=-1, individual_pixel=False) },
        aK[10]: { "c": PartyMode, "args": dict(colors=[colors.Red, colors.Green, colors.Blue]) },
        aK[11]: { "c": PixelPingPong, "args": dict(max_led=None, color=(255, 255, 255), total_pixels=1, fade_delay=1) },
        aK[12]: { "c": Rainbow, "args": dict() },
        aK[13]: { "c": RainbowCycle, "args": dict() },
        aK[14]: { "c": Searchlights, "args": dict(colors=[colors.MediumSeaGreen, colors.MediumPurple, colors.MediumVioletRed], tail=5) },
        aK[15]: { "c": Wave, "args": dict(color=colors.Red, cycles=2) },
        aK[16]: { "c": WaveMove, "args": dict(color=colors.Red, cycles=2) },
        aK[17]: { "c": WhiteTwinkle, "args": dict(max_led=None, density=80, speed=2, max_bright=255)}
}
animationKeys = aK[0:17]

def getNextAnimation() :
    global animationIndex
    global activeAnim

    label = "OFF" if activeAnim == None else activeAnim.__class__.__name__
        
    click.echo("Now: " + label + " | Press ←↑→↓, 0-" + animationKeys[-1] + ", space for index or delete for off: ", nl=False)
    k = click.getchar()
    click.echo()

    # Find next animation
    if k=='\x1b[A' or k=='\x1b[C': # up or right
        animationIndex += 1
    elif k=='\x1b[B' or k=='\x1b[D': # down or left
        animationIndex -= 1
    elif k in animationKeys:
        animationIndex = animationKeys.index(k)
    elif k==' ':
        for key in animationKeys: print(key + ": " + animations[key]["c"].__name__)
        return
    elif k=='\x1b':
        ledStrip.all_off()
        ledStrip.update()
        raise KeyboardInterrupt
    elif k=='\x08' or k=='\x7f': 
        ledStrip.all_off()
        ledStrip.update()
        if activeAnim != None:
            activeAnim.completed = True
            activeAnim = None
        return
    else:
        print("No matching command. If you would like to exit press \'esc\'")
        return

    # Clean up current animation
    if activeAnim != None:
        activeAnim.completed = True
        activeAnim = None

    # Fix the index if its over / under
    while animationIndex < 0: animationIndex += len(animationKeys)
    while animationIndex >= len(animationKeys): animationIndex -= len(animationKeys)

    activeAnimDict = animations[animationKeys[animationIndex]]
    activeAnim = activeAnimDict["c"](ledStrip, **(activeAnimDict["args"]))
    activeAnim.run(until_complete = True, threaded = True)

try:
    # Start initial animation
    while True:
        getNextAnimation()
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    ledStrip.all_off()
    ledStrip.update()
