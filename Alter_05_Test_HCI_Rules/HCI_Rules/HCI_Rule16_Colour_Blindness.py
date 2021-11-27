from io import StringIO
import numpy
import base64
from PIL import Image
from io import BytesIO

class HCI_Rule:
    def __init__(self, imageName):
        self.imageName = imageName

    def run(self):

        imgPath = 'Alter_Backend/Alter_05_Test_HCI_Rules/generated_web_ui/'.__add__(self.imageName)
        img = Image.open(imgPath)
        im = img.convert('RGB')
        RGB = numpy.asarray(im, dtype=float)

        # Transformation matrix for Deuteranope (a form of red/green color deficit)
        deut_matrix = numpy.array(
            [[0.457771, 0.731899, -0.189670],
             [0.226409, 0.731012, 0.042579],
             [-0.011595, 0.034333, 0.977261]]
        )
        # Transformation matrix for Protanope (another form of red/green color deficit)
        prot_matrix = numpy.array(
            [[0.319627, 0.849633, -0.169261],
             [0.106241, 0.815969, 0.077790],
             [-0.007025, -0.028051, 1.035076]]
        )
        # Transformation matrix for Tritanope (a blue/yellow deficit - very rare)
        trit_matrix = numpy.array(
            [[1.255528, -0.076749, -0.178779],
             [-0.078411, 0.930809, 0.147602],
             [0.004733, 0.691367, 0.303900]]
        )

        # Transform the image using each matrix
        rgb_d = numpy.zeros_like(RGB)
        rgb_p = numpy.zeros_like(RGB)
        rgb_t = numpy.zeros_like(RGB)
        for i in range(RGB.shape[0]):
            for j in range(RGB.shape[1]):
                rgb = RGB[i, j, :3]
                rgb_d[i, j, :3] = numpy.dot(deut_matrix, rgb)
                rgb_p[i, j, :3] = numpy.dot(prot_matrix, rgb)
                rgb_t[i, j, :3] = numpy.dot(trit_matrix, rgb)


        # Make sure that all numbers are within 0-255 due to conversions
        for i in range(RGB.shape[0]):
            for j in range(RGB.shape[1]):
                rgb_d[i, j, 0] = max(0, rgb_d[i, j, 0])
                rgb_d[i, j, 0] = min(255, rgb_d[i, j, 0])
                rgb_d[i, j, 1] = max(0, rgb_d[i, j, 1])
                rgb_d[i, j, 1] = min(255, rgb_d[i, j, 1])
                rgb_d[i, j, 2] = max(0, rgb_d[i, j, 2])
                rgb_d[i, j, 2] = min(255, rgb_d[i, j, 2])

                rgb_p[i, j, 0] = max(0, rgb_p[i, j, 0])
                rgb_p[i, j, 0] = min(255, rgb_p[i, j, 0])
                rgb_p[i, j, 1] = max(0, rgb_p[i, j, 1])
                rgb_p[i, j, 1] = min(255, rgb_p[i, j, 1])
                rgb_p[i, j, 2] = max(0, rgb_p[i, j, 2])
                rgb_p[i, j, 2] = min(255, rgb_p[i, j, 2])

                rgb_t[i, j, 0] = max(0, rgb_t[i, j, 0])
                rgb_t[i, j, 0] = min(255, rgb_t[i, j, 0])
                rgb_t[i, j, 1] = max(0, rgb_t[i, j, 1])
                rgb_t[i, j, 1] = min(255, rgb_t[i, j, 1])
                rgb_t[i, j, 2] = max(0, rgb_t[i, j, 2])
                rgb_t[i, j, 2] = min(255, rgb_t[i, j, 2])

        # Save as image into buffer
        sim_d = rgb_d.astype('uint8')
        sim_p = rgb_p.astype('uint8')
        sim_t = rgb_t.astype('uint8')
        im_d = Image.fromarray(sim_d, mode='RGB')
        im_p = Image.fromarray(sim_p, mode='RGB')
        im_t = Image.fromarray(sim_t, mode='RGB')
        d_string = BytesIO()
        p_string = BytesIO()
        t_string = BytesIO()
        im_d.save(d_string, format="PNG")
        im_p.save(p_string, format="PNG")
        im_t.save(t_string, format="PNG")

        # Encode it as base64
        d_b64 = base64.b64encode(d_string.getvalue()).decode('utf-8')
        p_b64 = base64.b64encode(p_string.getvalue()).decode('utf-8')
        t_b64 = base64.b64encode(t_string.getvalue()).decode('utf-8')

        d_string.close()
        p_string.close()
        t_string.close()

        isAccepted = True
        d_desc = 'Red-green colour blindness, lacking red cones.'
        p_desc = 'Red-green colour blindness, lacking green cones.'
        t_desc = 'Blue-yellow colour blindness.'

        d_title = 'Deuteranopia'
        p_title = 'Protanopia'
        t_title = 'Tritanopia'

        return ['Color Blindness', 'ac', isAccepted, 'image',
                [
                    {'src': d_b64, 'desc': d_desc, 'title': d_title},
                    {'src': p_b64, 'desc': p_desc, 'title': p_title},
                    {'src': t_b64, 'desc': t_desc, 'title': t_title}
                ]]

