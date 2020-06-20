
import numpy as np
import cv2
img = cv2.imread("image_name.png")
img = cv2.resize(img, (256, 256))
img = img.astype('float32')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img /= 255
np.savez_compressed("image_name",features=img)