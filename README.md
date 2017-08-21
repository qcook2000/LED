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
    - 5 strips, requiring 18A each
- AllPixel: http://maniacallabs.com/allpixel/
- Soldering Iron, Solder, Solder Adhesive
- Several Male-Male and Female-Female colored wires
- Power Supply for AllPixel+LED Strip, at 15A each
    - Each power supply will support 3 strips of 100 LEDs
        - Technically need 18A+, however these are non-standard / difficult to find

Raspberry Pi Setup
---
Download Raspbian Jessie Lite image
-   https://www.raspberrypi.org/documentation/installation/installing-images/README.md
Load image to Micro SD, Setup SSH
-   http://blog.smalleycreative.com/linux/setup-a-headless-raspberry-pi-with-raspbian-jessie-on-os-x/
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
Install Python3, Pip
-   sudo apt-get install python3 python3-pip

LED Software
---
From the Bibliopixel directory, run:
- sudo python3 setup.py install
- sudo pip3 install pyserial --upgrade --ignore-installed
    - in case of errors, you might need to reinstall this 
    - https://raspberrypi.stackexchange.com/questions/68837/pyserial-error-on-raspberry-3
- ls /dev/ttyACM*
    - Run this to show all USBs attached. Should show up as "/dev/ttyACM0" or similar

Editing Files on the Raspberry Pi from local machine via Sublime Package
---
- https://stackoverflow.com/questions/37458814/how-to-open-remote-files-in-sublime-text-3
- Synopsis of above link:
    - install rsub on server:
        - sudo wget -O /usr/local/bin/rsub \https://raw.github.com/aurora/rmate/master/rmate
        - sudo chmod a+x /usr/local/bin/rsub
    - Locally, install the "rsub" package
    - On command line connecting to server: 
        - ssh -R 52698:localhost:52698 server_user@server_address
            - for example: 
                - ssh -R 52698:localhost:52698 pi@10.0.0.154
    - Navigate to file and open:
        - rsub file_to_open.txt

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