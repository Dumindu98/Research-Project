import time
from PIL import Image
import os


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        colors = img.getpixel((320, 240))

        print("#################HCI_Rule_11_RGB_Color_Code#################")
        print("RGB color code is: ")
        print(colors)

        return [
            "RGB Color Code",
            "cp",
            colors
        ]

