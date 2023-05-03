# MIT License
# 
# Copyright (c) 2023 CashLabMines
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import datetime
import board
import neopixel
import os
import subprocess
from saveImages import calibrationImages, multipleImages

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
colorLoop = [0,1,2,3]

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
        colorStr = "Ext"
        print("Starting: Ext")
    pixels.show()
    time.sleep(ledTime)
    #calibrationImages(expName,colorStr)
    multipleImages(expName,colorStr)

# Turn off Leds
pixels.fill((0,0,0))
pixels.show()
