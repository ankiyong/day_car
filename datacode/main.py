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

info_e = to_df('etc')
info_b = to_df('black')
info_w = to_df('white')
info_g = to_df('gray')


encar_for_e = to_df_for('etc')
encar_for_b = to_df_for('black')
encar_for_w = to_df_for('white')
encar_for_g = to_df_for('gray')


kcar = to_df_k()

all_csv = pd.concat([info_e,info_b,info_w,info_g,encar_for_e,encar_for_b,encar_for_w,encar_for_g,kcar])
all_csv.to_csv("all_csv.csv",index=False,sep=',')

news_save()
