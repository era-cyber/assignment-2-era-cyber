from dip import *

class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """ Computes the histogram of the input image """
        hist = [0]*256
        height, width = image.shape

        for i in range(height):
            for j in range(width):
                intensity = image[i, j]
                hist[intensity] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """ Find the optimal threshold using Otsu's method """
        total = sum(hist)
        sum_total = 0
        for t in range(256):
            sum_total += t * hist[t]

        sumB = 0
        wB = 0
        max_var_between = 0
        threshold = 0

        for t in range(256):
            wB += hist[t]           # Weight Background
            if wB == 0:
                continue

            wF = total - wB         # Weight Foreground
            if wF == 0:
                break

            sumB += t * hist[t]

            mB = sumB / wB          # Mean Background
            mF = (sum_total - sumB) / wF  # Mean Foreground

            # Between Class Variance
            var_between = wB * wF * (mB - mF) * (mB - mF)

            if var_between > max_var_between:
                max_var_between = var_between
                threshold = t

        return threshold

    def binarize(self, image, threshold):
        """ Binarizes image: pixels ≤ threshold -> 0 (black), others -> 255 (white) """
        height, width = image.shape
        bin_img = image.copy()

        for i in range(height):
            for j in range(width):
                if image[i, j] <= threshold:
                    bin_img[i, j] = 0
                else:
                    bin_img[i, j] = 255

        return bin_img




