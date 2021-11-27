import threading
import time

from PIL import Image


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        print(imgPath)

        img = Image.open(imgPath)
        uniqueColors = set()

        w, h = img.size
        for x in range(w):
            for y in range(h):
                pixel = img.getpixel((x, y))
                uniqueColors.add(pixel)

        totalUniqueColors = len(uniqueColors)
        print("#################HCI_Rule_01_Number_of_Colors#################")
        print()
        print("Number of color is:")
        print(totalUniqueColors)

        result = ''
        fileName = ''
        isAccepted = False

        # time.sleep(1)
        if 0 <= int(totalUniqueColors) <= 5000:
            result = "Less Colourful"
            fileName = 'HCI_Rule1_Number_of_Colors'
            isAccepted = False
            print("less colourful")
        elif 5001 <= int(totalUniqueColors) <= 15000:
            result = "Fair"
            isAccepted = True
            print("fair")
        elif 15001 <= int(totalUniqueColors):
            result = "Colourful"
            isAccepted = True
            print("colourful")

        return ["No of Colors", "cp", isAccepted, totalUniqueColors, result, fileName]
