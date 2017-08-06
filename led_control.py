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
currentAnimation = None
animationNames = [
        # "Alternates",
        # "BEClock",
        # "ColorChase",
        # "ColorFade",
        # "ColorPattern",
        # "ColorWipe",
        "FireFlies",
        # "HalvesRainbow",
        # "LarsonRainbow",
        # "LarsonScanner",
        # "LinearRainbow",
        # "PartyMode",
        # "PixelPingPong",
        # "RGBClock",
        "Rainbow"#,
        # "RainbowCycle",
        # "Searchlights",
        # "Wave",
        # "WaveMove",
        # "WhiteTwinkle",
        # "HEXClock"
        ]

def getNewAnimationForName(name) :
    global ledStrip
    if   name == "Alternates":    return Alternates()                               #layout, max_led=-1, color1=(255, 255, 255), color2=(0, 0, 0) 
    elif name == "BEClock":       return BEClock()                                  #layout, onColor=colors.Red, offColor=colors.Off, bitWidth=1, bitSpace=1, reverse=False
    elif name == "ColorChase":    return ColorChase()                               #layout, color=[255, 0, 0], width=1, start=0, end=-1
    elif name == "ColorFade":     return ColorFade()                                #layout, colors=[colors.Red], step=5, start=0, end=-1
    elif name == "ColorPattern":  return ColorPattern()                             #layout, colors=[colors.Red, colors.Green, colors.Blue], width=1, dir=True, start=0, end=-1
    elif name == "ColorWipe":     return ColorWipe()                                #layout, color=[255, 0, 0], start=0, end=-1
    elif name == "FireFlies":     return FireFlies(ledStrip, [colors.White], 1, 10) #layout, colors=[colors.Red], width=1, count=1, start=0, end=-1
    elif name == "HalvesRainbow": return HalvesRainbow()                            #layout, max_led=-1, centre_out=True, rainbow_inc=4
    elif name == "LarsonRainbow": return LarsonRainbow()                            #layout, tail=2, start=0, end=-1
    elif name == "LarsonScanner": return LarsonScanner()                            #layout, color=colors.Red, tail=2, start=0, end=-1
    elif name == "LinearRainbow": return LinearRainbow()                            #layout, max_led=-1, individual_pixel=False
    elif name == "PartyMode":     return PartyMode()                                #layout, colors=[colors.Red, colors.Green, colors.Blue], start=0, end=-1
    elif name == "PixelPingPong": return PixelPingPong()                            #layout, max_led=None, color=(255, 255, 255), total_pixels=1, fade_delay=1
    elif name == "RGBClock":      return RGBClock()                                 #layout, hStart=0, hEnd=0, mStart=1, mEnd=1, sStart=2, sEnd=2
    elif name == "Rainbow":       return Rainbow(ledStrip)                           #layout, start=0, end=-1
    elif name == "RainbowCycle":  return RainbowCycle()                             #
    elif name == "Searchlights":  return Searchlights()                             #layout, colors=[colors.MediumSeaGreen, colors.MediumPurple, colors.MediumVioletRed], tail=5, start=0, end=-1
    elif name == "Wave":          return Wave()                                     #layout, color=colors.Red, cycles=2, start=0, end=-1
    elif name == "WaveMove":      return WaveMove()                                 #layout, color=colors.Red, cycles=2, start=0, end=-1
    elif name == "WhiteTwinkle":  return WhiteTwinkle()                             #layout, max_led=None, density=80, speed=2, max_bright=255
    elif name == "HEXClock":      return HEXClock()                                 #layout
    else:
        print("Used bad animation name: " + name)
        return 


def getNextAnimation() :
    global animationIndex
    global currentAnimation

    currentAnimName = "OFF" if currentAnimation == None else currentAnimation.__class__.__name__
        
    click.echo("Now: " + currentAnimName + " | Press ←↑→↓ or 0-Z: ", nl=False)
    k = click.getchar()
    click.echo()

    # Clean up current animation
    if currentAnimation != None:
        currentAnimation.completed = True
        currentAnimation = None

    # Find next animation
    if k=='\x1b[A' or k=='\x1b[C': # up or right
        animationIndex += 1
    elif k=='\x1b[B' or k=='\x1b[D': # down or left
        animationIndex -= 1
    elif k=='x':
        ledStrip.all_off()
        ledStrip.update()
        raise KeyboardInterrupt
    else:
        print("Not an arrow key, turning off. If you would like to exit press \'x\'")
        ledStrip.all_off()
        ledStrip.update()
        return

    # Fix the index if its over / under
    while animationIndex < 0: animationIndex += len(animationNames)
    while animationIndex >= len(animationNames): animationIndex -= len(animationNames)

    currentAnimation = getNewAnimationForName(animationNames[animationIndex])
    currentAnimation.run(until_complete = True, threaded = True)

try:
    # Start initial animation
    while True:
        getNextAnimation()
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    ledStrip.all_off()
    ledStrip.update()
