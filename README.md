# Rice Orientation

## Background
Imagine that you handle a rice processing plant and you want to predict how efficiently rice will pass through various processing steps. Based on their size, orientation may not matter. For the sake of argument, let's assume that more grains oriented in the direction of travel implies that more grains will pass through the processing step in a given amount of time. This was the portfolio project I chose for my _Foundations of Artificial Intelligence_ course in my master's program. As a proof-of-concept, this program focuses on individual rice grains, rather than rice as an aggregate.

## Methodology
The images used for this project come from [Kaggle](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset) and are very clean, mitigating many cleaning steps that would be required for live images. This script can be run on its own, provided you clone this repository to have access to all required files and load all required packages.

1. Using _Sci-Kit Image_, a full-color image of a well-separated rice grain is loaded, based on user input.
2. The full-color image is converted to grayscale.
3. Using `skimage.feature.canny`, the edges of the rice grain are outlined.
4. Using `skimage.transform.hough_ellipse`, an elliptical approximation of the rice grain is calculated. \
    a. `skimage.draw.ellipse_perimeter` displays the ellipse on the original image. \
    b. The orientation of the ellipse is calculated from major and minor axes, which is piped through `grain_orientation` to determine whether or not it is vertical $\pm 30\degree$. \
	c. A reference line is drawn on the image to aid understanding using `skimage.draw.line`. 
5. The original image is displayed with the ellipse and reference line, along with a descriptive title of the grain orientation and whether or not it is vertical.


## Results
Each run takes about 6 seconds, depending on how elliptical (or not) the selected rice grain is. This is impractical for production usage, but is an interesting proof-of-concept should it be expanded to examining thousands of grains in an aggregate in under a second.


![Vertical Grain Example](https://github.com/davidmvermillion/riceorientation/blob/main/Results/Basmati_1.png)\
*Vertical Grain Example Result*
 
 
![Non-Vertical Grain Example](https://github.com/davidmvermillion/riceorientation/blob/main/Results/Jasmine_1.png) \
 *Non-Vertical Grain Example Result*
   
   
   
![Barely non-Vertical Grain Example](https://github.com/davidmvermillion/riceorientation/blob/main/Results/Karacadag_10.png) \
*Barely non-Vertical Grain Example Result*
 
 
 
![Terminal Run Example](https://github.com/davidmvermillion/riceorientation/blob/working/Results/Terminal%20Sample.png) 
*Terminal Run Example*

## Implications
This shows how an image can be quickly assessed to find its outline and build properties from there. While this specific approach to determining rice grain orientation is impractical for production usage, but is an interesting proof-of-concept should it be expanded to examining thousands of grains in an aggregate in under a second. Additionally, it provides an interesting possible approach for my ongoing [Crater Detection Algorithm](https://github.com/davidmvermillion/MarsComputerVision) to find symmetrical craters, provided the image can be appropriately sub-divided and probed.

## Primary File Descriptions
[Main Script](https://github.com/davidmvermillion/riceorientation/blob/working/rice_orientation_classifier.py) is the primary file to run once you clone the repository to run yourself. \
[Function Script](https://github.com/davidmvermillion/riceorientation/blob/working/functions.py) holds functions that aren't from pre-existing packages, but needed for this script. \
[Grain Images](https://github.com/davidmvermillion/riceorientation/tree/working/Rice_Image_Dataset) each folder has 15,000 250x250 RGB images of rice grains on a plane, allowing for 2D calculations. The [citation request document](https://github.com/davidmvermillion/riceorientation/blob/working/Rice_Image_Dataset/Rice_Citation_Request.txt) is also held here. \
[Original Report](https://github.com/davidmvermillion/riceorientation/blob/main/Results/CSC510_Module8_Portfolio_Vermillion_David_Itr2.pdf) provides a more detailed examination of the methodology and results, as submitted for my portfolio project. \
[Original Script](https://github.com/davidmvermillion/riceorientation/blob/working/rice_orientation_classifier_original_script.py) if you want to run it all as one as written in the aforementioned report.
