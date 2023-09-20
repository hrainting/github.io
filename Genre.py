import json
import re
import time
import pandas as pd
import numpy as np
from collections import Counter
import collections
import random
import requests
import csv
from lxml import etree
headers = {'User-Agent':'SteamDB-Educational-Access; 202011080114@stu.zuel.edu.cn'}

df=pd.read_csv('Tag_divide_mergy.csv')


    
fail_id_lst = []

# for i in df[df.index>22437]['AppID']:

#     url = 'https://steamdb.info/app/' + str(i) + '/info/'
#     html_data = requests.get(url,headers=headers,timeout=20)
#     status = html_data.status_code
#     count=0
    
#     while status == 429: ##Too Many Requests or Can not find '/depots/'
#         time.sleep(300)
#         html_data = requests.get(url,headers=headers,timeout=20)
#         status = html_data.status_code
#         if count==3:
#             print("Your ip address has been banned!",i)
#             fail_id_lst.append([i,df[df['AppID']==i].index])
#             break
#         count+=1               
#     else:
#         if html_data.status_code == 200:
#             Html = html_data.text
#             etree_data = etree.HTML(Html)
            
#             Genre=etree_data.xpath('//td[contains(text(),"Primary Genre")]/../td[2]/text()')

#             if len(Genre)!=0:
#                 x = Genre[0]
#             else:
#                 x = 'NaN'

#             print([i,x])

#             with open('primary.csv','a',newline='') as f:
#                 writer = csv.writer(f)  #创建初始化写入对象
#                 writer.writerow([i,x])
#         else:   
#             fail_id_lst.append(i)
#     time.sleep(1)
    
# print ("End: %s" % time.ctime())  