from dip import *

class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """ Computes the histogram of the input image
        takes as input:
        image: a greyscale image
        returns a histogram as a list """

        hist = [0]*256

        return hist

    def find_otsu_threshold(self, hist):
        """ Analyses a histogram to find the otsu's threshold assuming that the input histogram is bimodal
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold) """

        threshold = 0

        return threshold

    def binarize(self, image, threshold):
        """ Comptues the binary image of the input image based on histogram analysis and thresholding
        take as input
        image: a greyscale image
        threshold: the threshold used in binarization
        returns: a binary image """

        bin_img = image.copy()

        return bin_img


