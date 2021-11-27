import base64
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

        rg = []
        yb = []
        for item in img:
            [r, g, b] = [int(item[0]), int(item[1]), int(item[2])]
            # These formulae are proposed in Hasler, D. and Susstrunk, S. Measuring Colourfuness in Natural Images. (2003)
            rg.append(np.abs(r - g))
            yb.append(np.abs((0.5 * (r + g)) - b))

        meanRG = np.mean(rg)
        stdRG = np.std(rg)
        meanYB = np.mean(yb)
        stdYB = np.std(yb)
        meanRGYB = np.sqrt(meanRG ** 2 + meanYB ** 2)
        stdRGYB = np.sqrt(stdRG ** 2 + stdYB ** 2)

        # Proposed in the same paper
        colourfulness = stdRGYB + 0.3 * meanRGYB

        result = [meanRG, stdRG, meanYB, stdYB, meanRGYB, stdRGYB, colourfulness]

        meanRGDoc = ''
        stdRGDoc = ''
        meanYBDoc = ''
        stdYBDoc = ''
        meanRGYBDoc = ''
        stdRGYBDoc = ''
        colourfulnessDoc = ''

        print("#################HCI_Rule_05_Average_of_LAB#################")
        print()

        # Mean Distribution (Red-Green)
        print("Mean Distribution (Red-Green) (float)is: ")
        print(result[0])
        # Check applicability Check Applicability of Mean Distribution (Red-Green) (float)
        if 0.00 == float(result[0]):
            meanRG = 'Meaningless'
            meanRGDoc = 'HCI_Rule5_Hassler_Sustrunk'
            print("Meaningless")
        else:
            meanRG = 'Your interface has Mean Distribution (Red-Green)'
            print("Your interface has Mean Distribution (Red-Green) (float)")
            print("*********************************************")
            print()
        # Standard Deviation Distribution (Red-Green) (float)
        print("Standard Deviation Distribution (Red-Green) (float) is: ")
        print(result[1])
        # Check applicability Standard Deviation A  (float)
        if 0.00 == float(result[1]):
            stdRG = 'Meaningless'
            stdRGDoc = 'HCI_Rule5_Hassler_Sustrunk'
            print("Meaningless")
        else:
            stdRG = 'Standard Deviation Distribution (Red-Green)'
            print("Standard Deviation Distribution (Red-Green)")
            print("*********************************************")
            print()

        # Mean Distribution (Yellow-Blue) (float),
        print("Mean B (Yellow-Blue Space) is: ")
        print(result[2])
        # Check Mean Distribution (Yellow-Blue) (float)
        if 0.00 == float(result[2]):
            meanYB = 'Meaningless'
            meanYBDoc = 'HCI_Rule5_Hassler_Sustrunk'
            print("Meaningless")
        else:
            meanYB = 'Your interface has Mean Distribution (Yellow-Blue)'
            print("Your interface has Mean Distribution (Yellow-Blue) (float)")
            print("*********************************************")
            print()

        # Standard Deviation Distribution (Yellow-Blue) (float),
        print("Standard Deviation B is: ")
        print(result[3])
        # Check Applicability of Standard Deviation Distribution (Yellow-Blue) (float),
        if 0.00 == float(result[3]):
            stdYB = 'Meaningless'
            stdYBDoc = 'HCI_Rule5_Hassler_Sustrunk'
            print("Meaningless")
        else:
            stdYB = 'Your interface has Standard Deviation Distribution (Yellow-Blue)'
            print("Your interface has Standard Deviation Distribution (Yellow-Blue) (float),")
            print("*********************************************")
            print()

        # Mean Distribution (RGYB) (float)
        print("Standard Deviation B is: ")
        print(result[4])
        # Check Applicability of Mean Distribution (RGYB) (float)
        if 0.00 == float(result[4]):
            meanRGYB = 'Meaningless'
            print("Meaningless")
        else:
            meanRGYB = 'Your interface has Standard Deviation Distribution (Yellow-Blue)'
            print("Your interface has Standard Deviation Distribution (Yellow-Blue) (float),")
            print("*********************************************")
            print()

        #  Standard Distribution (RGYB) (float),
        print(" Mean Distribution (RGYB) (float) is: ")
        print(result[5])
        # Check applicability of  Standard Deviation Distribution (RGYB) (float),
        if 0.00 == float(result[5]):
            stdRGYB = 'Meaningless'
            stdRGYBDoc = 'HCI_Rule5_Hassler_Sustrunk'
            print("Meaningless")
        else:
            stdRGYB = 'Your interface has Standard Deviation Distribution (RGYB)'
            print("Your interface has Standard Deviation Distribution (RGYB) (float)")
            print("*********************************************")
            print()

        # Detect Mean Lightness
        print("****************************")
        print("Mean Lightness is: ")
        print(result[6])
        # Check applicability of Mean Lightness (float)
        if 0.00 <= float(result[6]) <= 50.00:
            colourfulness = 'Less Colourful'
            colourfulnessDoc = 'HCI_Rule5_Hassler_Sustrunk'
            print("Less colourful")
        elif 50.01 <= float(result[6]) <= 100.00:
            colourfulness = 'Fair'
            print("Fair")
        elif 100.01 <= float(result[6]):
            colourfulness = 'Colourful'
            print("colourful")

        return [
            "Hassler Sustrunk", "cp",
            ["Mean Distribution (Red-Green)", result[0], meanRG, meanRGDoc],
            ["Standard Deviation Distribution (Red-Green)", result[1], stdRG, stdRGDoc],
            ["Mean Distribution (Yellow-Blue) ", result[2], meanYB, meanYBDoc],
            ["Standard Deviation Distribution (Yellow-Blue)", result[3], stdYB, stdYBDoc],
            ["Mean Distribution (RGYB)", result[4], meanRGYB, meanRGYBDoc],
            ["Standard Distribution (RGYB)", result[5], stdRGYB, stdRGYBDoc],
            ["Mean Lightness", result[6], colourfulness,colourfulnessDoc]
        ]
