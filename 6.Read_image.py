# author: Krzysztof Sopyła (krzysztofsopyla@gmail.com)
# Twitter: ksopyla
# Blog: http://ksopyla.com

# If you want to use this material in your own trainning please let me know.
import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('Tiger.jpg')
img_tinted = img * [1, 0.3, 0.5]

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.imshow(np.uint8(img_tinted))
plt.show()


#get the red channel

r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]

#plt.imshow(img,cmap='Greys_r')

plt.subplot(3,1,1)
plt.imshow(r)
plt.subplot(3,1,2)
plt.imshow(g)
plt.subplot(3,1,3)
plt.imshow(b)





