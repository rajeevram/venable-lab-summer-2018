# Part I – Generating Mosaics

## Photographing Transects

Each transect on Tumamoc hill varies considerably in size. Generally, a transect that is 20 x 20 meters squared is captured in a series of 100–150 overlapping photos. A sample of 15 consecutive photos for a particular transect on a particular date is given in the transect folder. Each photo is taken in series, and a single photos overlaps about half of its area with its predecessor and successor, respectively.

## Generating A Mesh

These overlapping photos are used to generate a non-overlapping mosaic of a whole transect. We stitched the imaged together using a photgrammetring image processing software called [Agisoft Photscan](http://www.agisoft.com/).

Once the photos are uploaded, various settings must be tuned over many trials to produce a decent model, or mesh.

![Mesh View One](https://imgur.com/wXrWaYG.png)

![Mesh View Two](https://imgur.com/8Bsu755.png)

![Mesh View Three](https://imgur.com/zd0V1ks.png)

Many times, the mesh generated contains holes, or is not flat. This is because the generator is not able to match content that overlaps between photos to a single location. Photos are are not included in the mese generated are marked as NA.

![Photo Not Added](https://imgur.com/9ARSLSN)

When this happens, either ground control points or GPS coordinated must be input to match landmarks between photos. Manually entering in GCPs is time-consuming, so it is best approach this in iterations. For example, first you input a few across many sets of non-overlapping photos.

![GCP #1](https://imgur.com/813v5tH.png)

![GCP #2](https://imgur.com/R0uplw2.png)

![GCP #3](https://imgur.com/QVt8TtD.png)

Then, you run the geneator once more, and see which images are now included. Then, you add some more GCPs and look for even more improvement.

## Exporting The Mosaic

Once a mesh of satifactory quality is generated, then it can be exported as an orthomosaic. An orthomosaic is just the stitched-together version that is projected onto a flat surface, to get rid of the remaining bumps.

![Orthomosaic](https://imgur.com/wI1kUDN.png)

The above picture is just a miniatuarized version of actual file. The actual orthomosaic is a 500+ MB TIFF.
