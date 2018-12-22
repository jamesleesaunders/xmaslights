## Raspberry Pi Christmas Lights

### Initial Setup

1. Download Raspbian Image
Head on over [here](https://www.raspberrypi.org/downloads/raspbian/) to grab a copy of the Raspbian image. The 'Lite' version will do.

2. Write Image to SD Card
Write the image to SD card. You can find detailed instructions [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

3. Add "ssh" File to the SD Card Root
Enable SSH by placing a file named "ssh" (without any extension) onto the boot partition of the SD card.

```
touch ssh
```

4. Boot your Pi
Pop your prepared SD card, power and a network cable into the Pi.

5. Connect to Pi.
SSH to Pi over wireless:

```
ssh pi@raspberrypi.local
```

[Tutorial](https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0)

### Pocketmonytronics RGB Tree

http://www.pocketmoneytronics.co.uk/?page_id=423

Using the Raspberry Pi version.
I have put together a simple bit of example Python code with you can download from http://www.pocketmoneytronics.co.uk/downloads/rgb_tree_example.py
https://www.raspberrypi-spy.co.uk/2016/12/rgb-led-christmas-tree-by-pocketmoneytronics/

This code works but is quite rough: any seasoned Python programmers out there will probably cry into their keyboards – sorry! If you have ideas on how to improve it, please get in touch.

To use the example code, you need the rpi_ws281x library by Jeremy Garff and Richard Hirst. If you’ve ever used the excellent Pimoroni Unicorn HAT or 4tronix’s McRoboFace (and if not, why not?!) or any other Neopixel-style products then you’ve probably got this installed. I hope to provide more instructions soon (again: can you help with this? Please get in touch!) but, for now, the easiest way is probably to use Pimoroni’s excellent installer.

With the power switched off, connect the tree on pins 1 to 16, facing outwards.


### Ryanteck SnowPi

https://ryanteck.uk/
https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/led-boards-1040/ryanteck-snowpi-the-gpio-snowman-for-raspberry-pi
https://www.modmypi.com/blog/ryanteck-tutorials/ryanteck-snowpi-tutorials

### ModMyPi Programmable Christmas Tree

![alt text](https://github.com/jamesleesaunders/xmaslights/blob/master/modmypi_tree.jpg "Christmas Tree")

https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/led-boards-1040/christmas-tree-programmable-kit
https://github.com/modmypi/Programmable-Xmas-Tree/
