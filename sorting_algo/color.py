from skimage import color
from scipy.misc import imsave

import numpy as np

newImage = np.random.randint(0, 255, (300, 300, 3))

in_hsv_h = color.convert_colorspace(newImage, 'RGB', 'HSV')
in_hsv_s = in_hsv_h.copy()
in_hsv_v = in_hsv_h.copy()

for i in range(newImage.shape[0]):
    in_hsv_h[i, :, 0] = np.sort(in_hsv_h[i, :, 0])
    in_hsv_s[i, :, 1] = np.sort(in_hsv_s[i, :, 1])
    in_hsv_v[i, :, 2] = np.sort(in_hsv_v[i, :, 2])
imsave('testing-sorted-hue.png', color.convert_colorspace(in_hsv_h, 'HSV', 'RGB'))
imsave('testing-sorted-saturation.png', color.convert_colorspace(in_hsv_s, 'HSV', 'RGB'))
imsave('testing-sorted-value.png', color.convert_colorspace(in_hsv_v, 'HSV', 'RGB'))
