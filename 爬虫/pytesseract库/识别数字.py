"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/21 16:36
file :识别数字.py
"""
import pytesseract
from PIL import Image
img = Image.open('1.jpg')
# 对于数字，无论给中文还是英文都可以
# text = pytesseract.image_to_string(img, lang='chi_sim')
# print(text)
# 高版本
code = pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(code)