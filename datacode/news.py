import csv
import json
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
url='https://auto.daum.net/prx/mc2/v2/contents/5030300.json?pageSize=20&page=1&range=30&maxDate=20211130&contentsType=news,harmony'
data={'type':'harmony'}
res=requests.get(url,data)
results=res.json()['data']

def get_news():
    pages=np.arange(1,20,1)
    test = []
    for page in pages:
        url='https://auto.daum.net/prx/mc2/v2/contents/5030300.json?pageSize=20&page='+str(page)+'&range=30&maxDate=20211130&contentsType=news,harmony'
        data={'type':'harmony'}
        res=requests.get(url,data)
        results=res.json()['data']
        for product in results:
            test.append({'title':product['title'],
                                  'script':product['description'],
                                    'link':product['cpInfo']['outlink'],
                                    'media':product['cpInfo']['korName'],
                                'image':product['image'][0]})
    return test
# print(get_news())
def news_save():
    car_db = pymysql.connect(
        user='root',
        passwd='1234',
        host='0.0.0.0',
        db='data',
        charset='utf8'
    )
    cursor = car_db.cursor(pymysql.cursors.DictCursor)
    info = get_news()
    insert_sql2 = f"INSERT INTO news VALUES (%(title)s,%(script)s,%(link)s,%(media)s,%(image)s);"
    cursor.executemany(insert_sql2, info)
    car_db.commit()
    print('News Success')
    
news_save()
