"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/21 15:45
file :识别英文.py
"""
import pytesseract
from PIL import Image
# 打开图片，获取图片实例化
img = Image.open('5.png')
# 提取图片里的信息
# lang默认为英文（lang='eng'）
text = pytesseract.image_to_string(img)
print(text)