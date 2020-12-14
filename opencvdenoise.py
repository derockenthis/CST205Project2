import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('Project2/girlnoise.png')

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imwrite('jetImage3.jpg', dst)

# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
