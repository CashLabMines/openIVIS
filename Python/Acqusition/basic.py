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

# Function to save images
def save_image(expName,color,level):
    imgPath = "/home/pi/Pictures/" + expName + "/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
    levelStr = "{:.2f}".format(level)
    imgName = imgPath + expName + "_" + color + "_" + levelStr + ".png"
    subprocess.run(["libcamera-still","-e","png","-o",imgName])

# Pixel Variable
pin = board.D18    # Pin connected to the Data In of the NeoPixel strip
num = 8            # The number of NeoPixels
order = neopixel.GRB # The order of the pixel colors (RGBW or GRBW)
level = 1.0
pixels = neopixel.NeoPixel(pin, num, brightness=level, auto_write=False, pixel_order=order)
   
# Main Function
# Ask user to cyle colors
while True:
    try:
        loopColors = int(input("Cyle through colors (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if loopColors < 0 or loopColors > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# If not cycling colors ask for color value
if loopColors == 0:
    while True:
        try:         
            selectColor = int(input("Enter Desired Colors (Green = 1, Red = 2, Blue = 3, White = 4): "))
        except ValueError:
            print("Invalid Entry. Try again")
            continue
        if loopColors < 0 or loopColors > 4:
            print("Invalid Entry. Try again")
            continue
        else:
            break

# Ask user to cyle brightness levels
while True:
    try:
        loopLevels = int(input("Cyle through brightness levels (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if loopLevels < 0 or loopLevels > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# If not cycling brightness ask for brightness value
if loopLevels == 0:
    while True:
        try:         
            selectLevel = float(input("Enter Desired Brightness (Min = 0, Max = 1): "))
        except ValueError:
            print("Invalid Entry. Try again")
            continue
        if selectLevel < 0 or selectLevel > 1:
            print("Invalid Entry. Try again")
            continue
        else:
            break

# Ask user for LED on time
while True:
    try:
        onTime = int(input("Set LED On Time (secs): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if onTime < 0:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# Ask user to save images
while True:
    try:
        saveImages = int(input("Save Images (Yes = 1, No = 0): "))
    except ValueError:
        print("Invalid Entry. Try again")
        continue
    if saveImages < 0 or saveImages > 1:
        print("Invalid Entry. Try again")
        continue
    else:
        break

# Ask User for Experiment Name
if saveImages:
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

# Set Color Value
if loopColors:
    print("Looping through colors: RGBW")
    for ii in range(1,5):
        if ii == 1:
            color = (255,0,0)
            colorStr = "Green"
            print("Starting: Green")
        elif ii == 2:
            color = (0,255,0)
            colorStr = "Red"
            print("Starting: Red")
        elif ii == 3:
            color = (0,0,255)
            colorStr = "Blue"
            print("Starting: Blue")
        else:
            color = (255,255,255)
            colorStr = "White"
            print("Starting: White")

        if loopLevels:
            print("Looping through brightness levels")
            for jj in range(0,11,1):
                print("Brightness: ",jj/10)
                pixels.fill(color)
                pixels.brightness = jj/10
                pixels.show()
                time.sleep(onTime)
                if saveImages:
                    save_image(expName,colorStr,jj/10)
        else:
            pixels.fill(color)
            pixels.brightness = selectLevel
            pixels.show()
            time.sleep(onTime)
            if saveImages:
                save_image(expName,colorStr,selectLevel)
else:
    if selectColor == 1:
        color = (255,0,0)
        colorStr = "Green"
    elif selectColor == 2:
        color = (0,255,0)
        colorStr = "Red"
    elif selectColor == 3:
        color = (0,0,255)
        colorStr = "Blue"
    else:
        color = (255,255,255)
        colorStr = "White"
    
    if loopLevels:
        for jj in range(0,11,1):
            pixels.fill(color)
            pixels.brightness = jj/10
            pixels.show()
            time.sleep(onTime)
            if saveImages:
                save_image(expName,colorStr,jj/10)
    else:
        pixels.fill(color)
        pixels.brightness = selectLevel
        pixels.show()
        time.sleep(onTime)
        if saveImages:
            save_image(expName,colorStr,selectLevel)

# Turn off Leds
pixels.fill((0,0,0))
pixels.show()

if saveImages:
    imgPath = "/home/pi/Pictures/" + expName + "/"
    subprocess.run(["chown","-R","pi",imgPath])
