
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

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from readImageData import importImage

outputDir = 'E:/penIVIS/Analysis/USAF_Target/'
filePath = 'E:/openIVIS/Analysis/USAF_Target/'

def absolute_file_paths(directory):
    path = os.path.abspath(directory)
    return [entry.path for entry in os.scandir(path) if entry.is_file()]

def findIdx(str, ch):
    return [ii for ii, ltr in enumerate(str) if ltr == ch]

# Check whether the output path exists or not
isExist = os.path.exists(outputDir)
if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(outputDir)

# Get list of all files in analysis folder
fileList = absolute_file_paths(filePath)

for ff in range(0,len(fileList)):
    fileName = fileList[ff]
    status = str(ff) + ' of ' + str(len(fileList)-1) + ': ' + fileName
    print(status)

    # Get image information
    idx = findIdx(fileName,'_') # Underscores
    edx = findIdx(fileName,'.') # Extension separator
    last = len(idx)

    typeStr = fileName[edx[0]+1:len(fileName)]

    img = importImage(fileName,typeStr)
    plt.imshow(img)
    plt.show()
    plt.close('all')
