## Script Name: train
## Author: Rajeev Ram
## Class: ECOL 499, Independent Research Project
## Purpose:
##    Run this script to train a unet() model on image data.
## Credits:
##      Adapted from the following repostiory:
##      https://github.com/zhixuhao/unet

from model import *
from data import *

# This dictionary is used for data augmentation on training data
data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')

# The batch size determines how many images to use per training step. 
# Small number means slow training speed but less likely to miss the optimal weights
# Large number means fast training speed but might miss optimal weights
myGene = trainGenerator(2,'data/train','image','label',data_gen_args,save_to_dir = None)

# Create and compile model and allow for weights to be saved only as loss goes down
model = unet()
model_checkpoint = ModelCheckpoint('unet_plant.hdf5', monitor='loss',verbose=1, save_best_only=True)

# Steps Per Epoch = Number of Training Images / Batch Size, for optimal usage according to paper
# Start with small number to test the code, then a reasonably large value to train a model
model.fit_generator(myGene,steps_per_epoch=30,epochs=20, callbacks=[model_checkpoint])

