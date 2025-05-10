from pdf2image import convert_from_path
import pytesseract
images = convert_from_path('2.pdf')
text = ""
for image in images:
	text += pytesseract.image_to_string(image, lang = 'fas')
print (text)
