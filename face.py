import matplotlib.pyplot as plt

# TODO: Rm try-except with scipy 1.10 is the minimum supported version
try:
    from scipy.datasets import face
except ImportError:  # Data was in scipy.misc prior to scipy v1.10
    from scipy.misc import face

img = face()
print(img)

plt.imshow(img)
print(img.shape)