'''
This script loads the weights from a Keras model previous trained on a binary classification scheme (plant
versus ground) and then performs a prediction on new images from a specified folder. Running this script
requires TensorFlow, Keras, and Python 2.7+ to be installed on the machine.
'''

# Program Name: binaryPlantPredictor
# Creator: Rajeev Ram, with help from Dr. Yun Wang
# Purpose:
#   This script loads in the weights created by a previously trained convuolutional network. The network is binary, and the two classes are
#   plant and ground. Once the model is compiled and its weights are loaded, it is used to predict on a new dataset of images; an array of
#   1s and 0s is output.

import warnings
# Filter out warning messages
warnings.filterwarnings("ignore")

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import os
import numpy as np

# Our image tiles are 100x100 pixels
img_width = 100
img_height = 100

# The prediction images are contained in this directory
prediction_datagen = ImageDataGenerator(rescale=1. / 255)
prediction_data_dir = 'data/validation'

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# Adding many layers to the model's network
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

# Compile with various settings
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Loading in the previously saved weights
model.load_weights('weightsJ.h5')

# Array to store images for prediction
images = []

# Read images in from a specified folder
for filename in os.listdir('imagesG3'):
	img = image.load_img(os.path.join('imagesG3', filename), target_size=(img_width, img_height))
	x = np.expand_dims(image.img_to_array(img)/255, axis=0) # flatten the image matrix to 10K + RBG values
	images.append(x) # append the values to the image matrix

# Make predictions and output to an array of 0s and 1s
pred_results = model.predict_classes(np.vstack(images), verbose=1) # vstack concatenates the images together

# Change to a loop counter instead of printing at some point
# print(pred_results)
i = 0
for arr in pred_results:
    if arr[0] == 1:
        i += 1
print(i)
