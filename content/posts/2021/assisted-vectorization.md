---
title: "Image Vectorization 🖇🍮"
date: 2021-12-08T19:26:46+01:00
draft: false
toc: true
tags:
  - svg
  - python
  - code
  - image
---


Automated vectorization and upscaling is useful in many scenarios particularly
for drawn art that can be segmented and is generally structured using strokes
and gradients. Here I will outline a methodology that is based around
structural analysis and direct regression methods then evaluate error metrics
for fine-tuning by comparing the output with non-vectorized up-scalers.


## Observations

Regarding image segmentation, I suspect the most common approach is directly
clustering the entire image using the colour and position. In
most scenarios this feature-space will be separable and is a well understood
problem statement. There result still poses some issues; first cluster enclosure
is difficult to resolve (convexity is not guaranteed), second gradient
components weaken the separability of the data. In addition we may need to
sub-sample the image since clustering is computationally expensive given the
mega-samples of image data.

## Outline

0. Coarse Analysis
    - Cluster based on colour-space and |∇×F| |∇·F| normalized components
    - Present image colour and segmentation complexity
    - Partition image in delta space using histogram method
1. Pre-processing and edge thresholding
    - Compute the YCbCr equivalent representation
    - Map the input colour space based on k-means / SVM for maximum cluster separation
    - Compute edges in images and fit spline segments with grouping
2. Fine image segmentation
    - Use edges to initialize segments and segment regions based on colour deltas
    - Complete segmentation by filling image
    - Regression to fit colour for each segment
4. Image restructuring and grouping
    - Simplify structures by creating region hierarchy
    - SVG 2.0 supports mesh-gradients / Bezier surface composition
    - Detect regular patterns with auto correlation / parameter comparison
3. Error evaluation and recalibration
    - Use upscaled reference to evaluate error
    - Identify segments that need to be restructured with more detail


## Action Items

 - Colour surface fitting
    - Given a set of samples, fit an appropriate colour gradient
 - Image normalization and pre-processing
 - Edge composition and image segmentation
    - Define a model for segments of the image
    - Define a model for closed and open edges
    - Evaluate segment coverage of the image
 - Heuristics for image hierarchy and optimizations


## Pre-processing Engine

Currently histogram binning has proven to be very effective for generating
initial clusters since it scales well with image size. This allows us to
quickly gauge the complexity of an image in terms of content separability.
These regions will be used to partition the image as edges are extracted
before more accurate mapping is performed.

The main challenge here is colour gradients that washout what should be
obvious centroids. Analysing the samples in batches can prevent this to some
extent but a more robust approach is needed. We could use a localized grouping
technique but accuracy may need be that important for this pre-processing step.
Another technique is that the image can first be clustered using the histogram
of derivative components followed by sub-classing a histogram for each gradient
cluster.

This idea for histogram-binning is surprisingly efficiently for artificial
images where the colour pallet is rich in features. A binary search for
parameterizing the local maxima detection will very quickly segment a wide
variety of images into 10 - 30 classifications.

## Edge extraction

At some point we will want to construct a model representing regions and shapes.
The principle component here is identifying edges segmenting the image. Edge
detection is relatively strait-forward as we only need look for extrema in the
derivative components. In most scenarios this is actually quite noisy and
it is not obvious how we should threshold for what is and what is not an edge.

Here we use the histogram-based clustering result for edge detection region to
region transitions are discretized and no adaptive threshold is required.
There will unavoidably be noisy regions where we see this boundary being spread
out or possibly just a select few pixels appearing in some sub-section due to
the clustering process. This can mostly be removed with a median filter if
necessary.

If the initial segmentation are generated based on k-means in the colour space,
two families of edges will be detected along segments: hard and soft edges.
Hard edges will correspond to the intended edges seen in the image where as
soft edges will arise due to the clustering technique. We can classify these
two families by looking at the norm of the derivative component along such an
edge. There will be more than one way to asses the correctness here but the
significance here is that soft edges present boundary conditions during colour
mapping while hard edges do not. Otherwise visual artefacts will arise are the
interface of two segments that originally was a smooth transition.


## Structural Variability

While we are targeting a-typical images for vectorization it is obvious that
'sharpness' in the final result depends on a subjective style that is difficult
to assess in terms of simple regress or interpolation. This problem however is
central to upscaling algorithms so the methodology here will be that a external
upscaling tool will guide the vectorization process. For example vectorizing
a pixel-art image yields better results 'nearest-neighbour' methods opposed to
Lanczos resampling.


## Regression over SVG colour surfaces

The SVG standard supports three methods for specifying colour profiles or
gradients: Flat, Linear, Radial. There are more advanced mechanisms through
embedding or meshing multiple components the aforementioned three readily
allow us to fit a first order colour contour through linear
regression. This will be our first objective for parameterizing
the colour for segments in our image. Another thing to note is that the gradient
can be transformed after being parameterized. This means that the a circular
gradient can be transformed to realize a family elliptical gradients.

Obviously this will not accommodate all colour contours that we find in images
but in such scenarios we may adopt piece-wise approximations or more accurate
masking of each component using the alpha channel. At some point we should
also be able to resolve mixtures and decompose the contour from a non-linear
or higher-order surface into multiple simpler contours. Again note that support
for advanced colour profiles is not well supported so composition through
these basic elements will yield the best support.

Using linear regression here with a second order polynomial kernel is a very
efficient method for directly quantifying the focal point of the colour
gradient if there is one.


## Contour estimation

My initial attempt to estimate the contour given a set of points was based on
using the convex-hull and recursively enclosing the outline in more detail
by interpolating in between the current outline and finding the closest point
orthogonal to the outline. This result yields a fast approximation of the
enclosing outline without many requirements on the set of points other than
having a dense outline. The drawback was that if it difficult to detect
incorrect interpolation and only resolves the outline with pixel-level
precision. If we pre-process the collection of points such that they
represent detected edges at sub-pixel resolution the later draw-back can be
addressed. Correctness or hypothesis testing could yield a more robust result
at the cost of increased complexity.
