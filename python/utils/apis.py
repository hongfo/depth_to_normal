import cv2 as cv
import numpy as np


def show(img, win_name="img"):
    cv.imshow(win_name, img)
    cv.waitKey()
    cv.destroyAllWindows()


def get_depth(path):
    depth = cv.imread(path, -1)
    mask = np.ones_like(depth)
    mask[depth == 0] = 0
    return depth, mask


def get_params(path):
    lines = open(path).readlines()
    list1 = []
    for line in lines:
        if "fx_depth" in line:
            fx = line.split()[-1]
            list1.append(int(eval(fx)))
        if "fy_depth" in line:
            fy = line.split()[-1]
            list1.append(int(eval(fy)))
        if "mx_depth" in line:
            u0 = line.split()[-1]
            list1.append(int(eval(u0)))
        if "my_depth" in line:
            v0 = line.split()[-1]
            list1.append(int(eval(v0)))
    return list1


def vector_normalization(normal, eps=1e-8):
    mag = np.linalg.norm(normal, axis=2)
    normal /= np.expand_dims(mag, axis=2) + eps
    return normal


def visualization_map_creation(normal, mask):
    mask = np.expand_dims(mask, axis=2)
    vis = normal * mask + mask - 1
    vis = (1 - vis) / 2  # transform the interval from [-1, 1] to [0, 1]
    return vis
