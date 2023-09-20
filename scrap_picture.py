import json
import re
import time
import pandas as pd
import numpy as np
from collections import Counter
import collections
import random
import requests
# from lxml import etree
headers = {'User-Agent':'SteamDB-Educational-Access; 202011080114@stu.zuel.edu.cn'}

df=pd.read_csv('games2.csv')
fail=pd.read_csv('fail_id.csv')
fail2=pd.read_csv('fail2_id.csv')
fail3=pd.read_csv('fail3_id.csv')
#下载图片
def download_img(i,img_url):
#下载图片存储的路径
    path = r'D://paper//game//data//pictures//'
    r = requests.get(img_url,headers,stream=True)
    # print(r.status_code) # 返回状态码
    if r.status_code == 200:
        # 截取图片文件名
        img_name = str(i)+'.jpg'
        with open(path+'./'+str(img_name), 'wb') as f:
            f.write(r.content)
        return True
    

    
    
# print ("End: %s" % time.ctime())  


for i in fail3[fail3.index>38]['Appid']:
    download_img(i,'https://cdn.cloudflare.steamstatic.com/steam/apps/'+str(i)+'/header.jpg')
    time.sleep(1)
    print(str(i)+",success")