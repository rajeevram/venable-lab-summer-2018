# Research Project – Venable Lab (2018)
Design, analysis, and documentation for my research project in [Dr. Larry Venable's](http://www.eebweb.arizona.edu/faculty/venable/) lab at the Evolutionary Biology & Ecology Department at the University of Arizona. Dr. Larry Venable, and his lab manager [Ursula Basinger](https://eeb.arizona.edu/people/ursula-basinger-walholm) study the [competition, coexistence, and dispersal mechanisms](http://www.eebweb.arizona.edu/faculty/venable/research.htm) of over forty species of [winter annual plants](https://en.wikipedia.org/wiki/Annual_plant#Winter) on Tumamoc Hill.

## Background
Larry and Ursula have identified a collection of terrain segments on Tumamoc Hill, called plots, from which they collect demographic data on winter annual plants. Right now, the distribution of plants and their seeds is manually recorded to scale on a transparency. Plant germination, survival, and reproduction is captured over multiple dates across the growing season, accounting for cohorts. With over three decades of collection, these manually constructed profiles produce insights into the long-term ecological dynamics under study. In order to automate this process and expand the terrain, they are now taking sequential overlapping photos to capture the layout of larger continuous transects. Rajeev's role in this project is to create composite images of these transects and apply a neural network to identify and count plants within the transects. 

## Description
First, we will generate accurate 2D spatial renderings of ecological reserves in the Sonoran Desert using photogrammetric processing of digital images. That is, we will construct a profile of different transects across multiple time points with ground control markers. Finally, we will employ machine learning classification schemes to identify and count common plant species. Eventually, if possible, we would like to to track the long-term growth and survival patterns of over forty of these winter annual plant species. 

## Overview
There are three main objectives involved in this project:
1. Create accurate digital mosaics of the transects by digitally stitching the overlapping pictures together.
2. Create a binary convolutional neural network by training a model with tiles of plants versus non-plants.
3. Employ the machine model on the mosaics to count the number of plants in a particular transect.

Possible additional objectives include:

4. Expand and refine the machine model to categorize according to geus or species.
5. Track the plant growths in a transect via changes in size, physiological state, and reproductive structures over multiple dates.

