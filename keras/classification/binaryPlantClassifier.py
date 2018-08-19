'''
This script is adapted from the article "Building powerful image classification models using very little data" located at blog.keras.io; running this script
requires TensorFlow, Keras, and Python 2.7+ to be installed on the machine.
'''

# Program Name: binaryPlantClassifier
# Creator: Rajeev Ram, adapted from the Keras blog post (https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
# Purpose:
#   This script creates a machine model, and trains it to recognize plants via a convolutional network. The network is binary, and the two classes are
#   plant and ground. The model and it weights can be saved and reloaded, and subsequently used to predict whether an image has a plan or not.

'''
The setup of the image data is as follows:
```
data/
    training/
        plant/
            plant001.jpg
            plant002.jpg
            ...
        ground/
            ground001.jpg
            ground002.jpg
            ...
    validation/
        plant/
            plant001.jpg
            plant002.jpg
            ...
        ground/
            ground001.jpg
            ground002.jpg
            ...
```
Both classes contain 770 training tiles and 230 validation tiles each
'''

import warnings
# Filter out warning messages
warnings.filterwarnings("ignore")

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

# Our image tiles are 100x100 pixels
img_width = 100
img_height = 100

# These directories are detailed above
train_data_dir = 'data/training'
validation_data_dir = 'data/validation'

# These can be experimented with
nb_train_samples = 770 # number of training tiles
nb_validation_samples = 230 # number of validation tiles
epochs = 60 # number of training rounds
batch_size = 14

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

# This is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)
# Augmentatation prevents overfitting

# This is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

# This loads in the training images
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# This loads in the validation images
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# This runs the learning algorithm
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

# This saves the weights to a file
model.save_weights('weights.h5')
