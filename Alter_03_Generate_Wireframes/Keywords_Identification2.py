import easyocr
reader = easyocr.Reader(['en'])

results = reader.readtext('../../static/img/Class Diagram.png')

text = ''
for result in results:
    text += result[1] + ' '

print(text)
