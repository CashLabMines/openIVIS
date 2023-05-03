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

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Pixel Variable
ledPin = board.D18          # Data in pin of the NeoPixel strip
ledNum = 8                  # Number of NeoPixels
ledOrder = neopixel.RGB     # Order of the pixel colors (RGBW or GRBW)
ledLevel = 1.0              # LED Brightness level
ledTime = 2.0               # LED time delay
pixels = neopixel.NeoPixel(ledPin, ledNum, brightness=ledLevel, auto_write=False, pixel_order=ledOrder)

# Turn off Leds
pixels.fill((0,0,0))
pixels.show()
time.sleep(ledTime)

while True:
    # White
    pixels.fill((255,255,255))
    pixels.brightness = 1.0
    pixels.show()
    time.sleep(ledTime)
    
    # Red
    pixels.fill((255, 0, 0))
    pixels.brightness = 1.0
    pixels.show()
    time.sleep(ledTime)

    # Green
    pixels.fill((0, 255, 0))
    pixels.brightness = 1.0
    pixels.show()
    time.sleep(ledTime)

    # Blue
    pixels.fill((0, 0, 255))
    pixels.brightness = 1.0
    pixels.show()
    time.sleep(ledTime)




