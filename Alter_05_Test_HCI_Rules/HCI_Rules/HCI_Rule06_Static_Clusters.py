import base64
import collections
import math
from io import BytesIO

import numpy as np
from PIL import Image
from skimage import util


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        img = np.array(img)
        img = util.img_as_ubyte(img)
        img = img.reshape(-1, 3)
        img = [tuple(l) for l in img]

        hist = collections.Counter(img)
        hist = hist.items()
        cluster = np.zeros((64, 64, 64))
        # print("cluster : ", cluster)
        for x in hist:
            rc = int(math.ceil((x[0][0] / 8) + 1)) - 1
            gc = int(math.ceil((x[0][1] / 8) + 1)) - 1
            bc = int(math.ceil((x[0][2] / 8) + 1)) - 1
            cluster[rc, gc, bc] += x[1]

        result = (cluster > 5).sum()

        print("#################HCI_Rule6_Static_Clusters#################")
        print()

        # Mean Distribution (Red-Green)
        print("number of static 32 - sized  color clusters: ")
        print(result)

        color = ''
        fileName = ''
        isAccepted = False

        if 0 <= float(result) <= 4000:
            color = 'Less Colourful'
            fileName = 'HCI_Rule6_Static_Clusters'
            isAccepted = False
            print("Less colourful")
        elif 4001 <= float(result) <= 8000:
            color = "Fair"
            isAccepted = True
            print("Fair")
        elif 8001 <= float(result):
            color = "Colourful"
            isAccepted = True
            print("Colourful")

        return [
            "Static Cluster",
            "cp",
            isAccepted,
            float(result),
            color,
            fileName
        ]
