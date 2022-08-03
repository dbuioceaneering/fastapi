from asyncio.constants import ACCEPT_RETRY_DELAY
from datetime import datetime, timedelta
import numpy
from traceback import print_tb
from databases import Database
import pandas
import sqlite3
import requests
import json



database = Database("sqlite:///database/calendar.db")
con = sqlite3.connect('database\calendar.db')


def check_holiday(startDate):
    cur = con.cursor()
    cur.execute("select isholiday from date where datekey = '{}'".format(startDate))
    result = cur.fetchall()
    for index, item in enumerate(result):
        result = item[0]
    return result

##################### Tinh T+5 #######################
# Request 20 ngay ke tu ngay nhap vao de lay mang trading date, lay 20 ngay de tranh roi vao cac ngay nghi le dai,co the dieu chinh sau do de phu hop hon. Lay ra next20days
# Request de lay mang rang time 20 ngay
# Dem phan tu trong mang. T+1 la phan tu thu tu la 1, tuong tu cho den T+5 la phan tu thu 5. Coi ngay nhap vao la T+0
def next5days(startDate):
    result = []
    isholiday = check_holiday(startDate)
    if isholiday != 1:
        cur = con.cursor()
        date_obj = pandas.to_datetime(startDate, format='%Y-%m-%d')
        date_obj += timedelta(days=14)
        str_next14days = datetime.strftime(date_obj,"%Y-%m-%d")
        cur.execute("select datekey from date where datekey between '{}' and '{}' and isholiday = 0".format(startDate,str_next14days))
        # cur.execute("select strftime('%d/%m/%Y', datekey) as datekey from date where datekey between '{}' and '{}' and isholiday = 0".format(startDate,str_next14days))
        result = cur.fetchall()
        arr_result = numpy.array(result)
        t1_temp = arr_result[1]
        t1 = t1_temp[0]
        t2_temp = arr_result[2]
        t2 = t2_temp[0]
        t3_temp = arr_result[3]
        t3 = t3_temp[0]
        t4_temp = arr_result[4]
        t4 = t4_temp[0]
        t5_temp = arr_result[5]
        t5 = t5_temp[0]
        return [{"t1" : t1,
                "t2" : t2,
                "t3" : t3,
                "t4" : t4,
                "t5" : t5}]
    return result


def back5days(startDate):
    result = []
    isholiday = check_holiday(startDate)
    if isholiday != 1:
        cur = con.cursor()
        date_obj = pandas.to_datetime(startDate, format='%Y-%m-%d')
        date_obj -= timedelta(days=14)
        str_back14days = datetime.strftime(date_obj,"%Y-%m-%d")
        cur.execute("select datekey from date where datekey between '{}' and '{}' and isholiday = 0 order by datekey desc".format(str_back14days,startDate))
        # cur.execute("select strftime('%d/%m/%Y', datekey) as datekey from date where datekey between '{}' and '{}' and isholiday = 0 order by datekey desc".format(str_back14days,startDate))
        result = cur.fetchall()
        arr_result = numpy.array(result)
        t1_temp = arr_result[1]
        t1 = t1_temp[0]
        t2_temp = arr_result[2]
        t2 = t2_temp[0]
        t3_temp = arr_result[3]
        t3 = t3_temp[0]
        t4_temp = arr_result[4]
        t4 = t4_temp[0]
        t5_temp = arr_result[5]
        t5 = t5_temp[0]
        return [{"t1" : t1,
                "t2" : t2,
                "t3" : t3,
                "t4" : t4,
                "t5" : t5}]    
    return result

def import_date(year):
    url1 = "https://finfo-api.vndirect.com.vn/v4/trading_calendars?sort=date:asc&q=holiday:true~date:gte:{}-01-01&size=365".format(year)
    cur = con.cursor()
    payload={}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://dstock.vndirect.com.vn',
        'Pragma': 'no-cache',
        'Referer': 'https://dstock.vndirect.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response1 = requests.request("GET", url1, headers=headers, data=payload)
    data1 = json.loads(response1.text)
    arr_data1 = data1["data"]
    for index, item in enumerate(arr_data1):
        cur.execute("INSERT INTO DATE (DATEKEY, ISHOLIDAY) VALUES ('{}', 1)".format(item['date']))
        con.commit()
        print("Done record {}".format(item['date']))

    

    url2 = "https://finfo-api.vndirect.com.vn/v4/trading_calendars?sort=date:asc&q=holiday:false~date:gte:{}-01-01&size=365".format(year)
    cur = con.cursor()
    payload={}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://dstock.vndirect.com.vn',
        'Pragma': 'no-cache',
        'Referer': 'https://dstock.vndirect.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    response2 = requests.request("GET", url2, headers=headers, data=payload)
    data2 = json.loads(response2.text)
    arr_data2 = data2["data"]
    for index, item in enumerate(arr_data2):
        cur.execute("INSERT INTO DATE (DATEKEY, ISHOLIDAY) VALUES ('{}', 0)".format(item['date']))
        con.commit()
        print("Done record {}".format(item['date']))
