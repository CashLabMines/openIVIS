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
import time
import datetime
import subprocess

# Function to save images
def saveImage(expName,color):
    #print('Saving image ...')
    imgPath = "/home/pi/Pictures/" + expName + "/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
 
    baseExp = 1000
    scale = [250,500,1000]
    
    for ii in scale:
        expValue = baseExp*ii
        exp = str(expValue)
        expStr = str(int(expValue/1000))
    
        imgName = imgPath + expName + "_" + color + "_" + expStr + "ms" + ".png"
        print(imgName)
        subprocess.run(["libcamera-still","--autofocus-mode=auto","--autofocus-on-capture=1","--vflip","--hflip","-n","--shutter",exp,"-e","png","-o",imgName])
        
        imgName = imgPath + expName + "_" + color + "_" + expStr + "ms" + ".dng"
        print(imgName)
        subprocess.run(["libcamera-still","--autofocus-mode=auto","--autofocus-on-capture=1","--vflip","--hflip","-n","--raw","1","--shutter",exp,"-o",imgName])
        
        imgName = imgPath + expName + "_" + color + "_" + expStr + "ms" + ".raw"
        print(imgName)
        subprocess.run(["libcamera-raw","--autofocus-mode=auto","--autofocus-on-capture=1","--vflip","--hflip","--gain","1","--awbgains","1,1","--shutter",exp,"-o",imgName])
    
    subprocess.run(["chown","-R","pi",imgPath])

def timeImage(expName):
    #print('Saving image ...')
    imgPath = "/home/pi/Pictures/" + expName + "/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
    execStr = datetime.datetime.now()
    execMonth = execStr.strftime("%Y")+execStr.strftime("%m")+execStr.strftime("%d")
    execTime = execStr.strftime("%H")+execStr.strftime("%M")+execStr.strftime("%S")
    imgName = imgPath + expName + "_" + execMonth + "_" + execTime + ".png"
    subprocess.run(["libcamera-still","-e","png","--autofocus-mode=auto","--autofocus-on-capture=1","","-o",imgName])
    
    subprocess.run(["chown","-R","pi",imgPath])

def calibrationImages(expName,color):
    #print('Saving image ...')
    imgPath = "/home/pi/Pictures/" + expName + "/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
 
    baseExp = 1000
    scale = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,100,200,300,400,500,600,700,800,900,1000]
    
    for ii in scale:
        expValue = baseExp*ii
        exp = str(expValue)
        expStr = str(int(expValue/1000))
    
        imgName = imgPath + expName + "_" + color + "_" + expStr + "ms" + ".png"
        print(imgName)
        subprocess.run(["libcamera-still","--autofocus-mode=auto","--autofocus-on-capture=1","--vflip","--hflip","-n","--shutter",exp,"-e","png","-o",imgName])
        
        imgName = imgPath + expName + "_" + color + "_" + expStr + "ms" + ".dng"
        print(imgName)
        subprocess.run(["libcamera-still","--autofocus-mode=auto","--autofocus-on-capture=1","--vflip","--hflip","-n","--raw","1","--shutter",exp,"-o",imgName])
        
        imgName = imgPath + expName + "_" + color + "_" + expStr + "ms" + ".raw"
        print(imgName)
        subprocess.run(["libcamera-raw","--autofocus-mode=auto","--autofocus-on-capture=1","--vflip","--hflip","--gain","1","--awbgains","1,1","--shutter",exp,"-o",imgName])
    
    subprocess.run(["chown","-R","pi",imgPath])

def multipleImages(expName,color):
    #print('Saving image ...')
    imgPath = "/home/pi/Pictures/" + expName + "/"
    dirExists = os.path.exists(imgPath)
    if dirExists:
        print("Output Directory: ",imgPath)
    else:
        print("Creating Output Directory ...")
        subprocess.run(["mkdir",imgPath])
        print(["Output Directory: ",imgPath])
    
    for ii in range(1,100):
        execStr = datetime.datetime.now()
        execMonth = execStr.strftime("%Y")+execStr.strftime("%m")+execStr.strftime("%d")
        execTime = execStr.strftime("%H")+execStr.strftime("%M")+execStr.strftime("%S")
        imgName = imgPath + expName + "_" + color + "_" + execMonth + "_" + execTime + ".png"
        subprocess.run(["libcamera-still","-n","-e","png","--autofocus-mode=auto","--autofocus-on-capture=1","-o",imgName])
    
    subprocess.run(["chown","-R","pi",imgPath])
