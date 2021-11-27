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

        # Get the number of edge pixels per level. See 1
        edge_per_level = []
        for x in range(1, 8):
            # Blur is needed: https://dsp.stackexchange.com/questions/4716/differences-between-opencv-canny-and-matlab-canny
            img_la = cv2.GaussianBlur(img_la, (7, 7), 2)
            cd = cv2.Canny(img_la, x * 0.04, x * 0.1)  # Higher level from 0.1-0.7, lower level is 40% of higher
            number_edges = np.count_nonzero(cd)  # Number of edge pixels
            edge_per_level.append(number_edges)

        difference = []

        # Calculate the difference between each level
        for x in range(len(edge_per_level) - 1):
            difference.append(edge_per_level[x] - edge_per_level[x + 1])

        # Give weight per level. Lower levels have more impact so higher weight
        weighted_sum = 0
        for x in range(len(difference)):
            weighted_sum += difference[x] * (1.0 - ((x - 1.0) / 6.0))

        # Normalize
        try:
            result = [weighted_sum / (edge_per_level[0] - edge_per_level[5])]
        except ZeroDivisionError:
            result = [0]

            print("#################HCI_Rule15_Figure_Ground_Contrast#################")
            print()
            # Detect Edge Congestion
            print("****************************")
            print("Edge Congestion is: ")
            print(result)

        res = ''
        isAccepted = False

        if 0.00 == float(result[0]):
            res = "Normal"
            isAccepted = True
        else:
            res = 'There is something went wrong..'
            isAccepted = False

        fileName = 'HCI_Rule12_Figure_Ground_Contrast'

        return [
            "Figure Ground Contrast",
            "pf",
            isAccepted,
            float(result[0]),
            res,
            fileName
        ]