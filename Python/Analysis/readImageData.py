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

import numpy as np
import cv2
import rawpy
import imageio

# Raw stream: 4656x3496 stride 5824 format SBGGR10_CSI2P
width = 4656
height = 3496
stride = 5824

# Color Conversion Notes:
# COLOR_Bayer_BG2BGR     equivalent to RGGB Bayer pattern
# COLOR_Bayer_GB2BGR     equivalent to GRBG Bayer pattern
# COLOR_Bayer_RG2BGR     equivalent to BGGR Bayer pattern
# COLOR_Bayer_GR2BGR     equivalent to GBRG Bayer pattern
#bayer = cv2.COLOR_BAYER_RG2BGR
bayer = cv2.COLOR_BAYER_RG2RGB

def unpack_mipi_raw10(byte_buf):
    data = np.frombuffer(byte_buf, dtype=np.uint8)
    # 5 bytes contain 4 10-bit pixels (5x8 == 4x10)
    b1, b2, b3, b4, b5 = np.reshape(data, (data.shape[0]//5, 5)).astype(np.uint16).T
    o1 = (b1 << 2) + ((b5) & 0x3)
    o2 = (b2 << 2) + ((b5 >> 2) & 0x3)
    o3 = (b3 << 2) + ((b5 >> 4) & 0x3)
    o4 = (b4 << 2) + ((b5 >> 6) & 0x3)
    unpacked = np.reshape(np.concatenate(
        (o1[:, None], o2[:, None], o3[:, None], o4[:, None]), axis=1),  4*o1.shape[0])
    return unpacked

def align_down(size, align):
    return (size & ~((align)-1))

def align_up(size, align):
    return align_down(size + align - 1, align)

def remove_padding(data, width, height, bit_width):
    buff = np.frombuffer(data, np.uint8)
    real_width = int(width / 8 * bit_width)
    align_width = align_up(real_width, 32)
    align_height = align_up(height, 16)

    buff = buff.reshape(-1,align_width)
    buff = buff[:height, :real_width]
    buff = buff.reshape(height * real_width)
    return buff

def importImage(fileName,imgType):
    if imgType == 'png':
        img = imageio.imread(fileName)
        img = np.asarray(img)
        
    elif imgType == 'dng':
        img = rawpy.imread(fileName)
        #img = img.postprocess(four_color_rgb=False)
        img = img.postprocess(demosaic_algorithm=rawpy.DemosaicAlgorithm.AAHD,
            four_color_rgb=True,use_camera_wb=False,use_auto_wb=True,output_color=rawpy.ColorSpace.sRGB,
            no_auto_bright=True)#,gamma=(2.222, 4.5))


    elif imgType == 'raw':
        fin = open(fileName,mode='rb')
        data = fin.read()
        fin.close()

        raw = unpack_mipi_raw10(remove_padding(data,width,height,10)).reshape(height,width,1)
        raw = raw >> 2
        raw = raw.astype(np.uint8)
        img = cv2.cvtColor(raw,bayer)
    
    else:
        img = np.zeros(width,height)
    
    return img


        