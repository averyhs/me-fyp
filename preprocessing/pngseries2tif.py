import numpy as np
import skimage
import os

# Specify directories
ROOTDIR = '/home/avery/Documents/2022/EEE4022/0A_Project_Code/me-fyp/' # absolute path to local project code directory
IMDIR = '../SampleOutput-04_08-30/images' # path to image directory, relative to ROOTDIR

# Input image files
pngpath = os.path.join(ROOTDIR,IMDIR)
pngs = list(os.path.join(pngpath,f) for f in os.listdir(pngpath) if f.endswith('.png')) # list of pngs (as paths) in IMDIR
pngs.sort()

# Get required shape of np array
imshape = np.shape(skimage.io.imread(pngs[0]))

# Read png images and add to numpy stack
imstack = np.empty([len(pngs), imshape[0], imshape[1]])
for n in range(len(pngs)):
    imstack[n,:,:] = skimage.io.imread(pngs[n])

# np array to tif
skimage.io.imsave('images.tif', imstack.astype('uint16'))
