"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/21 16:10
file :识别中文.py
"""
import pytesseract
from PIL import Image
# 打开图片实例化图片
img = Image.open('gushi.jpg')
# 识别中文lang="chi_sim"（简体中文）
text = pytesseract.image_to_string(img, lang="chi_sim")
print(text)

# 导包
import pytesseract
from PIL import Image
# 打开图片
img = Image.open('2.jpg')
# 提取图片里的信息
# lang= 'chi_sim'(简体中文) chi_tra(繁体)
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)