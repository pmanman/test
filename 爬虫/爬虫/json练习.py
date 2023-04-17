"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/8 11:28
file :json练习.PY
"""
import json
z = "中文abc123"
a = json.dumps(z)
print(a)
print(json.loads(a))

p = {"name": "图图"}
b = json.dumps(p)
print(b)

# 1.json 花扣号，双引号
# 2.内置模块，不需要安装，可以直接导入使用
# 3.内置四个方法，dumps(), dump(), loads(), load()

