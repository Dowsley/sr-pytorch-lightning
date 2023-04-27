from skimage.metrics import structural_similarity as calculate_ssim
from skimage.metrics import peak_signal_noise_ratio as calculate_psnr
import cv2
import numpy as np
from os import listdir
from statistics import mean

original_folder_prefix = 'G10_original'
sr_folder_prefix = 'G10_sr_from_x4_wrong_model_only_bicubic'
length = len(listdir(original_folder_prefix))

ssim_scores = []
psnr_scores = []
for i in range(length):
    before = cv2.imread(f'{original_folder_prefix}/test_img_{i:03}.jpg')
    after = cv2.imread(f'{sr_folder_prefix}/test_img_{i:03}.png')

    # Convert images to grayscale
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between two images
    (ssim_score, ssim_diff) = calculate_ssim(before_gray, after_gray, full=True)
    ssim_scores.append(ssim_score)
    psnr_score = calculate_psnr(before_gray, after_gray)
    psnr_scores.append(psnr_score)

print(f"Mean SSIM Score: {mean(ssim_scores)}")
print(f"Mean PSNR Score: {mean(psnr_scores)}")