######## Colorize Imgs using OpenCV #########

# Author: George
# Youtube Channel : https://www.youtube.com/channel/UC-j647KCqjQKE50Npx9TZsg

# Description: 
# Colorize imgs using OpenCV and caffemodel.

# Models

# https://github.com/richzhang/colorization/tree/caffe/models
# https://github.com/richzhang/colorization/blob/caffe/resources/pts_in_hull.npy

# Importing the modules.

import numpy as np
import cv2
import os

# Paths

wk_pth = '/home/george/george/coding_place/python/projects/colorize_images'
prototxt_pth = wk_pth + '/model/colorization_deploy_v2.prototxt'
model_pth = wk_pth + '/model/colorization_release_v2.caffemodel'
kernal_pth = wk_pth + '/model/pts_in_hull.npy'
img_pth = input('Input the file path: ')
filename = os.path.basename(img_pth)
out_pth = wk_pth + '/imgs/' + str(filename)

# Loading the model.

net = cv2.dnn.readNetFromCaffe(prototxt_pth, model_pth)

# Loding the kernal.

# Points are cluster center points or kernals
# the are used in the model and is a numpy object.

points = np.load(kernal_pth)

# Reshaping the points convolutional kernal with the size 1 by 1
# and this is somthing that we need in convolut a convolutional neurel network.  

points = points.transpose().reshape(2, 313, 1,1)

# Getting specific layer types.

net.getLayer(net.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606, dtype="float32")]

# Loading the blk & wh img.

bw_img = cv2.imread(img_pth)
normalized = bw_img.astype("float32") / 255.0

# Converting the orginal img to lab format.

img_lab = cv2.cvtColor(normalized, cv2.COLOR_BGR2LAB)

# Resizing the img to 224x224 because the model was
# trained on 224x224 imgs.

img_resize = cv2.resize(img_lab, (224,224))

# Spliting the channels.

l = cv2.split(img_resize)[0]
l -= 50

# Setting the input to the model.

net.setInput(cv2.dnn.blobFromImage(l))

# Getting the results.

ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

# Resizing the img to it's orginal size.

ab = cv2.resize(ab, (bw_img.shape[1], bw_img.shape[0]))

# Getting the lightness.

l = cv2.split(img_lab)[0]

#-------------------------DONE BY MY DAD-------------------------

# Finally getting the result img.

reduction_ratio = 1
reduction_ratio_w = 1
reduction_ratio_h = 1

w = bw_img.shape[1]
h = bw_img.shape[0]

if (w > 500):
    reduction_ratio_w = w / 500

if (h > 300):
    reduction_ratio_h = h / 300

if (reduction_ratio_w > reduction_ratio_h):
    reduction_ratio = reduction_ratio_w

else:
    reduction_ratio = reduction_ratio_h

w = int(w / reduction_ratio)
h = int(h / reduction_ratio)

colorized_img = np.concatenate((l[:, :, np.newaxis], ab), axis = 2)
colorized_img = cv2.cvtColor(colorized_img, cv2.COLOR_LAB2BGR)
colorized_img = (255.0 * colorized_img).astype("uint8")
copy = colorized_img
colorized_img = cv2.resize(colorized_img, (w, h))
bw_img = cv2.resize(bw_img, (w, h))

# Write it on to the HD

cv2.imwrite(out_pth, colorized_img)

# Displaying the img.

cv2.imshow("Orginal Img", bw_img)
cv2.imshow("Colorized Img", colorized_img)
cv2.waitKey(0)