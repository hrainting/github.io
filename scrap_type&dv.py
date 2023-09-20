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
df=pd.read_csv('games2.csv')

def reNan1(x):
    if len(x) >= 1:
        return x[0]
    else:
        return None
    
def reNan2(x):
    if len(x) ==2:
        return x[1]
    else:
        return None
    
fail_id_lst = []

for i in df[df.index>33832]['AppID']:

    url = 'https://steamdb.info/app/' + str(i) + '/charts/'
    html_data = requests.get(url,headers=headers,timeout=20)
    status = html_data.status_code
    count=0
    while status == 429: ##Too Many Requests or Can not find '/depots/'
        time.sleep(300)
        html_data = requests.get(url,headers=headers,timeout=20)
        status = html_data.status_code
        if count==3:
            print("Your ip address has been banned!",i)
            fail_id_lst.append([i,df[df['AppID']==i].index])
            break
        count+=1               
    else:
        if html_data.status_code == 200:
            Html = html_data.text
            etree_data = etree.HTML(Html)
            Type=etree_data.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/text()')
            
            followers=etree_data.xpath('//*[@id="charts"]/div[5]/div[h3="Store data"]/ul/li[contains(text()," followers")]/strong/text()')
            positive_rev=etree_data.xpath('//*[@id="charts"]/div[5]/div[h3="Store data"]/ul/li[contains(text()," positive reviews")]/strong/text()')
            negative_rev=etree_data.xpath('//*[@id="charts"]/div[5]/div[h3="Store data"]/ul/li[contains(text()," negative reviews")]/strong/text()')
            
            owner1=etree_data.xpath('//*[@id="charts"]/div[5]/div[h3="Owner estimations"]/ul/li[contains(@aria-label,"Steam reviews")]/strong/text()')
            owner2=etree_data.xpath('//*[@id="charts"]/div[5]/div[h3="Owner estimations"]/ul/li[contains(@aria-label,"PlayTracker")]/strong/text()')
            owner3=etree_data.xpath('//*[@id="charts"]/div[5]/div[h3="Owner estimations"]/ul/li[contains(@aria-label,"VG Insights")]/strong/text()')
            owner4=etree_data.xpath('//*[@id="charts"]/div[5]/div[h3="Owner estimations"]/ul/li[contains(@aria-label,"SteamSpy")]/strong/text()')
            print([i,reNan1(Type),reNan1(followers),reNan1(positive_rev),reNan1(negative_rev),reNan2(positive_rev),reNan1(owner1),reNan1(owner2),reNan1(owner3),reNan1(owner4)])
            with open('dv.csv','a',newline='') as f:
                writer = csv.writer(f)  #创建初始化写入对象
                writer.writerow([i,reNan1(Type),reNan1(followers),reNan1(positive_rev),reNan1(negative_rev),reNan2(positive_rev),reNan1(owner1),reNan1(owner2),reNan1(owner3),reNan1(owner4)])
        else:   
            fail_id_lst.append(i)
    time.sleep(1)
    
print ("End: %s" % time.ctime())  