This project applies the method proposed in the paper "D2NT: A High-Performing Depth-to-Normal Translator" to compute surface normals from depth images. It also utilizes cross-product to calculate the surface normal vectors.

Introduction

    The goal of this project is to generate surface normal maps from depth images.
    The method used in this project is based on the paper "D2NT: A High-Performing Depth-to-Normal Translator". The paper proposes an effective approach to translate depth maps into normal maps by estimating the surface normals at each pixel.

Method
The D2NT method consists of the following steps:

    Load the depth image and corresponding camera parameters.
    Calculate the depth gradients using either the basic filter or the Directed Acyclic Graph (DAG) filter, depending on the chosen version.
    Perform Depth to Normal Translation using the depth gradients and camera parameters.
    Normalize the resulting normal vectors.
    Optionally, apply MRF-based Normal Refinement to further improve the quality of the normal maps.
    Generate a visualization map of the computed normals.
    Save the normal map as an image.

    D2NT provides different versions of the method:
    d2nt_basic: Uses the basic filter for depth gradient calculation.
    d2nt_v2: Uses DAG filter for depth gradient calculation.
    d2nt_v3: Includes DAG filter for depth gradient calculation and MRF-based Normal Refinement for enhanced results.

Usage

To use this project, follow these steps:

    Install the required dependencies mentioned in the requirements.txt file.
    Place your depth images in the depth folder.
    Adjust the camera parameters in the text files located in the depth folder.
    The resulting normal maps will be saved in the normal-map folder.

Results

The computed normal maps are saved in the normal-map folder. These maps represent the surface orientations in the corresponding depth images.

References

    Paper: D2NT: A High-Performing Depth-to-Normal Translator
    Author: Yi Feng, Bohuan Xue, Ming Liu, Qijun Chen, Rui Fan



Please refer to the paper for more detailed information about the method and its performance.

License

This project is licensed under the MIT License.