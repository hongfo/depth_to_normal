## Introduction

The goal of this project is to generate surface normal maps from depth images.

The method used in this project is based on the paper ["D2NT: A High-Performing Depth-to-Normal Translator"](https://arxiv.org/abs/2304.12031). The paper proposes an effective approach to translate depth maps into normal maps by estimating the surface normals at each pixel.

## Method
The D2NT method consists of the following steps:
1. Load the depth image and corresponding camera parameters.
2. Calculate the depth gradients using either the basic filter or the  Discontinuity-Aware Gradient Filtering (DAG) filter, depending on the chosen version.

3. Perform Depth to Normal Translation using the depth gradients and camera parameters.Normalize the resulting normal vectors.
Optionally, apply MRF-based Normal Refinement to further improve the quality of the normal maps.
4. Generate a visualization map of the computed normals.
Save the normal map as an image.

D2NT provides different versions of the method:
>d2nt_basic: Uses the basic filter for depth gradient calculation.
d2nt_v2: Uses DAG filter for depth gradient calculation.
d2nt_v3: Includes DAG filter for depth gradient calculation and MRF-based Normal Refinement for enhanced results.


## requirements
To use this project, follow these steps:

1. Install the required dependencies mentioned in the requirements.txt file.
2. Place your depth images in the depth folder.
Adjust the camera parameters in the text files located in the depth folder.
3. The resulting normal maps will be saved in the normal-map folder.

## Results

The computed normal maps are saved in the [normal-map](./normal-map/) folder. These maps represent the surface orientations in the corresponding depth images.

This is the comparison result of an example:![compare](normal-map/compare.png)

## References

    @article{feng2023d2nt,
    title={D2NT: A High-Performing Depth-to-Normal Translator},
    author={Feng, Yi and Xue, Bohuan and Liu, Ming and Chen, Qijun and Fan, Rui},
    journal={arXiv preprint arXiv:2304.12031},
    year={2023}
    }
## License

This project is licensed under the MIT License.