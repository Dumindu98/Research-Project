import base64
from io import BytesIO

import numpy as np
from PIL import Image
from skimage import color, util


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        img = np.array(img)
        img = util.img_as_ubyte(img)

        # Convert the LAB space
        lab = color.rgb2lab(img)

        L = lab[:, :, 0]
        A = lab[:, :, 1]
        B = lab[:, :, 2]

        # Get average and standard deviation for each value separately
        meanL = np.mean(L)
        stdL = np.std(L)
        meanA = np.mean(A)
        stdA = np.std(A)
        meanB = np.mean(B)
        stdB = np.std(B)

        result = [meanL, stdL, meanA, stdA, meanB, stdB]

        print("#################HCI_Rule_04_Average_of_LAB#################")
        print()

        meanLight = ''
        sdLight = ''
        meanA = ''
        sdA = ''
        meanB = ''
        sdB = ''

        meanLightDoc = ''
        sdLightDoc = ''
        meanADoc = ''
        sdADoc = ''
        meanBDoc = ''
        sdBDoc = ''


        # Detect Mean Lightness
        print("****************************")
        print("Mean Lightness is: ")
        print(result[0])
        # Check applicability of Mean Lightness (float)
        if 0.00 <= float(result[0]) <= 40.00:
            meanLightDoc = 'HCI_Rule4_Average_of_LAB'
            meanLight = "Dark"
            print("Dark")
        elif 40.01 <= float(result[0]) <= 75.00:
            meanLight = "Medium"
            print("Medium")
        elif 75.01 <= float(result[0]) <= 100.00:
            meanLight = "Light"
            print("Light")

        # Detect Standard Deviation Lightness (float),
        print("Standard Deviation Lightness is: ")
        print(result[1])
        # Check applicability of Standard Deviation Lightness (float)
        if 0.00 <= float(result[1]) <= 15.00:
            sdLightDoc = 'HCI_Rule4_Average_of_LAB'
            sdLight = "Low"
            print("Low")
        elif 15.01 <= float(result[1]) <= 35.00:
            sdLight = "Medium"
            print("Medium")
        elif 35.01 <= float(result[1]) <= 100.00:
            sdLight = "High"
            print("High")

        print("Mean A (Green-Red Space) is: ")
        print(result[2])
        # Check applicability Mean A (Green-Red Space)  (float)
        if 0.00 == float(result[2]):
            meanADoc = 'HCI_Rule4_Average_of_LAB'
            meanA = "Meaningless"
            print("Meaningless")
        else:
            meanA = "Your interface has Mean A (Green-Red Space)"
            print("Your interface has Mean A (Green-Red Space)")
            print("*********************************************")
            print()

        # Detect Standard Deviation A
        print("Standard Deviation A is: ")
        print(result[3])
        # Check applicability Standard Deviation A  (float)
        if 0.00 == float(result[3]):
            sdA = "Meaningless"
            sdADoc = 'HCI_Rule4_Average_of_LAB'
            print("Meaningless")
        else:
            sdA = "Standard Deviation A"
            print("Standard Deviation A")
            print("*********************************************")
            print()

        # Detect Mean B (Yellow-Blue Space) (float),
        print("Mean B (Yellow-Blue Space) is: ")
        print(result[4])
        # Check Mean B (Yellow-Blue Space) (float)
        if 0.00 == float(result[4]):
            meanBDoc = 'HCI_Rule4_Average_of_LAB'
            meanB = "Meaningless"
            print("Meaningless")
        else:
            meanB = "Your interface has Mean B (Yellow-Blue Space)"
            print("Your interface has Mean B (Yellow-Blue Space)")
            print("*********************************************")
            print()

        # Detect Standard Deviation B (float),
        print("Standard Deviation B is: ")
        print(result[5])
        # Check Applicability of Standard Deviation B (float)
        if 0.00 == float(result[5]):
            sdB = "Meaningless"
            sdBDoc = 'HCI_Rule4_Average_of_LAB'
            print("Meaningless")
        else:
            sdB = "Your interface has Standard Deviation B"
            print("Your interface has Standard Deviation B")
            print("*********************************************")
            print()

        return [
            "Average of LAB", "cp",
            ["Mean Lightness", result[0], meanLight, meanLightDoc],
            ["Standard Deviation Lightness", result[1], sdLight, sdLightDoc],
            ["Mean A (Green-Red Space)", result[2], meanA, meanADoc],
            ["Standard Deviation A", result[3], sdA, sdADoc],
            ["Mean B (Yellow-Blue Space)", result[4], meanB, meanBDoc],
            ["Standard Deviation B", result[5], sdB, sdBDoc]
        ]
