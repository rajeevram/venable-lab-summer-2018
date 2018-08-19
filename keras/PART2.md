# Part II – Machine Learning

## Part 2A: Training A Neural Network

Because the number of plants that appear in a given area of the transect is quite small, we needed to be able to develop a construct a neural network with only a couple thousand instances of data. Thus, we decided to build a binary classification model with the [Keras Library](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html).

Furthermore, after research, we were not able to a find a pre-trained network that would appropritely adapt to classifying winter annual plants. Thus, our classification network is contructed from scratch. Moving forward, the goal is to fine-tune the decisions of our trained-from-scratch machine learning model.

### Creating Training Tiles

We generated 1600 training tiles in two classes: plant and ground. Each training tile is a 100 pixel x 100 pixel PNG that comes from splitting up individual photos (similar to the ones in the agisoft/transect folder) chosen at random.

![Image](https://imgur.com/fAjmi2r.png)

The above image is 400 x 2250, and therefore produces 880 training tiles. Morever, by cropping the photo +50 pixels right and down, we can generate another 880 training tiles that are offset from the originals.

From these, plant and ground tiles, or varying quality (e.g., some are blurry, some contains plants that are off-center) were selected to promote the development of a robust model.

Example Ground Tiles:

![Ground](https://imgur.com/GERJljt.png) ![Ground](https://imgur.com/OiSVxZz.png) ![Ground](https://imgur.com/OiSVxZz.png) ![Ground](https://imgur.com/YCCrEbV.png) ![Ground](https://imgur.com/YCCrEbV.png)

Example Plant Tiles:

![Plant](https://imgur.com/KUsNHfh.png) ![Plant](https://imgur.com/WHMRkz5.png) ![Plant](https://imgur.com/FxJzcqA.png) ![Plant](https://imgur.com/mbb7pa1.png) ![Plant](https://imgur.com/ciBVQ5Z.png) ![Plant](https://imgur.com/fnPNkvc.png) ![Plant](https://imgur.com/9wQo87R.png)

### Python Training Script

Check for binaryPlantClassifier.py within the classification folder. The weights from the training and validation series are saved to an .h5 file that can be reimported later.

### Cross-Validation


## Part 2B: Binary Prediction Results

