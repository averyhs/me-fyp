import numpy as np
from skimage import io
from skimage import exposure
import os

# Specify directories
ROOTDIR = '/home/avery/Documents/2022/EEE4022/0A_Project_Code/me-fyp/' # absolute path to local project code directory
IMDIR = '../SampleOutput-04_08-30/images' # path to image directory, relative to ROOTDIR

# Input image files
pngpath = os.path.join(ROOTDIR,IMDIR)
pngs = list(os.path.join(pngpath,f) for f in os.listdir(pngpath) if f.endswith('.png')) # list of pngs (as paths) in IMDIR
pngs.sort()

# Get required shape of np array
sample_img = io.imread(pngs[0])
imshape = np.shape(sample_img)

# Read png images and add to numpy stack
imstack = np.empty([len(pngs), imshape[0], imshape[1]], dtype=sample_img.dtype)
for n in range(len(pngs)):
    img = io.imread(pngs[n])
    img_rescaled = exposure.adjust_log(img)
    imstack[n,:,:] = img

# np array to tif
io.imsave('images.tif', imstack)
