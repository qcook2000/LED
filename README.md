# LED

This is to control APA102 LED strips from python 3.4+ on a Raspberry Pi.


Physical items used:
    - Raspberry Pi 3
        - from canakit.com: http://www.canakit.com/raspberry-pi-3-model-b.html
            - includes wifi card, mini-usb power, hdmi cable
        - 8GB micro SD card
    - APA102 LED strips (5M strips bought, cut into 100 led increments)

Setup on the Raspberry Pi:
    - Download Raspbian Jessie Lite image:
        - https://www.raspberrypi.org/documentation/installation/installing-images/README.md
    - Load the image to a micro SD. Add a empty ssh file so that the Raspberry Pi accepts incoming SSH requests after it boots.
        - instructions to load: http://blog.smalleycreative.com/linux/setup-a-headless-raspberry-pi-with-raspbian-jessie-on-os-x/
    - Put the SD card into the Raspberry Pi. Connect via ethernet to your router.
            - note that if the name isn't immediately obvious, you could brute force in by trying:
                - ssh pi@[ipaddress]
                - default user is: pi
                - default password is: raspberry
    - Loading WIFI
        - Follow these instructions, along with loading your wifi credentials, to setup wifi.
        - https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

    - Install SSH for LED Github repo
        - https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
        - note at the step for "ssh-add", use a lowercase k instead.
    - Add the ssh key to your Github account
        - https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-linux

    - Install APA102_Pi python module. Includes instructions for installing Python3
        - https://github.com/tinue/APA102_Pi

For programming the LEDs...
    - 
    - We used the BiblioPixel python library
        - https://github.com/ManiacalLabs/BiblioPixel
    - Python packages needed for install:
        - BiblioPixel
        - Click
        - spidev
            - setup: https://github.com/ManiacalLabs/BiblioPixel/wiki/SPI-Setup

