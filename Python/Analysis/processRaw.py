
import numpy as np
import cv2
import sys

import matplotlib.pyplot as plt
from matplotlib import image, projections, cm

fileName = 'D:\ImagingBox\Flatness\Color\Flatness_IMX519_FlexWhite\Flatness_IMX519_FlexWhite_both_Blue.raw'
#fileName = 'D:\ImagingBox\Flatness\Color\Flatness_IMX519_FlexWhite\Flatness_IMX519_FlexWhite_both_Green.raw'
#fileName = 'D:\ImagingBox\Flatness\Color\Flatness_IMX519_FlexWhite\Flatness_IMX519_FlexWhite_both_Red.raw'
#fileName = 'D:\ImagingBox\Flatness\Color\Flatness_IMX519_FlexWhite\Flatness_IMX519_FlexWhite_both_White.raw'

# Raw stream: 4656x3496 stride 5824 format SBGGR10_CSI2P
width = 4656
height = 3496
stride = 5824

# Color Conversion Notes:
# COLOR_Bayer_BG2BGR     equivalent to RGGB Bayer pattern
# COLOR_Bayer_GB2BGR     equivalent to GRBG Bayer pattern
# COLOR_Bayer_RG2BGR     equivalent to BGGR Bayer pattern
# COLOR_Bayer_GR2BGR     equivalent to GBRG Bayer pattern
bayer = cv2.COLOR_BAYER_RG2BGR

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

# Main Code
fin = open(fileName,mode='rb')
data = fin.read()
fin.close()

raw = unpack_mipi_raw10(remove_padding(data,width,height,10)).reshape(height,width,1)
raw = raw >> 2
raw = raw.astype(np.uint8)
img = cv2.cvtColor(raw,bayer)
img2 = cv2.resize(img,(1920,1080))

# cv2.imshow('Raw Image: Blue LED, Both',raw)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imshow('Test',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Blue Channel
# cv2.imshow('Test',img2[:,:,0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Green Channel
# cv2.imshow('Test',img2[:,:,1])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Red Channel
# cv2.imshow('Test',img2[:,:,2])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
