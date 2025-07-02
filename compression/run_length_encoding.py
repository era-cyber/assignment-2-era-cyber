from dip import *  # for zeros, uint8, etc.

class Rle:
    def __init__(self):
        pass

    def encode_image(self, binary_image):
        """
        Encode binary image using run-length encoding
        input: binary_image (2D numpy array, values 0 or 255)
        returns: list of (pixel_value, run_length) tuples
        """

        # Flatten image row-wise
        flat = binary_image.flatten()
        rle_code = []

        prev_pixel = flat[0]
        count = 1

        for pixel in flat[1:]:
            if pixel == prev_pixel:
                count += 1
            else:
                rle_code.append((prev_pixel, count))
                prev_pixel = pixel
                count = 1

        # Add the last run
        rle_code.append((prev_pixel, count))
        return rle_code

    def decode_image(self, rle_code, height, width):
        """
        Decode RLE code back into binary image
        input: rle_code (list of tuples), height, width
        returns: binary image numpy array (2D uint8)
        """

        pixels = []
        for (pixel_val, run_length) in rle_code:
            pixels.extend([pixel_val] * run_length)

        # Convert list back to numpy array and reshape
        img_array = array(pixels, dtype=uint8).reshape((height, width))
        return img_array





