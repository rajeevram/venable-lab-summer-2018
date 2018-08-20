# Part II – Machine Learning

Create a binary convolutional neural network by training a model with tiles of plants versus non-plants. Employ the machine model on the moasics to count the number of plants in a particular transect.

## Part 2A: Training A Neural Network

Because the number of plants that appear in a given area of the transect is quite small, we needed to be able to construct a neural network with only a couple thousand instances of data. Thus, we decided to build a [binary classification model with the Keras Library](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html).

Furthermore, after research, we were not able to a find a pre-trained network that would appropriately adapt to classifying winter annual plants. Thus, our classification network is constructed from scratch. Moving forward, the goal is to fine-tune the decisions of our trained-from-scratch machine learning model.

### Creating Training Tiles

We generated 1600 training tiles in two classes: plant and ground. Each training tile is a 100 pixel x 100 pixel PNG that comes from splitting up individual photos (similar to the ones in the agisoft/transect folder) chosen at random.

![Image](https://imgur.com/fAjmi2r.png)

The above image is 4000 x 2250, and therefore produces 880 training tiles. Morever, by cropping the photo +50 pixels right and down, we can generate another 880 training tiles that are offset from the originals.

From these, plant and ground tiles of varying quality (e.g., some are blurry, some contains plants that are off-center) were selected to promote the development of a robust model.

Example Ground Tiles:

![Ground](https://imgur.com/GERJljt.png) ![Ground](https://imgur.com/6RvqwPv.png) ![Ground](https://imgur.com/OiSVxZz.png) ![Ground](https://imgur.com/TV0ClxH.png) ![Ground](https://imgur.com/YCCrEbV.png) ![Ground](https://imgur.com/teKZHGG.png) ![Ground](https://imgur.com/lQD9Ev8.png)

Example Plant Tiles:

![Plant](https://imgur.com/KUsNHfh.png) ![Plant](https://imgur.com/WHMRkz5.png) ![Plant](https://imgur.com/FxJzcqA.png) ![Plant](https://imgur.com/mbb7pa1.png) ![Plant](https://imgur.com/ciBVQ5Z.png) ![Plant](https://imgur.com/fnPNkvc.png) ![Plant](https://imgur.com/9wQo87R.png)

### Python Training Script

Check for the binaryPlantClassifier.py file within the classification folder. The weights from the training and validation series are saved to an .h5 file that can be reimported later.

### Cross-Validation

After selecting and finalizing the training data, a five-fold cross-validation was performed. In every case, 1200 of the 1600 tiles were used for training and the remaining 400 were used for validation. Two example results from the cross-validation are showed in weightsOne.txt and weightsTwo.txt (see the classification folder); a batch size of 12 was used over 75 epochs.

Both of these trials were rather successful as indicated by: a steady descrese in training and validation loss over time, a training accuracy of ~0.8, and a training and validation accuracy that are within 5% of each other. Consdering the small data set, and that ours is not a pre-trained network, these results are rather enouraging.

## Part 2B: Binary Prediction

### Python Prediction Script

Check for the binaryPlantPredictor.py file within the prediction folder. A new Keras model is instantiated, compiled, and loaded with the previously determined weights. The prediction method takes any number of images from a specified directory, compresses and stacks them into a tensor for processing, and outputs and array of 1s (plant) and 0s (ground).

### Apply Result To The Mosaic

Right now, while the recall of our model is wonderful, its precision and accuracy are lagging behind in terms of performance. Before we apply it to the mosaic, we need to make sure our precision and accuracy match the high performance of our recall. On the other hand, we might move straight into a four-way model soon instead of maintaining the binary model.

