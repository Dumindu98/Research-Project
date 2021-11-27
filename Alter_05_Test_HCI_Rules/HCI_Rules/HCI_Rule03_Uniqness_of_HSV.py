from skimage import color, util
import collections
import numpy as np
import base64
from PIL import Image
from io import BytesIO


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        img = np.array(img)
        img = util.img_as_ubyte(img)
        img = color.rgb2hsv(img)
        img = img.reshape(-1, 3)
        img = [tuple(l) for l in img]

        hist = collections.Counter(img)
        hist = hist.items()

        hsv_unique = []
        count = []
        h = []
        s = []
        v = []

        for x in hist:
            add = x[0][0], x[0][1], x[0][2]
            hsv_unique.append(add)
            count.append(x[1])
            h.append(x[0][0])
            s.append(x[0][1])
            v.append(x[0][2])

        # Get all unique values, still has all counts (so no minimal occurence). This probably needs some changing in
        # the future
        h_unique = np.unique(h)
        s_unique = np.unique(s)
        v_unique = np.unique(v)

        new_hsv = []

        # Only often enough occuring values for hsv
        for x in range(len(hsv_unique)):
            if count[x] > 5:
                new_hsv.append(hsv_unique[x])

        # Returns: List of 4 items: Number of Unique HSV (int), Number of Unique Hue (int), Number of Unique
        # Saturation (int), Number of Unique Value (int)

        result = [len(new_hsv), len(h_unique), len(s_unique), len(v_unique)]

        print("#################HCI_Rule3_Uniqueness_of_HSV#################")
        print()

        noOfUniqueHSV = ''
        noOfUniqueHue = ''
        noOfUniqueSat = ''
        noOfUniqueVal = ''

        noOfUniqueHSVDoc = ''
        noOfUniqueHueDoc = ''
        noOfUniqueSatDoc = ''
        noOfUniqueValDoc = ''

        isNoOfUniqueHSVAccepted = False
        isNoOfUniqueHueAccepted = False
        isNoOfUniqueSatAccepted = False
        isNoOfUniqueValAccepted = False
        isAccepted = False

        # Detect Number of Unique HSV (int)
        print("****************************")
        print("Number of Unique HSV (int) is: ")
        print(result[0])
        # Check applicability of Number of Unique HSV (int)
        if 0 <= int(result[0]) <= 20000:
            noOfUniqueHSV = 'Good'
            isNoOfUniqueHSVAccepted = True
            print("Good")
        elif 20001 <= float(result[0]):
            noOfUniqueHSVDoc = 'HCI_Rule3_Uniqness_of_HSV'
            noOfUniqueHSV = 'Potential Varied'
            isNoOfUniqueHSVAccepted = False
            print("Potential varied")


        # Detect Number of Unique Hue (int)
        print("****************************")
        print("Number of Unique Hue (int) is: ")
        print(result[1])
        # Check applicability of Number of Unique Hue (int)
        if 0 == int(result[1]):
            noOfUniqueHueDoc = 'HCI_Rule3_Uniqness_of_HSV'
            noOfUniqueHue = 'Meaningless'
            isNoOfUniqueHueAccepted = False
            print("Meaningless")
        else:
            noOfUniqueHue = 'Your interface has average HUE'
            isNoOfUniqueHueAccepted = True
            print("Your interface has average HUE")

        # Detect Number of Unique Saturation (int)
        print("****************************")
        print("Number of Unique Saturation (int) is: ")
        print(result[2])
        # Check applicability of Number of Unique Saturation (int)
        if 0 == int(result[2]):
            noOfUniqueSatDoc = 'HCI_Rule3_Uniqness_of_HSV'
            noOfUniqueSat = 'Meaningless'
            isNoOfUniqueSatAccepted = False
            print("Meaningless")
        else:
            noOfUniqueSat = 'Your interface has Number of Unique Saturation'
            print("Your interface has Number of Unique Saturation ")
            isNoOfUniqueSatAccepted = True

        # Detect Number of Unique Value (int)
        print("****************************")
        print("Number of Unique Value (int) is: ")
        print(result[3])
        # Check applicability of Average Saturation
        if 0 == int(result[3]):
            noOfUniqueValDoc = 'HCI_Rule3_Uniqness_of_HSV'
            noOfUniqueVal = 'Meaningless'
            isNoOfUniqueValAccepted = False
            print("Meaningless")
        else:
            noOfUniqueVal = 'Your interface has Number of Unique Value'
            print("Your interface has Number of Unique Value")
            isNoOfUniqueValAccepted = True

        if isNoOfUniqueHSVAccepted and isNoOfUniqueHueAccepted and isNoOfUniqueSatAccepted and isNoOfUniqueValAccepted:
            isAccepted = True

        return ["Uniqness of HSV", "cp", isAccepted,
                ["Number of Unique HSV", result[0], noOfUniqueHSV, noOfUniqueHSVDoc],
                ["Number of Unique Hue", result[1], noOfUniqueHue, noOfUniqueHueDoc],
                ["Number of Unique Saturation", result[2], noOfUniqueSat, noOfUniqueSatDoc],
                ["Number of Unique Value ", result[3], noOfUniqueVal, noOfUniqueValDoc]
                ]
