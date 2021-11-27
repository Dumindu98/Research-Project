import base64
import threading
from io import BytesIO

import numpy as np
from PIL import Image
from skimage import color, util


# Hue is an angle, so cannot simple add and average it
class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        h = []

        def sind(x):
            y = np.sin(np.deg2rad(x))
            y = np.rad2deg(y)
            return y

        def cosd(x):
            y = np.cos(np.deg2rad(x))
            y = np.rad2deg(y)
            return y

        def atan2d(x, y):
            z = np.arctan2(np.deg2rad(x), np.deg2rad(y))
            z = np.rad2deg(z)
            return z

        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        img = np.array(img)
        img = util.img_as_ubyte(img)
        img = img / 255.  # this division is needed to get proper values. for hue, saturation and value (0 to 360, 0 to 1,0 to 1)
        img = color.rgb2hsv(img)
        img = img.reshape(-1, 3)
        img = [tuple(l) for l in img]

        h = []
        s = []
        v = []

        # Give each channel its own list
        for items in img:
            [hue, sat, val] = [items[0], items[1], items[2]]
            h.append(hue * 360)
            s.append(sat)
            v.append(val)

        # Hue is an angle, so cannot simple add and average it
        sumsin = sum(sind(h[:]))
        sumcos = sum(cosd(h[:]))

        # Get the average value and standard deviation over H,S and V
        avgHue = atan2d(sumsin, sumcos) % 360
        avgSaturation = np.mean(s)
        stdSaturation = np.std(s)
        avgValue = np.mean(v)
        stdValue = np.std(v)
        result = [avgHue, avgSaturation, stdSaturation, avgValue, stdValue]

        avgHueDoc = ''
        avgSatDoc = ''
        stdSatDoc = ''
        avgValDoc = ''
        stdValDoc = ''

        isAvgHueAccepted = False
        isAvgSatAccepted = False
        isStdSatAccepted = False
        isAvgValueAccepted = False
        isStdValueAccepted = False
        isAccepted = False

        #
        print("#################HCI_Rule_02_Average_of_HSV#################")
        # print()
        # # Detect Average HUE Metrics
        # print("****************************")
        print("Average HUE is: ")
        # print(result[0])
        #
        # Check applicability of Average HUE Metrics
        if 0.00 == float(result[0]):
            avgHueDoc = 'HCI_Rule2_Average_of_HSV_AverageHue'
            avgHue = "Meaningless"
            isAvgHueAccepted = False
            print("Meaningless")
        else:
            avgHue = "Your interface has average HUE"
            isAvgHueAccepted = True
            print("Your interface has average HUE")
        #
        # # Detect Average Saturation Metrics
        # print("****************************")
        print("Average Saturation is: ")
        print(result[1])
        #
        # # Check applicability of Average Saturation
        if 0.00 <= float(result[1]) <= 0.10:
            avgSatDoc = 'HCI_Rule2_Average_of_HSV_AverageSaturation'
            avgSaturation = "Low average of Saturation"
            isAvgSatAccepted = False
            print("Low average of Saturation")
        elif 0.11 <= float(result[1]) <= 0.61:
            avgSaturation = "Medium average of Saturation"
            print("Medium average of Saturation")
            isAvgSatAccepted = True
        elif 0.61 <= float(result[1]):
            avgSaturation = "High average of Saturation"
            print("High average of Saturation")
            isAvgSatAccepted = True

        # # Detect Average Standard Saturation Metrics
        # print("****************************")
        print("Average std Saturation is: ")
        # print(result[2])
        #
        # # Check applicability of Standard Deviation Saturation
        if 0.00 <= float(result[2]) <= 0.20:
            stdSatDoc = 'HCI_Rule2_Average_of_HSV_StandardDeviationSaturation'
            stdSaturation = "Low average of Std Saturation"
            isStdSatAccepted = False
            print("Low average of Std Saturation")
        elif 0.21 <= float(result[2]) <= 0.40:
            stdSaturation = "Medium average of Std Saturation"
            isStdSatAccepted = True
            print("Medium average of std Saturation")
        elif 0.41 <= float(result[2]):
            stdSaturation = "High average of Std Saturation"
            isStdSatAccepted = True
            print("High average of std Saturation")

        print("Average Value is: ")
        print(result[3])
        # Check applicability of Average Value

        if 0.00 <= float(result[1]) <= 0.40:
            avgValDoc = 'HCI_Rule2_Average_of_HSV_AverageValue'
            avgValue = "Dark"
            isAvgValueAccepted = False
            print("Low average of Saturation")
        elif 0.41 <= float(result[1]) <= 0.80:
            avgValue = "Medium"
            print("Medium average of Value")
            isAvgValueAccepted = True
        elif 0.81 <= float(result[1]):
            avgValue = "High average of Value"
            isAvgValueAccepted = True
            print("Light")

        if 0.00 <= float(result[1]) <= 0.15:
            stdValue = "Low"
            stdValDoc = 'HCI_Rule2_Average_of_HSV_StandardDeviationValue'
            isStdValueAccepted = False
            print("Low")
        elif 0.16 <= float(result[1]) <= 0.35:
            stdValue = "Medium"
            print("Medium")
            isStdValueAccepted = True
        elif 0.36 <= float(result[1]):
            stdValue = "High"
            stdValDoc = 'HCI_Rule2_Average_of_HSV_StandardDeviationValue'
            isStdValueAccepted = False
            print("Light")

        if isAvgHueAccepted and isAvgSatAccepted and isStdSatAccepted and isAvgSatAccepted and isStdValueAccepted:
            isAccepted = True

        return ["Average of HSV", "cp", isAccepted,
                ["Average HUE", result[0], avgHue, avgHueDoc],
                ["Average Standard Saturation", result[1], avgSaturation, avgSatDoc],
                ["Standard Deviation Saturation", result[2], stdSaturation, stdSatDoc],
                ['Average Value', result[3], avgValue, avgValDoc],
                ['Standard Deviation of Value', result[4], stdValue, stdValDoc]
                ]
