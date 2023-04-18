import cv2
import matplotlib.pyplot as plt
import sys
import h5py

from salt_pepper import salt_and_pepper

def downsample(img, factor):
    scale_percent = 100 / factor
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized2x = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    
    return resized2x
    blur2x = cv2.GaussianBlur(resized2x,(5,5),0)
    sp2x = salt_and_pepper(resized2x)

normal_h5 = 'Galaxy10_DECals.h5'
downscaled_h5 = 'Galaxy10_DECals_downscaled.h5'

LENGTH = 100
FACTOR = 4
ORIGINAL_IMG_SHAPE = (LENGTH, 256, 256, 3)
NEW_IMG_SHAPE = (LENGTH, 256 * (100 / FACTOR) / 100, 256 * (100 / FACTOR) / 100, 3)


with h5py.File(normal_h5,'r') as f:
    for i in range(f['images'].shape[0]):
        if i >= LENGTH:
            break
        img_arr = f['images'][i,:]   # slice notation gets [i,:,:,:]
        cv2.imwrite(f'downscaled_g10/test_img_{i:03}.jpg',img_arr)
        
        print(i)