import argparse
from skimage.metrics import structural_similarity as calculate_ssim
from skimage.metrics import peak_signal_noise_ratio as calculate_psnr
import cv2
import numpy as np
from os import listdir
from statistics import mean

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate image quality.')
    parser.add_argument('--datasets_dir', type=str)
    parser.add_argument('--default_root_dir', type=str) 
    parser.add_argument('--predict_datasets', type=str) 

    args = parser.parse_args()

    length = len(listdir(f'{args.datasets_dir}/{args.predict_datasets}'))

    ssim_scores = []
    psnr_scores = []
    for i in range(length):
        before = cv2.imread(f'{args.datasets_dir}/{args.predict_datasets}/test_img_{i:03}.jpg')
        after = cv2.imread(f'{args.default_root_dir}/{args.predict_datasets}/test_img_{i:03}.png')

        # Convert images to grayscale
        # before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
        # after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

        # Compute SSIM between two images
        (ssim_score, ssim_diff) = calculate_ssim(before, after, channel_axis=2, full=True)
        ssim_scores.append(ssim_score)
        psnr_score = calculate_psnr(before, after)
        psnr_scores.append(psnr_score)

    print(sum(ssim_scores))
    print(sum(psnr_scores))