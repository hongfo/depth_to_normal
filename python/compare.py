import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv

depth = mpimg.imread('depth/0.png')
cross_normal = cv.imread('../normal-map/cross_normal.png')
d2nt_basic = cv.imread("../normal-map/d2nt_basic.png")
d2nt_v2 = cv.imread("../normal-map/d2nt_v2.png")
d2nt_v3 = cv.imread("../normal-map/d2nt_v3.png")

fig, axes = plt.subplots(1, 5, figsize=(40, 8))

axes[0].imshow(depth)
axes[0].set_title('depth')

axes[1].imshow(cross_normal)
axes[1].set_title('cross_normal')

axes[2].imshow(d2nt_basic)
axes[2].set_title('d2nt_basic')

axes[3].imshow(d2nt_v2)
axes[3].set_title('d2nt_v2')

axes[4].imshow(d2nt_v3)
axes[4].set_title('d2nt_v3')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.savefig('../normal-map/compare.png')
plt.show()
