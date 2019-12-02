import vot
from vot import Rectangle
import sys
import cv2  # imread
import torch
import numpy as np
from os.path import realpath, dirname, join




# load net
import vot
import sys
import time

handle = vot.VOT("rectangle")
selection = handle.region()

# Process the first frame
imagefile = handle.frame()
if not imagefile:
    sys.exit(0)

while True:
    imagefile = handle.frame()
    if not imagefile:
        break

    handle.report(selection, confidence)
    time.sleep(0.01)