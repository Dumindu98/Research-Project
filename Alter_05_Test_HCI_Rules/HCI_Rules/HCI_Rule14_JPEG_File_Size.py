import base64
from io import BytesIO
import cv2
from PIL import Image


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)

        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())

        jpg_size = int(len(img_str) * 0.75)

        print("#################HCI_Rule21_JPG_File_Size#################")
        print()
        # Detect JPEG file size
        print("****************************")
        print("JPEG file size is: ")
        print(jpg_size)

        res = ''
        documentName = ''
        isAccepted = False

        # Check applicability of png_size
        if 0 <= int(jpg_size) <= 100000:
            res = 'Suitable'
            isAccepted = True
            print("Suitable")
        elif 100001 <= int(jpg_size) <= 200000:
            res = 'Fair'
            isAccepted = True
            print("Fair")
        elif 200001 <= int(jpg_size):
            res = 'Huge'
            isAccepted = False
            documentName = 'HCI_Rule14_JPEG_File_Size'
            print("Huge")

        return [
            "JPEG File Size",
            "pf",
            isAccepted,
            jpg_size,
            res,
            documentName
        ]
