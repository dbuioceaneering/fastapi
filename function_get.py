from asyncio.constants import ACCEPT_RETRY_DELAY
from datetime import datetime, timedelta
import datetime
import numpy
from traceback import print_tb
# from databases import Database
import pandas
# import sqlite3
import requests
import json
import calendar

################### Number of days in month #####################

def days_in_month():
    now = datetime.datetime.now()
    num_of_days = calendar.monthrange(now.year, now.month)[1]
    array_day_in_month = []
    i = 0
    while (i < num_of_days):
        temp_array = []
        i += 1
        given_date = datetime.date.today()
        first_day_of_month = given_date.replace(day=i)
        temp_array.append(first_day_of_month)
        array_day_in_month = array_day_in_month + temp_array
        
    return array_day_in_month

################## Get event in month ##########################

def get_event_in_month():
    array_days = days_in_month()
    given_date = datetime.date.today()
    first_day_of_month = given_date.replace(day=1)
    date_obj = first_day_of_month
    first_date = date_obj.strftime('%Y-%m-%d')
    url = "https://finfo-api.vndirect.com.vn/v4/events?sort=code:asc~type:asc&q=locale:VN~group:investorRight,stockAlert~effectiveDate:{}&size=200".format(first_date)
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
    response1 = requests.request("GET", url, headers=headers, data=payload)
    json_obj1 = json.loads(response1.text)
    json1 = json_obj1['data']

    for index, item in enumerate(array_days):
        date_obj = item
        string_date = date_obj.strftime('%Y-%m-%d')
        url = "https://finfo-api.vndirect.com.vn/v4/events?sort=code:asc~type:asc&q=locale:VN~group:investorRight,stockAlert~effectiveDate:{}&size=200".format(string_date)
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
        json_obj = json.loads(response.text)
        json_data = json_obj['data']
        json1 = json1 + json_data
        
    stringdata = json.dumps(json1).encode('utf8')
    with open("events_in_month.json", "w") as json_file:
        json_file.write(stringdata.decode('utf8'))
    data = pandas.read_json('events_in_month.json')
    data.to_excel("Events_in_month.xlsx")
