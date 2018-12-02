#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:05:16 2018

@author: apple
"""

import requests
from lxml import etree
for j in range(1,5):
    ur1='https://book.douban.com/subject/1084336/comments/hot?p={}'.format(j)
    r=requests.get(ur1).text
    s=etree.HTML(r)
    file=s.xpath('//div[@class="comment"]/p/span/text()')
    with open('pinglun.txt','w',encoding='utf-8')as f:
        for i in file:
            print(i,'\n')
            f.write(i+'\n')
import pandas as pd
df=pd.DataFrame(file)
df.to_excel('小王子评论.xlsx',sheet_name='sheet1')