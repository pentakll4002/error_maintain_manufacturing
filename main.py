from mymodule.utilities import rle2mask, mask2rle
import numpy as np

# Fake mask for testing
mask = np.zeros((5, 5), dtype=np.uint8)
mask[1:4, 2] = 1  # vertical line in center

print("Original Mask:\n", mask)

rle = mask2rle(mask)
print("RLE string:", rle)

decoded_mask = rle2mask(rle, shape=(5, 5))
print("Decoded Mask:\n", decoded_mask)
