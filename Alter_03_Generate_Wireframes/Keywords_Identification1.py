# Import files
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Sapthaka Godage\AppData\Local\Programs\Tesseract-OCR\tesseract'
from PIL import Image

# Import the image to the system
img = Image.open('../../static/img/Class Diagram.png')
text = tess.image_to_string(img)

print(text)