import numpy as np

def rle2mask(rle_string, height, width):
    if rle_string == '':
        return np.zeros((height, width), dtype=np.uint8)

    s = np.asarray(rle_string.strip().split(), dtype=int)
    starts, lengths = s[::2], s[1::2]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(height * width, dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape((height, width), order='F')


def mask2rle(mask):
    pixels = mask.T.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)
