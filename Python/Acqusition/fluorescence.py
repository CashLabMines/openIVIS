import time
import datetime
import board
import neopixel
import os
import subprocess
from saveImages import saveImage

# Pixel Variable
ledPin = board.D18          # Data in pin of the NeoPixel strip
ledNum = 8                  # Number of NeoPixels
ledOrder = neopixel.RGB     # Order of the pixel colors (RGBW or GRBW)
ledLevel = 1.0              # LED Brightness level
ledTime = 1.0               # LED time delay
pixels = neopixel.NeoPixel(ledPin, ledNum, brightness=ledLevel, auto_write=False, pixel_order=ledOrder)

# Main Function
# Ask User for Experiment Name
while True:
    try:
        expName = input("Enter experiment name: ")
    except expName:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# Turn off Leds
pixels.fill((0,0,0))
pixels.show()
colorLoop = [4]

print("Looping through colors: RGBW")
for ii in colorLoop:
    if ii == 0:
        pixels.fill((255, 0, 0))
        colorStr = "Red"
        print("Starting: Red")
    elif ii == 1:
        pixels.fill((0, 255, 0))
        colorStr = "Green"
        print("Starting: Green")
    elif ii == 2:
        pixels.fill((0, 0, 255))
        colorStr = "Blue"
        print("Starting: Blue")
    elif ii == 3:
        pixels.fill((255,255,255))
        colorStr = "White"
        print("Starting: White")
    else:
        pixels.fill((255,255,255))
        colorStr = "UV"
        print("Starting: UV")
    pixels.show()
    time.sleep(ledTime)
    saveImage(expName,colorStr)

# Turn off Leds
pixels.fill((0,0,0))
pixels.show()
