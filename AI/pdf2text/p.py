import easyocr
reader = easyocr.Reader(['fa'])
result = reader.readtext('1.pdf')
for detection in result:
    print(detection[1])  # متن فارسی استخراج شده
