#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
import time

url = 'https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1614174646181'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
html = requests.get(url, headers=headers).content.decode()
print(html)
comments_list = list()
totalcom = int(re.findall('"oritotal":(.*?),', html, re.S)[0])
print(totalcom)
rangetime = round((totalcom - 10) / 10) + 1
print(rangetime)
t = int(time.time())
print(t)
now = t + 3
n = 1
m = 1
print(now, n, m)
cursor = 0

# 获取评论
for i in range(rangetime):
    print("爬取第{}页的评论".format(str(m)))
    url_content = 'https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + str(
        cursor) + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=' + str(t)
    html = requests.get(url_content, headers=headers).content.decode()
    contents = re.findall('"content":"(.*?)"', html, re.S)[0]
    cursor = re.findall(',"last":"(.*?)",', html, re.S)[0]
    m += 1
    t = now
    now += 1
    comments_list.append(contents)
# 写入txt文档
with open("评论.txt", "w", encoding="GBK", errors="ignore") as f:
    for i in comments_list:
        f.write(str(i))
        f.write("\n")