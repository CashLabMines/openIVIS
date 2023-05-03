import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from readImageData import importImage

outputDir = 'E:/ImagingBox/Results/Sensitivity/'
filePath = 'E:/ImagingBox/Sensitivity/Analysis/'

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

# Raw stream: 4656x3496 stride 5824 format SBGGR10_CSI2P
width = 4656
height = 3496
aspect = width/height
figWidth = 12

chipL = 1100
chipR = 3450
chipT = 1300
chipB = 2500

idx1 = 85
idx2 = 280
idx3 = 870
idx4 = 1050

dis = 50

arraySize = 4*3
results = np.zeros((chipR-chipL,len(fileList)*arraySize))

analyzeData = True
plotImage = False
plotResults = True
blockImage = False
saveImages = True

for ff in range(0,len(fileList)):
    fileName = fileList[ff]
    status = str(ff) + ' of ' + str(len(fileList)-1) + ': ' + fileName
    print(status)

    # Get image information
    idx = findIdx(fileName,'_') # Underscores
    edx = findIdx(fileName,'.') # Extension separator
    last = len(idx)

    #      0       1       2    3
    #Sodium_PCRWell_LP570nm_Blue_800ms.dng
    plateStr = fileName[idx[0]+1:idx[1]]
    filterStr = fileName[idx[1]+1:idx[2]]
    durStr = fileName[idx[3]+1:edx[0]]
    typeStr = fileName[edx[0]+1:len(fileName)]

    img = importImage(fileName,typeStr)
    if plotImage:
        plt.imshow(img)
        plt.show()
        plt.close('all')

    chip = img[chipT:chipB,chipL:chipR,:]
    if plotImage:
        plt.imshow(chip)
        plt.show()
        plt.close('all')

    if analyzeData:
        data1 = chip[idx1-dis:idx1+dis,:,:]
        data2 = chip[idx2-dis:idx2+dis,:,:]
        data3 = chip[idx3-dis:idx3+dis,:,:]
        data4 = chip[idx4-dis:idx4+dis,:,:]

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

        results = np.transpose([meanData1R,meanData2R,meanData3R,meanData4R,meanData1G,meanData2G,meanData3G,meanData4G,meanData1B,meanData2B,meanData3B,meanData4B])

        if plotResults:
            titleStr = 'Na Flourescence: ' + plateStr + ', Duration: ' + durStr + ', Type: ' + typeStr + ', Filter: ' + filterStr
            imageStr = 'NA_Flourescence_' + plateStr + '_' + durStr + '_' + typeStr + '_' + filterStr + '.png'

            plt.figure(figsize=(figWidth,figWidth/aspect))
            plt.plot(meanData1R,color='red')
            plt.plot(meanData2R,color='red')
            plt.plot(meanData3R,color='red')
            plt.plot(meanData4R,color='red')
            plt.plot(meanData1G,color='green')
            plt.plot(meanData2G,color='green')
            plt.plot(meanData3G,color='green')
            plt.plot(meanData4G,color='green')
            plt.plot(meanData1B,color='blue')
            plt.plot(meanData2B,color='blue')
            plt.plot(meanData3B,color='blue')
            plt.plot(meanData4B,color='blue')
            plt.xlabel('Well position (pixel)')
            plt.ylabel('Fluorescence (a.u.)')
            plt.grid(color='gray',linestyle='dashed')
            if saveImages:
                outImage= outputDir + imageStr
                plt.savefig(outImage)
            plt.show(block=blockImage)
            plt.close('all')

        outData = outputDir + 'Sensitivity_' + plateStr + '_' + durStr + '_' + typeStr + '_' + filterStr + '_Profile.csv'
        print(outData)
        np.savetxt(outData,results,delimiter=',')

        window = np.ones(20)/20
        meanData = np.zeros((chipR-chipL,arraySize))
        for ii in range(0,arraySize):
            meanData[:,ii] = np.convolve(results[:,ii],window,mode='same')
        outData = outputDir + 'Sensitivity_' + plateStr + '_' + durStr + '_' + typeStr + '_' + filterStr + '_Profile_Mean20.csv'
        np.savetxt(outData,meanData,delimiter=',')

        window = np.ones(50)/50
        meanData = np.zeros((chipR-chipL,arraySize))
        for ii in range(0,arraySize):
            meanData[:,ii] = np.convolve(results[:,ii],window,mode='same')
        outData = outputDir + 'Sensitivity_' + plateStr + '_' + durStr + '_' + typeStr + '_' + filterStr + '_Profile_Mean50.csv'
        np.savetxt(outData,meanData,delimiter=',')