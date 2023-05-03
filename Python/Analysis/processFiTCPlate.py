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

filePath = 'E:/openIVIS/Analysis/FITC/FITC_FullPlate_Trial1/'
outputDir = 'E:/openIVIS/Analysis/Results/FITC/FITC_FullPlate_Trial1/'

def absolute_file_paths(directory):
    path = os.path.abspath(directory)
    return [entry.path for entry in os.scandir(path) if entry.is_file()]

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

idx1 = 180
idx2 = 390
idx3 = 600
idx4 = 800
idx5 = 1000
idx6 = 1200
idx7 = 1410
idx8 = 1610

dis = 30

gridWidth = chipR - chipL + 1
gridHeight = chipB - chipT + 1
gridXmajor = np.arange(0,gridWidth,100,dtype=int)
gridXminor = np.arange(0,gridWidth,50,dtype=int)
gridYmajor = np.arange(0,gridHeight,100,dtype=int)
gridYminor = np.arange(0,gridHeight,50,dtype=int)

arraySize = 24
results = np.zeros((chipR-chipL,len(fileList)*arraySize))

blockImage = False
plotImage = True
analyzeData = True
plotResults = True
saveImages = True


if analyzeData:
    checkDir(outputDir)

for ff in range(8,12):#range(0,len(fileList)):
    fileName = fileList[ff]
    status = str(ff) + ' of ' + str(len(fileList)-1) + ': ' + fileName
    print(status)

    # Get image information
    idx = findIdx(fileName,'_') # Underscores
    edx = findIdx(fileName,'.') # Extension separator
    last = len(idx)

    runStr = fileName[idx[6]-1]
    durStr = fileName[idx[7]+1:edx[0]]
    typeStr = fileName[edx[0]+1:len(fileName)]

    img = importImage(fileName,typeStr)
    chip = img[chipT:chipB,chipL:chipR,:]

    if plotImage:
        plt.imshow(img)
        plt.show()
        plt.close('all')

    if plotImage:
        fig = plt.figure()
        ax = plt.axes()
        plt.imshow(chip)
        plt.minorticks_on()
        ax.set_xticks(gridXmajor)
        ax.set_xticks(gridXminor,minor=True)
        ax.set_yticks(gridYmajor)
        ax.set_yticks(gridYminor,minor=True)
        ax.xaxis.grid(which = 'both', color = 'white', linestyle = '--', linewidth = 0.5)
        ax.yaxis.grid(which = 'both', color = 'white', linestyle = '--', linewidth = 0.5)
        plt.show()
        plt.close('all')
    
    if analyzeData:
        data1 = chip[idx1-dis:idx1+dis,:,:]
        data2 = chip[idx2-dis:idx2+dis,:,:]
        data3 = chip[idx3-dis:idx3+dis,:,:]
        data4 = chip[idx4-dis:idx4+dis,:,:]
        data5 = chip[idx5-dis:idx5+dis,:,:]
        data6 = chip[idx6-dis:idx6+dis,:,:]
        data7 = chip[idx7-dis:idx7+dis,:,:]
        data8 = chip[idx8-dis:idx8+dis,:,:]

        meanData1R = np.mean(data1[:,:,0],axis=0)
        meanData1G = np.mean(data1[:,:,1],axis=0)
        meanData1B = np.mean(data1[:,:,2],axis=0)

        meanData2R = np.mean(data2[:,:,0],axis=0)
        meanData2G = np.mean(data2[:,:,1],axis=0)
        meanData2B = np.mean(data2[:,:,2],axis=0)

        meanData3R = np.mean(data3[:,:,0],axis=0)
        meanData3G = np.mean(data3[:,:,1],axis=0)
        meanData3B = np.mean(data3[:,:,2],axis=0)

        meanData4R = np.mean(data4[:,:,0],axis=0)
        meanData4G = np.mean(data4[:,:,1],axis=0)
        meanData4B = np.mean(data4[:,:,2],axis=0)

        meanData5R = np.mean(data5[:,:,0],axis=0)
        meanData5G = np.mean(data5[:,:,1],axis=0)
        meanData5B = np.mean(data5[:,:,2],axis=0)

        meanData6R = np.mean(data6[:,:,0],axis=0)
        meanData6G = np.mean(data6[:,:,1],axis=0)
        meanData6B = np.mean(data6[:,:,2],axis=0)

        meanData7R = np.mean(data7[:,:,0],axis=0)
        meanData7G = np.mean(data7[:,:,1],axis=0)
        meanData7B = np.mean(data7[:,:,2],axis=0)

        meanData8R = np.mean(data8[:,:,0],axis=0)
        meanData8G = np.mean(data8[:,:,1],axis=0)
        meanData8B = np.mean(data8[:,:,2],axis=0)

        results = np.transpose([meanData1R,meanData2R,meanData3R,meanData4R,meanData5R,meanData6R,meanData7R,meanData8R,
            meanData1G,meanData2G,meanData3G,meanData4G,meanData5G,meanData6G,meanData7G,meanData8G,
            meanData1B,meanData2B,meanData3B,meanData4B,meanData5B,meanData6B,meanData7B,meanData8B])

        if plotResults:
            gridXmajor = np.arange(0,gridWidth,100,dtype=int)
            gridXminor = np.arange(0,gridWidth,50,dtype=int)
            gridYmajor = np.arange(0,257,32,dtype=int)
            gridYminor = np.arange(0,257,8,dtype=int)

            titleStr = 'FITC Flourescence: ' + ', Duration: ' + durStr + ', Type: ' + typeStr + 'Channel: Red' + ', Run: ' + runStr
            imageStr = 'FITC_Flourescence_' + durStr + '_' + typeStr + '_RedChan' + '_Run' + runStr + '.png'

            fig = plt.figure(figsize=(figWidth,figWidth/aspect))
            ax = plt.axes()
            plt.plot(meanData1R)
            plt.plot(meanData2R)
            plt.plot(meanData3R)
            plt.plot(meanData4R)
            plt.plot(meanData5R)
            plt.plot(meanData6R)
            plt.plot(meanData7R)
            plt.plot(meanData8R)
            plt.title(titleStr)
            plt.xlabel('Well position (pixel)')
            plt.ylabel('Fluorescence (a.u.)')
            #plt.legend(['Row 1','Row 2','Row 3','Row 4','Row 5','Row 6','Row 7','Row 8'])
            plt.minorticks_on()
            ax.set_xticks(gridXmajor)
            ax.set_xticks(gridXminor,minor=True)
            ax.set_yticks(gridYmajor)
            ax.xaxis.grid(which = 'both', color = 'black', linestyle = '--', linewidth = 0.5)
            ax.yaxis.grid(which = 'major', color = 'black', linestyle = '--', linewidth = 0.5)
            if saveImages:
                outImage= outputDir + imageStr
                plt.savefig(outImage)
            plt.show(block=blockImage)
            plt.close('all')

            titleStr = 'FITC Flourescence: ' + ', Duration: ' + durStr + ', Type: ' + typeStr + 'Channel: Green' + ', Run: ' + runStr
            imageStr = 'FITC_Flourescence_' + durStr + '_' + typeStr + '_GreenChan' + '_Run' + runStr + '.png'

            fig = plt.figure(figsize=(figWidth,figWidth/aspect))
            ax = plt.axes()
            plt.plot(meanData1G)
            plt.plot(meanData2G)
            plt.plot(meanData3G)
            plt.plot(meanData4G)
            plt.plot(meanData5G)
            plt.plot(meanData6G)
            plt.plot(meanData7G)
            plt.plot(meanData8G)
            plt.title(titleStr)
            plt.xlabel('Well position (pixel)')
            plt.ylabel('Fluorescence (a.u.)')
            #plt.legend(['Row 1','Row 2','Row 3','Row 4','Row 5','Row 6','Row 7','Row 8'])
            plt.minorticks_on()
            ax.set_xticks(gridXmajor)
            ax.set_xticks(gridXminor,minor=True)
            ax.set_yticks(gridYmajor)
            ax.xaxis.grid(which = 'both', color = 'gray', linestyle = '--', linewidth = 0.5)
            ax.yaxis.grid(which = 'major', color = 'gray', linestyle = '--', linewidth = 0.5)
            if saveImages:
                outImage= outputDir + imageStr
                plt.savefig(outImage)
            plt.show(block=blockImage)
            plt.close('all')

            titleStr = 'FITC Flourescence: ' + ', Duration: ' + durStr + ', Type: ' + typeStr + 'Channel: Blue' + ', Run: ' + runStr
            imageStr = 'FITC_Flourescence_' + durStr + '_' + typeStr + '_BlueChan' + '_Run' + runStr + '.png'

            fig = plt.figure(figsize=(figWidth,figWidth/aspect))
            ax = plt.axes()
            plt.plot(meanData1B)
            plt.plot(meanData2B)
            plt.plot(meanData3B)
            plt.plot(meanData4B)
            plt.plot(meanData5B)
            plt.plot(meanData6B)
            plt.plot(meanData7B)
            plt.plot(meanData8B)
            plt.title(titleStr)
            plt.xlabel('Well position (pixel)')
            plt.ylabel('Fluorescence (a.u.)')
            #plt.legend(['Row 1','Row 2','Row 3','Row 4','Row 5','Row 6','Row 7','Row 8'])
            plt.minorticks_on()
            ax.set_xticks(gridXmajor)
            ax.set_xticks(gridXminor,minor=True)
            ax.set_yticks(gridYmajor)
            ax.xaxis.grid(which = 'both', color = 'gray', linestyle = '--', linewidth = 0.5)
            ax.yaxis.grid(which = 'major', color = 'gray', linestyle = '--', linewidth = 0.5)
            if saveImages:
                outImage= outputDir + imageStr
                plt.savefig(outImage)
            plt.show(block=blockImage)
            plt.close('all')

        outData = outputDir + 'FITC_Sensitivity_' + durStr + '_' + typeStr + '_Run' + runStr + '_Profile.csv'
        np.savetxt(outData,results,delimiter=',')

        window = np.ones(20)/20
        meanData = np.zeros((chipR-chipL,arraySize))
        for ii in range(0,arraySize):
            meanData[:,ii] = np.convolve(results[:,ii],window,mode='same')
        outData = outputDir + 'FITC_Sensitivity_' + durStr + '_' + typeStr + '_Run' + runStr + '_Profile_Mean20.csv'
        np.savetxt(outData,meanData,delimiter=',')

        window = np.ones(50)/50
        meanData = np.zeros((chipR-chipL,arraySize))
        for ii in range(0,arraySize):
            meanData[:,ii] = np.convolve(results[:,ii],window,mode='same')
        outData = outputDir + 'FITC_Sensitivity_' + durStr + '_' + typeStr + '_Run' + runStr + '_Profile_Mean50.csv'
        np.savetxt(outData,meanData,delimiter=',')


    
