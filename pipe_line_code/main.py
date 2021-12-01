import requests
from bs4 import BeautifulSoup
import json
import csv
import pandas as pd
import pymysql
from encar import to_db,add_info,to_df
from encar_for import add_info_for,to_df_for
from kcar import get_all_k,to_df_k
from news import news_save
from make_db import *
from function import save_db
from create import make_db
#데이터를 저장할 db 생성(raw_data,news table)
make_db()

#encar사이트에서 국산 중고차 데이터 불러오기
info_e,e_info = to_df('etc')
info_b,b_info = to_df('black')
info_w,w_info = to_df('white')
info_g,g_info = to_df('gray')

#encar사이트에서 수입 중고차 데이터 불러오기
encar_for_e,e_encar_for = to_df_for('etc')
encar_for_b,b_encar_for = to_df_for('black')
encar_for_w,w_encar_for = to_df_for('white')
encar_for_g,g_encar_for = to_df_for('gray')

#kcar사이트에서 중고차 데이터 불러오기
kcar_info = get_all_k()
kcar = to_df_k()

#모든 데이터 list에 담기
list = [e_info,b_info,w_info,g_info,e_encar_for,b_encar_for,w_encar_for,g_encar_for,kcar_info]

#모든 데이터 합쳐서 cvs로 저장
all_csv = pd.concat([info_e,info_b,info_w,info_g,encar_for_e,encar_for_b,encar_for_w,encar_for_g,kcar])
all_csv.to_csv("all_csv.csv",index=False,sep=',')

#raw 데이터를 db에 저장
save_db(list)

#news 크롤링 데이터를 db에 저장
news_save()

#전처리된 데이터를 db에 저장
savedb()