import argparse
from skimage.metrics import structural_similarity as calculate_ssim
from skimage.metrics import peak_signal_noise_ratio as calculate_psnr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate image quality.')
    parser.add_argument('--datasets_dir', type=str)
    parser.add_argument('--default_root_dir', type=str) 

    args = parser.parse_args()
    print(args)