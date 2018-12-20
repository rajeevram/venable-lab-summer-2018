# Part II – Machine Learning

Configure a neural network to perform semantic segmentation to label areas of the transect which are plants. A [U-Net Architecture](https://arxiv.org/abs/1505.04597) was used. Right now, the machine model is binary, and some more work must be done to achieve a multi-class model with efficacy.

Please read the PDF titled [RajeevCodeResults](./rajeev_code_results.pdf) for a more detailed account of the process. The relevant scripts are located in the `code` directory.  **Running on a machine with a GPU is strongly recommended.**

## Part 2A: Training A Neural Network

The instructions for running `train.py` are described in the report.  The weight are saved to `unet_plant.h5` after training and can be reimported later.

### Preparing The Data

Open-source image editing software (GIMP) was used to prepare the grayscale tiles that correspond to the RGBA tiles.

## Part 2B: Binary Prediction

The instructions for running `test.py` are described in the report.

### Apply Result To The Mosaic

The testing tiles are all collected from photographs that were used to construct the digital orthomosaics. The `results` directory contains visualizations of the predictions on sixteen instances.

## Auxiliary Files: Data, Model

The `data.py` file contain descriptions of how the data is prepared and processed for training and testing. The `model.py` file shows how the machine model is configured.



