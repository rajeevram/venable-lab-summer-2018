# Research Project – Venable Lab (Summer 2018)
Design, analysis, and documentation for my (ongoing) summer research project in [Dr. Larry Venable's](http://www.eebweb.arizona.edu/faculty/venable/) lab at the Evolutionary Biology & Ecology Department at the University of Arizona. Dr. Larry Venable, and his lab manager [Ursula Basinger](https://eeb.arizona.edu/people/ursula-basinger-walholm) study the [competition, coexistence, and dispersal mechanisms](http://www.eebweb.arizona.edu/faculty/venable/research.htm) of over forty species of [winter annual plants](https://en.wikipedia.org/wiki/Annual_plant#Winter) on Tumamoc Hill.

## Background
Larry and Ursula have identified a collection of terrain segments on Tumamoc Hill, called transects, from which they collect and study data on plants. Right now, to capture the layout of a given transect, multiple overlapping photos are taken in sequence; afterward, the distribution of plants and their seeds is manually recorded to scale on a transparency. Consequently, plant and seed counts are determined. The state of the transects is captured over multiple dates, so a to-scale transparency must be created for each transect for each date. Finally, these manually constructed profiles must be examined to produce insights into the ecological dynamics under study.

## Description
Generate accurate 2D spatial renderings of ecological reserves in the Sonoran Desert using photogrammetric processing of digital images. Construct a GIS profile of different transects across multiple time points with ground control markers. Employ machine learning classification schemes to track the long-term growth and survival patterns of over forty winter annual plant species. Collected data is used to study the coexistence and competition mechanisms in arid biomes, especially those induced by ongoing global climate change.

## Overview
There are three main steps involved in this project:
1. Create accurate digital mosaics of the transects by digitally stitching the overlapping pictures together.
2. Create a binary convolutional neural network by training a model with tiles of plants versus non-plants.
3. Employ the machine model on the mosaics to count the number of plants in a particular transect.

Possible additional steps include:

4. Expand and refine the machine model to categorize according to species or genus.
5. Track the plant growths in a transect via their sizes over multiple dates.

