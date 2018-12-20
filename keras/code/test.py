## Script Name: test
## Author: Rajeev Ram
## Class: ISTA 421, Machine Learning
## Due: 5pm, Monday, Decembeer 10th
## Purpose:
##    Run this script to use an already trained unet() model
##    for testing on new data.    

from model import *
from data import *

# Create new model and load existing weights
model = unet()
model.load_weights("unet_plant.hdf5")

# Configure test data in to proper format
testGene = testGenerator("data/test")

# The value of second parameter steps should equal to
# the number of images in the test folder
results = model.predict_generator(testGene, steps=21, verbose=1)

# Save the results after prediction
saveResult("data/test",results)
