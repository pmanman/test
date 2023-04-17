"""
*_* coding: utf-8 *_*
author:zmm
time:2022/10/19 8:54
file :英雄联盟抓取英雄.py
"""
import requests
import json
img_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big'
#请求地址
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=29'
#请求头
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
#发送 请求requests.get()

response = requests.get(url, headers=header)
#获取网页源码
page = response.text
# print(page)
#网页源码不是html数据，不需要xpath解析
#反序列化------字典
info = json.loads(page)
# print(type(info))
# print(info)
heros = info['hero']  # 字典取值  列表
for hero in heros:
    heroId = hero['heroId']
    name = hero['name']
    alias = hero['alias']
    print(heroId, name, alias)
    # 将数据存入 csv文件
    #自己拼接路由看皮肤图片怎么获取
    # img_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big'
    # skin_img = img_link + heroId + '000.jpg'
    # # 请求图片链接
    # skin_res = requests.get(skin_img, headers=header)
    # # 将图片写到本地   -----对于图片和视频 （二进制）
    # with open(f'img/{name}.jpg', 'ab') as f:
    #     f.write(skin_res.content)
    #     pass
    #一个英雄的多个皮肤
    for k in range(5):
        result_url = img_link + heroId + '%03d' % k + '.jpg'  # '%03d'%k[000到009]
        # if k <=9:
        #     s = '00'+str(k)
        # else:
        #     s = '0'+str(k)
        # 3.保存图片
        img = requests.get(result_url)
        if img.status_code == 200:
            with open('img/%s%d.jpg' % (alias, k), 'wb') as f:
                # img.content 就是写入图片的二进制数据
                f.write(img.content)


