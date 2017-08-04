import bibliopixel
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.layout import *
from bibliopixel.drivers.SimPixel import *

import logging, sys

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
driver = SimPixel(num = 300)

# load the LEDStrip class
ledStrip = Strip(driver)

animations = [
#         Alternates(), #layout, max_led=-1, color1=(255, 255, 255), color2=(0, 0, 0) 
#         BEClock(), #layout, onColor=colors.Red, offColor=colors.Off, bitWidth=1, bitSpace=1, reverse=False
#         ColorChase(), #layout, color=[255, 0, 0], width=1, start=0, end=-1
#         ColorFade(), #layout, colors=[colors.Red], step=5, start=0, end=-1
#         ColorPattern(), #layout, colors=[colors.Red, colors.Green, colors.Blue], width=1, dir=True, start=0, end=-1
#         ColorWipe(), #layout, color=[255, 0, 0], start=0, end=-1
        FireFlies(ledStrip, [colors.White], 1, 10), #layout, colors=[colors.Red], width=1, count=1, start=0, end=-1
#         HalvesRainbow(), #layout, max_led=-1, centre_out=True, rainbow_inc=4
#         LarsonRainbow(), #layout, tail=2, start=0, end=-1
#         LarsonScanner(), #layout, color=colors.Red, tail=2, start=0, end=-1
#         LinearRainbow(), #layout, max_led=-1, individual_pixel=False
#         PartyMode(), #layout, colors=[colors.Red, colors.Green, colors.Blue], start=0, end=-1
#         PixelPingPong(), #layout, max_led=None, color=(255, 255, 255), total_pixels=1, fade_delay=1
#         RGBClock(), #layout, hStart=0, hEnd=0, mStart=1, mEnd=1, sStart=2, sEnd=2
        Rainbow(ledStrip) #layout, start=0, end=-1
#         RainbowCycle(), #
#         Searchlights(), #layout, colors=[colors.MediumSeaGreen, colors.MediumPurple, colors.MediumVioletRed], tail=5, start=0, end=-1
#         Wave(), #layout, color=colors.Red, cycles=2, start=0, end=-1
#         WaveMove(), #layout, color=colors.Red, cycles=2, start=0, end=-1
#         WhiteTwinkle(), #layout, max_led=None, density=80, speed=2, max_bright=255
#         HEXClock() #layout
        ]

animationIndex = 0

def getNextAnimation(i) :
    global animationIndex

    click.echo("Now: " + animations[animationIndex].__class__.__name__ + " | Press ←↑→↓ or 0-Z: ", nl=False)
    k = click.getchar()
    click.echo()

    animations[animationIndex].completed = True

    if k=='\x1b[A' or k=='\x1b[C': # up or right
        animationIndex += 1
    elif k=='\x1b[B' or k=='\x1b[D': # down or left
        animationIndex -= 1
    else:
        print("not an arrow key!")
        raise KeyboardInterrupt

    while animationIndex < 0:
        animationIndex += len(animations)

    while animationIndex >= len(animations):
        animationIndex -= len(animations)

    animations[animationIndex].run(until_complete = True, threaded = True)


try:
    while True:
        getNextAnimation(0)
        getNextAnimation(1)
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    ledStrip.all_off()
    ledStrip.update()
