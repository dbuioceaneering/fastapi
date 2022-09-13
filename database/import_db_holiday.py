import sqlite3
import requests
import json

def import_date(year):
    con = sqlite3.connect('calendar1.db')

    url = "https://finfo-api.vndirect.com.vn/v4/trading_calendars?sort=date:asc&q=holiday:true~date:gte:{}-01-02&size=365".format(year)
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
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    arr_data = data["data"]
    for index, item in enumerate(arr_data):
        cur.execute("INSERT INTO DATE (DATEKEY, ISHOLIDAY) VALUES ('{}', 1)".format(item['date']))
        con.commit()
        print("Done record {}".format(item['date']))

    

    url = "https://finfo-api.vndirect.com.vn/v4/trading_calendars?sort=date:asc&q=holiday:false~date:gte:{}-01-01&size=365".format(year)
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

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    arr_data = data["data"]
    for index, item in enumerate(arr_data):
        cur.execute("INSERT INTO DATE (DATEKEY, ISHOLIDAY) VALUES ('{}', 0)".format(item['date']))
        con.commit()
        print("Done record {}".format(item['date']))
        

import_date(year="2013")
