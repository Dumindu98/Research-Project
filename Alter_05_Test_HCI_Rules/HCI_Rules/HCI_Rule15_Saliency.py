import base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from Alter_Backend.Alter_05_Test_HCI_Rules.HCI_Rules import pySaliencyMap


class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):
        plt.switch_backend('AGG')
        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)

        img = Image.open(imgPath)
        img = np.array(img)

        # Initialize
        imgsize = img.shape
        img_width = imgsize[1]
        img_height = imgsize[0]
        sm = pySaliencyMap.pySaliencyMap(img_width, img_height)

        # Computation
        saliency_map = sm.SMGetSM(img)

        image_string = BytesIO()
        plt.imsave(image_string, saliency_map, cmap='Greys')

        base64Img = base64.b64encode(image_string.getvalue()).decode('utf-8')

        print(">>>> bas64 : ", base64Img)

        isAccepted = True
        desc = 'An overview of the most salient places on the interface.'
        title = 'Saliency'

        return ['Saliency', 'vg', isAccepted, 'image', [{'src': base64Img, 'desc': desc, 'title': title}]]


