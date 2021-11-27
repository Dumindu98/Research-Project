import base64
from io import BytesIO
import cv2
from PIL import Image

image = cv2.imread('car.png')


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)

        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())

        png_size = int(len(img_str) * 0.75)

        print("#################HCI_Rule20_PNG_File_Size#################")
        print()
        # Detect png file size
        print("****************************")
        print("PNG file size is: ")
        print(png_size)

        res = ''
        documentName = ''
        isAccepted = False

        # Check applicability of png_size
        if 0 <= int(png_size) <= 500000:
            res = 'Suitable'
            isAccepted = True
            print("Suitable")
        elif 500001 <= int(png_size) <= 1200000:
            res = 'Fair'
            isAccepted = True
            print("Fair")
        elif 1200001 <= int(png_size):
            res = 'Huge'
            isAccepted = False
            documentName = 'HCI_Rule13_PNG_File_Size'
            print("Huge")

        return [
            "PNG File Size",
            "pf",
            isAccepted,
            png_size,
            res,
            documentName
        ]
