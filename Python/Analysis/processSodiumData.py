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
from readImageData import importImage
import cv2

filePath = 'E:/openIVIS/Analysis/Sodium/Plate1_LP645/'
outputDir = 'E:/openIVIS/Analysis/Results/Sodium/Plate1_LP645/'
outFileName = outputDir + 'Sodium_LP645_Plate1_Results.csv'

def absolute_file_paths(directory):
    path = os.path.abspath(directory)
    return [os.path.join(path, name) for path, subdirs, files in os.walk(path) for name in files]

def findIdx(str, ch):
    return [ii for ii, ltr in enumerate(str) if ltr == ch]

def checkDir(directory):
    path = os.path.abspath(directory)
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

# Get list of all files in analysis folder
fileList = absolute_file_paths(filePath)

# Raw stream: 4656x3496 stride 5824 format SBGGR10_CSI2P
width = 4656
height = 3496
aspect = width/height
figWidth = 12

chipL = 1000
chipR = 3600
chipT = 800
chipB = 2600

dis = 30
rdxValues = [680, 880, 1090, 1300]
cdxValues = [1050, 1250, 1455, 1660]
arraySize = len(rdxValues)*len(cdxValues)
channels = ['FileType','Ex (nm)','Filter (nm)','Plate','Run','Exp (ms)','Idx','Red','Green','Blue','Gray']
results = np.zeros((len(fileList),arraySize,len(channels)))

gridWidth = chipR - chipL + 1
gridHeight = chipB - chipT + 1
gridXmajor = np.arange(0,gridWidth,100,dtype=int)
gridXminor = np.arange(0,gridWidth,50,dtype=int)
gridYmajor = np.arange(0,gridHeight,100,dtype=int)
gridYminor = np.arange(0,gridHeight,50,dtype=int)

blockImage = False
plotImage = False
analyzeData = True
plotResults = True
saveImages = True
plotGrid = True

if analyzeData:
    checkDir(outputDir)

for ff in range(0,len(fileList)):
    fileName = fileList[ff]
    status = str(ff) + ' of ' + str(len(fileList)-1) + ': ' + fileName
    print(status)

    # Get image information
    idx = findIdx(fileName,'_') # Underscores
    edx = findIdx(fileName,'.') # Extension separator
    last = len(idx)

    # File Name Structure: Plate1_LP645\Plate1_LP645_Trial1_Red_100ms.png
    # idx position:              0            1     2      3   4
    plateStr = fileName[idx[2]-1]
    filterStr = fileName[idx[2]+3:idx[3]]
    runStr = fileName[idx[4]-1]
    colorStr = fileName[idx[4]+1:idx[5]]
    durStr = fileName[idx[5]+1:edx[0]-2]
    typeStr = fileName[edx[0]+1:len(fileName)]
    
    if colorStr == 'Red':
        excite = 630
    elif colorStr == 'Green':
        excite = 520
    else:
        excite = 465
    
    if typeStr == 'dng':
        typeVal = 1
    else:
        typeVal = 2

    img = importImage(fileName,typeStr)
    chip = img[chipT:chipB,chipL:chipR,:]
    grayChip = cv2.cvtColor(chip,cv2.COLOR_RGB2GRAY)

    if plotImage:
        fig = plt.figure()
        ax = plt.axes()
        plt.imshow(chip)
        plt.minorticks_on()
        if plotGrid:
            ax.set_xticks(gridXmajor)
            ax.set_xticks(gridXminor,minor=True)
            ax.set_yticks(gridYmajor)
            ax.set_yticks(gridYminor,minor=True)
            ax.xaxis.grid(which = 'both', color = 'white', linestyle = '--', linewidth = 0.5)
            ax.yaxis.grid(which = 'both', color = 'white', linestyle = '--', linewidth = 0.5)
        plt.show()
        plt.close('all')

    if plotImage:
        plt.imshow(grayChip,cmap=plt.get_cmap('gray'))
        plt.show()
        plt.close('all')
    
    if analyzeData:
        idx = 0
        for rr in rdxValues:
            for cc in cdxValues:
                data = chip[rr-dis:rr+dis,cc-dis:cc+dis,:]    
                grayData = grayChip[rr-dis:rr+dis,cc-dis:cc+dis]
                meanRed = np.mean(data[:,:,0])
                meanGreen = np.mean(data[:,:,1])
                meanBlue = np.mean(data[:,:,2])
                meanGray = np.mean(grayData)
                mResults = [int(typeVal),int(excite),int(filterStr),int(plateStr),int(runStr),int(durStr),idx,meanRed,meanGreen,meanBlue,meanGray]
                results[ff,idx,:] = mResults
                idx += 1

#outFileName = outputDir + 'Plate-' + plateStr + '_Run-' + runStr + '_Filter-' + filterStr +'_Results.csv'

outData = results.reshape(len(fileList)*arraySize,len(channels))
np.savetxt(outFileName,outData,delimiter=',')
