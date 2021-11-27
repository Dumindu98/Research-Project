
import base64
from io import BytesIO
import numpy as np
from PIL import Image
from skimage import util


class HCI_Rule:
    def __init__(self, imageName, value1, value2, value3,):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        img = np.array(img)
        img = util.img_as_ubyte(img)
        img = img.reshape(-1, 3)
        img = [tuple(l) for l in img]

        print("value1: ", self.value1)
        print("value2: ", self.value2)
        print("value3: ", self.value3)

        lum = []
        for pixel in img:
            # Based on: https://en.wikipedia.org/wiki/Luma_(video)
            y = float(self.value1) * pixel[0] + float(self.value2) * pixel[1] + float(self.value3) * pixel[2]
            lum.append(y)

        result = np.std(lum)

        print("#################HCI_Rule8_Standard_Deviation_in_Luminance#################")
        print()
        print("Standard deviation of luminance : ")
        print(result)

        res = ""
        documentName = ''

        if 0.00 <= float(result) <= 60.00:
            res = "Good"
            print("Good")
        elif 60.01 <= float(result) <= 90.00:
            res = "Acceptable"
            print("Acceptable")
        elif 90.01 <= float(result):
            res = "Potential varied"
            documentName = 'HCI_Rule8_Standard_Deviation_in_Luminance'
            print("Potential varied")

        return ["Standard Deviation in Luminance", "cp", result, res, documentName]
