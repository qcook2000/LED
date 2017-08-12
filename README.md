# LED
---
This is to control APA102 LED strips from python 3.4+ on a headless Raspberry Pi, wirelessly.

---

Shopping List
---
- Raspberry Pi 3
    - from canakit.com: http://www.canakit.com/raspberry-pi-3-model-b.html
- 32GB micro SD card
- APA102 300 LED strips (5M strips bought, which have different amperage requirements)
- AllPixel: http://maniacallabs.com/allpixel/
- Soldering Iron, Solder, Solder Adhesive
- Several Male-Male and Female-Female colored wires
- Breadboard for testing (replaced by AllPixel)
- Several Power Supplies, at 15A+ each
    - Each power supply will support 3 strips of 100 LEDs

Raspberry Pi Setup
---
Download Raspbian Jessie Lite image
- https://www.raspberrypi.org/documentation/installation/installing-images/README.md
Load image to Micro SD, Setup SSH
- http://blog.smalleycreative.com/linux/setup-a-headless-raspberry-pi-with-raspbian-jessie-on-os-x/
Insert SD card into the Raspberry Pi. Connect via ethernet to your router.
        - note that if the name isn't immediately obvious, you could brute force in by trying:
            - ssh pi@[ipaddress]
            - default user is: pi
            - default password is: raspberry
Enable WIFI
- https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

Edit Raspberry Pi config
- sudo raspi-config
    - Set SPI, SSH and Expand File System
    - Reboot
Install SSH for LED/Bibliopixel Github repos
-   https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
-   note at the step for "ssh-add", use a lowercase k instead.
Install Python3
-   sudo apt-get install python3

LED Software
---




Setup PixelWeb
Install non-python reqs
-   sudo apt-get install git python-pip python-dev python-pyaudio libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk 
-   sudo pip install pip --upgrade
 Install Python Reqs
-   sudo -H pip install pyaudio numpy pillow spidev
Run Pixel Web
-   sudo run-pixelweb



Deprecated (unused), but useful info:

-   Add the ssh key to your Github account
    -   https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-linux
For programming the LEDs...
-   We used the BiblioPixel python library
    -   https://github.com/ManiacalLabs/BiblioPixel
-   Python packages needed for install:
    -   BiblioPixel
    -   Click
    -   spidev
        -   setup: https://github.com/ManiacalLabs/BiblioPixel/wiki/SPI-Setup