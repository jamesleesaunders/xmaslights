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
