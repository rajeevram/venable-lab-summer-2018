# Part I – Generating Mosaics

Create accurate digital mosaics of the transects by digitally stitching the overlapping pictures together.

## Photographing Transects

Each transect on Tumamoc hill varies considerably in size. Generally, a transect that is 20 x 20 meters squared is captured in a series of 100–150 overlapping photos. A sample of 15 consecutive photos for a particular transect on a particular date is given in the transect folder. Each photo is taken in series, and a single photos overlaps about half (or less) of its area with its predecessor and successor, respectively.

## Generating A Mesh

These overlapping photos are used to generate a non-overlapping mosaic of a whole transect. We stitched the images together using a photogrammetric image processing software called [Agisoft Photscan](http://www.agisoft.com/).

Once the photos are uploaded, various settings must be tuned over many trials to produce a decent model, or mesh.

![Mesh View One](https://imgur.com/wXrWaYG.png)

![Mesh View Two](https://imgur.com/8Bsu755.png)

![Mesh View Three](https://imgur.com/zd0V1ks.png)

Many times, the mesh generated contains holes, or is not flat enough to be an accurate representation of the actual transect. This is because the generator is not able to match content that overlaps among photos to a single location. 

![Non-Flat Mesh](https://imgur.com/uhqzRTE.png)

Sometimes, when photos cannot be placed properly into the mesh, they are just omitted from the model. Photos that are not included in the meshes generated are marked as NA in the workspace.

![Photo Not Added](https://imgur.com/9ARSLSN.png)

When this happens, either ground control points or GPS coordinates must be input to match landmarks among photos. Manually entering in GCPs is time-consuming, so it is best to approach this in iterations. For example, first input a few GCPs across many small sets of non-overlapping photos.

![GCP #1](https://imgur.com/813v5tH.png)

![GCP #2](https://imgur.com/R0uplw2.png)

![GCP #3](https://imgur.com/QVt8TtD.png)

Then, you run the generator once more, and see which images are now included. Then, you add some more GCPs and look for even more improvement, all the while fine-tuning various parameters.

## Exporting The Mosaic

Once a mesh of satisfactory quality is generated, then it can be exported as an orthomosaic. An orthomosaic is just the stitched-together version that is projected onto a flat surface, to get rid of the remaining bumps.

![Orthomosaic](https://imgur.com/wI1kUDN.png)

The above picture is just a miniaturized version of actual file. The actual orthomosaic for this transect is a 500+ MB TIFF. Other transects produce orthomosaics of an even larger file size simply because of the sheer number of photos used in the generation of the final image.
