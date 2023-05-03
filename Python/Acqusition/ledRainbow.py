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

# Loop through random colors on each LED
import time
import board
import neopixel
from random import getrandbits
from random import randint

# Pixel Variable
ledPin = board.D18          # Data in pin of the NeoPixel strip
ledNum = 8                  # Number of NeoPixels
ledOrder = neopixel.RGB     # Order of the pixel colors (RGBW or GRBW)
ledLevel = 1.0              # LED Brightness level
ledTime = 2.0               # LED time delay
pixels = neopixel.NeoPixel(ledPin, ledNum, brightness=ledLevel, auto_write=False, pixel_order=ledOrder)

# Rainbow time delay
rainbowDelay = 0.001

def wheel(pos):
	# Input a value 0 to 255 to get a color value.
	# The colours are a transition r - g - b - back to r.
	if pos < 0 or pos > 255:
		r = g = b = 0
	elif pos < 85:
		r = int(pos * 3)
		g = int(255 - pos * 3)
		b = 0
	elif pos < 170:
		pos -= 85
		r = int(255 - pos * 3)
		g = 0
		b = int(pos * 3)
	else:
		pos -= 170
		r = 0
		g = int(pos * 3)
		b = int(255 - pos * 3)
	return (r, g, b) if ledOrder in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
	
def rainbow_cycle(wait):
	for k in range(10):
		lvl = randint(1,10)
		for j in range(255):
			for i in range(ledNum):
				pixelIDX = (i * 256 // ledNum) + j
				pixels[i] = wheel(pixelIDX & 255)
			pixels.show()
			time.sleep(wait)

try:
	while True:
		rainbow_cycle(rainbowDelay)

except KeyboardInterrupt as e:
    print( "Exception:", e )
    # Turn off all the lights
    for i in range(ledNum):
        pixels[i] = (0, 0, 0)
    pixels.write()
	    	
