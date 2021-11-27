import base64
from io import BytesIO

import cv2
import numpy as np
from PIL import Image
from skimage import util, color


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        img = np.array(img)
        img_la = color.rgb2gray(img)
        img_la = util.img_as_ubyte(img_la)

        # 0.11 and 0.27, sigma = 1,     from Measuring visual clutter
        # See sigma here: https://dsp.stackexchange.com/questions/4716/differences-between-opencv-canny-and-matlab-canny
        img_la = cv2.GaussianBlur(img_la, (7, 7), 1)
        cd = cv2.Canny(img_la, 0.11, 0.27)
        total = cd.shape[0] * cd.shape[1]  # Total number of pixels
        number_edges = np.count_nonzero(cd)  # Number of edge pixels
        contour_density = float(number_edges) / float(total)  # Ratio

        result = [contour_density]

        print("#################HCI_Rule13_Edge_Density#################")
        print()
        # Detect Average Saturation Metrics
        print("****************************")
        print("Edge Density is: ")
        print(result[0])

        avgSat = ''
        avgSatDoc = ''
        isAccepted = False

        # Check applicability of Average Saturation
        if 0.00 <= float(result[0]) <= 0.12:
            avgSat = "Good"
            isAccepted = True
            print("Good")
        elif 0.13 <= float(result[0]) <= 0.22:
            avgSat = "Fair"
            isAccepted = True
            print("Fair")
        elif 0.23 <= float(result[0]):
            avgSat = "Poor"
            avgSatDoc = 'HCI_Rule10_Edge_Density'
            isAccepted = False
            print("Poor")

        return [
            "Edge Density",
            "pf",
            isAccepted,
            result[0],
            avgSat,
            avgSatDoc
        ]
