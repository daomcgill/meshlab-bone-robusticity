# Measuring Robusticity of 3D Bone Meshes
## Overview

This project seeks to standardize robusticity grading of various bones, by using 3D scanned meshes and principle curvature analysis. Currently, robusticity is being measured using sight, and comparison to a non-standardized range. 

>**Definition of robusticity:** [https://github.com/daomcgill/meshlab-bone-robusticity/blob/e620405de06738181e53e2ba6324cc5f1e6fc753/docs/Robusticity%20definition.docx][1] <br />
<font size="1"> - Ashley Atkins</font>

## Curvature Measurement

>**Curvature:** in mathematics, the rate of change of direction of a curve with respect to distance along the curve. At every point on a circle, the curvature is the reciprocal of the radius; for other curves (and straight lines, which can be regarded as circles of infinite radius), the curvature is the reciprocal of the radius of the circle that most closely conforms to the curve at the given point <br />
<font size="1"> - Britannica, The Editors of Encyclopaedia. "curvature".<br /> Encyclopedia Britannica, 18 Aug. 2013, [https://www.britannica.com/science/curvature][2]. Accessed 8 May 2022.</font>

* **Principal Curvature:**<br /> The maximum **<img src="https://latex.codecogs.com/svg.image?\bg{black}\kappa_{1}">** and minimum **<img src="https://latex.codecogs.com/svg.image?\bg{black}\kappa_{2}">** normal curvature at a given point on a surface. 
* **Gaussian Curvature:**<br /> <img src= "https://latex.codecogs.com/svg.image?\bg{black}K=\kappa_{1}\cdot&space;\kappa_{2}">
* **Mean Curvature:**<br /> <img src="https://latex.codecogs.com/svg.image?\bg{black}H=\frac{1}{2}\left&space;(&space;\kappa_{1}&plus;\kappa_{2}&space;\right&space;)">
* **Taubin Approximation of Principal Curvature Directions:**<br />
> https://github.com/daomcgill/meshlab-bone-robusticity/blob/59eeb6f23a9875098134fe087728adef551fa869/resources/taubin-iccv95b.pdf<br />
<font size="1"> - Gabriel Taubin </font>

**in Meshlab:**<br />
A 1-ring neighborhood is taken around a current central vertex, and the change in slope to all neighboring vertices is used the calculate the curvature of the point. Iterates through all vertices of the mesh. 

## Obtaining Curvature Values from Meshlab

1. The first step in obtaining curvature values from Meshlab is to produce a 3D object file. This can be achieved through 3D scanning or photogrammetry. In this case, photogrammetry was more suited to the task, as 3D scanned objects have inherent roughness due to their creation process. 
![Object file (.obj) of a bone as a 3D mesh](/images/uag66_bone.png)



  [1]: https://github.com/daomcgill/meshlab-bone-robusticity/blob/e620405de06738181e53e2ba6324cc5f1e6fc753/docs/Robusticity%20definition.docx
  [2]: https://www.britannica.com/science/curvature
