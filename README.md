#learm-python

Python scripts to connect to a Lewansoul LeArm device and move the servos

## Assumptions

I'm running all of this on a Mac - for now until I can dig deeper on a Raspberry Pi.

## Dependencies

I'm using an Adafruit USB to Serial connector https://www.adafruit.com/product/954. I had to install the drivers here http://www.silabs.com/Support%20Documents/Software/Mac_OSX_VCP_Driver.zip.

The Python scripts depend on Pyserial so `pip install pyserial`.

## Examples

`simple.py` is very basic - just a single movement.
