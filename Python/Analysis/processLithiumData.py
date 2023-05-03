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
from matplotlib.patches import Circle
from getAnalyteValue import getLogAnalyte, getLogAnalyteSwapped

filePath = 'E:/openIVIS/Analysis/Lithium/Li_ChVII_LP665_Plate1/'
outputDir = 'E:/openIVIS/Analysis/Results/Lithium/Li_ChVII_LP665_Plate1/'
outFileName = outputDir + 'Li_ChVII_LP665_Plate1_Results.csv'

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

chipL = 1000
chipR = 3600
chipT = 800
chipB = 2600

dis = 20
xValues = [900, 1100, 1300, 1500]
yValues = [720, 920, 1110, 1310]
arraySize = len(xValues)*len(yValues)
channels = ['FileType','Ex (nm)','Filter (nm)','Exp (ms)','Idx','LogA','Red','Green','Blue','Gray']
results = np.zeros((len(fileList),arraySize,len(channels)))

gridWidth = chipR - chipL + 1
gridHeight = chipB - chipT + 1
gridXmajor = np.arange(0,gridWidth,100,dtype=int)
gridXminor = np.arange(0,gridWidth,50,dtype=int)
gridYmajor = np.arange(0,gridHeight,100,dtype=int)
gridYminor = np.arange(0,gridHeight,50,dtype=int)

startImg = 0
stopImg = len(fileList)
startImg = 28
stopImg = 29
debugInfo = True

for ff in range(startImg,stopImg):
    fileName = fileList[ff]
    status = str(ff) + ' of ' + str(len(fileList)-1) + ': ' + fileName
    print(status)

    if (stopImg - startImg) > 2:
        plotImage = False
    else:
        plotImage = True

    # Get image information
    idx = findIdx(fileName,'_') # Underscores
    edx = findIdx(fileName,'.') # Extension separator
    last = len(idx)

    # File Name Structure:  \Li_ChVII_LP665_Plate1\Li_ChVII_LP665_Plate1_Blue_1ms.dng
    # idx position:            0    1     2         3    4     5      6    7   
    filterStr = fileName[idx[1]+3:idx[2]]
    colorStr = fileName[idx[6]+1:idx[7]]
    durStr = fileName[idx[7]+1:edx[0]-2]
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
        #plt.minorticks_on()
        #ax.set_xticks(gridXmajor)
        #ax.set_xticks(gridXminor,minor=True)
        #ax.set_yticks(gridYmajor)
        #ax.set_yticks(gridYminor,minor=True)
        #ax.xaxis.grid(which = 'both', color = 'white', linestyle = '--', linewidth = 0.5)
        #ax.yaxis.grid(which = 'both', color = 'white', linestyle = '--', linewidth = 0.5)

        if debugInfo:
            for xx in xValues:
                for yy in yValues:
                    circ = Circle((xx,yy),25)
                    ax.add_patch(circ)

        plt.show()
        plt.close('all')

    idx = 0
    for yy in yValues:
        for xx in xValues:
            #data = chip[rr-dis:rr+dis,cc-dis:cc+dis,:]
            #grayData = grayChip[rr-dis:rr+dis,cc-dis:cc+dis]
            data = chip[yy-dis:yy+dis,xx-dis:xx+dis,:]
            grayData = grayChip[yy-dis:yy+dis,xx-dis:xx+dis]
            meanRed = np.mean(data[:,:,0])
            meanGreen = np.mean(data[:,:,1])
            meanBlue = np.mean(data[:,:,2])
            meanGray = np.mean(grayData)
            #logA = getLogAnalyte(idx)
            logA = getLogAnalyteSwapped(idx)
            mResults = [int(typeVal),int(excite),int(filterStr),int(durStr),idx,logA,meanRed,meanGreen,meanBlue,meanGray]
            if debugInfo:
                print(xx,yy,idx,logA,meanRed,meanGreen,meanBlue,meanGray)
            results[ff,idx,:] = mResults
            idx += 1

checkDir(outputDir)
outData = results.reshape(len(fileList)*arraySize,len(channels))
np.savetxt(outFileName,outData,delimiter=',')
