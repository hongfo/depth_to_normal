import cv2 as cv
import numpy as np
import time
from utils import *


def depth_to_3d(depth):
    """
        Convert a depth image to a 3D point .

        Args:
            depth (numpy.ndarray): Depth image with shape (h, w), where h is the height and w is the width.

        Returns:
            numpy.ndarray: Transformed 3D point cloud with shape (h, w, 3), where each point's coordinates are (x, y, z).
    """
    ans = np.zeros((depth.shape[0], depth.shape[1], 3))
    fx, fy, u0, v0 = get_params("depth/scene0000_00.txt")
    h, w = depth.shape
    ans[:, :, 2] = depth
    u_map = np.ones((h, 1)) * np.arange(1, w + 1) - u0
    v_map = np.arange(1, h + 1).reshape(h, 1) * np.ones((1, w)) - v0
    ans[:, :, 0] = u_map / fx * depth
    ans[:, :, 1] = v_map / fy * depth
    return ans


def depth_to_normal(depth):
    """
        Convert a depth image to surface normals.

        Args:
            depth (numpy.ndarray): Depth image with shape (h, w), where h is the height and w is the width.

        Returns:
            numpy.ndarray: Surface normal vectors with shape (h, w, 3), representing the normal direction at each pixel.
    """
    ans = depth_to_3d(depth)

    # Compute spatial vectors between the center point and its right and bottom neighbors using kernel-based filtering
    h_kernel = np.array([[1], [-1]])
    v_kernel = np.array([[1, -1]])
    h_map = cv.filter2D(ans, -1, h_kernel)
    v_map = cv.filter2D(ans, -1, v_kernel)

    normal = np.cross(h_map, v_map)
    normal = vector_normalization(normal)

    return normal


if __name__ == "__main__":
    path = "depth/0.png"
    depth, mask = get_depth(path)
    normal_map = depth_to_normal(depth)
    normal_map = (visualization_map_creation(normal_map, mask) * 255).astype(np.uint8)
    show(normal_map)
    cv.imwrite("../normal-map/cross_normal.png", normal_map)
