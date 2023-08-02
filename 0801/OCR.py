# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:08:21 2023

@author: USER
"""

from PIL import Image
import pytesseract

fileName = 'images.jpg'
#雙引號前面的r表示忽略特殊符號判斷
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open(fileName)
text = pytesseract.image_to_string(img,lang='eng',config='--psm 12')
print(text.strip())