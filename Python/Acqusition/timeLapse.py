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

from datetime import datetime, timedelta
import time
import os
import board
import neopixel
from saveImages import timeImage

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

# Ask user for number of days
while True:
    try:
        numDays = int(input("Enter length of experiment (days): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if numDays < 0:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# Ask user for delay between images
while True:
    try:
        timeDelayMins = float(input("Enter the delay between images (mins): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if timeDelayMins < 0:
        print("Invalid Entry. Try again")
        continue
    else:
        break
timeDelay = timeDelayMins * 60;

# Ask user for LED on time
while True:
    try:
        ledOnTimeMins = int(input("Enter the LED on time (mins): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if timeDelayMins < 0:
        print("Invalid Entry. Try again")
        continue
    else:
        break
ledOnTime = ledOnTimeMins * 60

imageCycles = int(ledOnTime / timeDelay)
dayCyles = int((numDays * 86400) / timeDelay)
numImageCycles = 0
numDayCylces = 0
ledState = True
pixels.fill((255,255,255))
pixels.show()

while numDayCylces <= dayCyles:
    # Get current system time
    execStr = datetime.now()
    startSec = execStr.second
    
    # Check if LED on time is elapsed
    if numImageCycles >= imageCycles:
        # Reset cycle counter
        numImageCyles = 0
        
        # If LEDs on on, turn off
        if ledState:
            pixels.fill((0,0,0))
            pixels.show()
            ledState = False
            print('Turning LEDs off')
        # If LEDs on off, turn on
        else:
            pixels.fill((255,255,255))
            pixels.show()
            ledState = True
            print('Turning LEDs On') 
    
    # Save image
    timeImage(expName)
    
    # Incremen cycle counter
    numImageCycles += 1
    numDayCylces += 1
    
    # Get current system time
    execStr = datetime.now()
    endSec = execStr.second
    
    # Sleep for image delay time
    sleepTime = timeDelayMins * 60 - (endSec-startSec)
    print('Sleeping for: ', sleepTime, ' secs')
    time.sleep(sleepTime)
    
    
    
