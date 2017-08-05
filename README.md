# LED

This is to control APA102 LED strips from python 3.4+ on a Raspberry Pi.
The lights will be placed on a 24 ft Geodesic Dome, which dictate the length 
of the strips. 

Physical items used:
    - Raspberry Pi
        - includes wifi card
        - connected w/ bluetooth keyboard/mouse
        - powered by mini-usb
        - hdmi cable for visual output
    - APA102 LED strips (5M strips bought, cut into 100 led increments)

Setup on the Raspberry Pi:
    - need to install ssh to pull this repository
        - https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
    - Python 3.4+ already installed

For programming the LEDs...
    - We used the BiblioPixel python library
        - https://github.com/ManiacalLabs/BiblioPixel
    - Python packages needed for install:
        - BiblioPixel
        - Click
        - spidev
            - setup: https://github.com/ManiacalLabs/BiblioPixel/wiki/SPI-Setup