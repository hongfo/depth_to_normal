# This script applies the method proposed in the paper "D2NT: A High-Performing Depth-to-Normal Translator" to
# compute surface normals from depth images.

from utils import *
import cv2 as cv
import time


def run(VERSION):
    # t0 = time.time()
    depth_path = "depth/0.png"
    params_path = "depth/scene0000_00.txt"
    depth, mask = get_depth(depth_path)

    h, w = depth.shape

    depth = cv.normalize(depth, None, 0, 255, cv.NORM_MINMAX, dtype=cv.CV_64F)
    fx, fy, u0, v0 = get_params(params_path)
    u_map = np.ones((h, 1)) * np.arange(1, w + 1) - u0  # u-u0
    v_map = np.arange(1, h + 1).reshape(h, 1) * np.ones((1, w)) - v0

    # get depth gradients
    if VERSION == "d2nt_basic":
        Gu, Gv = get_filter(depth)
    else:
        Gu, Gv = get_DAG_filter(depth)

    # Depth to Normal Translation
    est_nx = Gu * fx
    est_ny = Gv * fy
    est_nz = -(depth + v_map * Gv + u_map * Gu)
    est_normal = cv2.merge((est_nx, est_ny, est_nz))

    # vector normalization
    est_normal = vector_normalization(est_normal)

    # MRF-based Normal Refinement
    if VERSION == "d2nt_v3":
        est_normal = MRF_optim(depth, est_normal)

    # show the computed normal
    n_vis = (visualization_map_creation(est_normal, mask) * 255).astype(np.uint8)
    path = '../normal-map/' + VERSION + '.png'
    cv.imwrite(path, n_vis)
    # print(f"{VERSION} RUNNING_TIME:{time.time()-t0}")
    # plt.figure(f"{VERSION}")
    # plt.imshow(n_vis)
    # plt.show()


if __name__ == "__main__":
    run("d2nt_basic")
    run("d2nt_v2")
    run("d2nt_v3")