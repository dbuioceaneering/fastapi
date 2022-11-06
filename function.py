from asyncio.constants import ACCEPT_RETRY_DELAY
from datetime import datetime, timedelta
import numpy
from traceback import print_tb
from databases import Database
import pandas
import sqlite3
import requests
import json
import os.path

database = Database("sqlite:///database/calendar.db")
data_path = os.path.join("database")
file_open = os.path.join(data_path, "calendar.db")
con = sqlite3.connect(file_open)
# con = sqlite3.connect('database\calendar.db')


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
        date_obj += timedelta(days=21)
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
        t6_temp = arr_result[6]
        t6 = t6_temp[0]
        t7_temp = arr_result[7]
        t7 = t7_temp[0]
        return [{"t1" : t1,
                "t2" : t2,
                "t3" : t3,
                "t4" : t4,
                "t5" : t5,
                "t6" : t6,
                "t7" : t7
                }]
    return result


def back5days(startDate):
    result = []
    isholiday = check_holiday(startDate)
    if isholiday != 1:
        cur = con.cursor()
        date_obj = pandas.to_datetime(startDate, format='%Y-%m-%d')
        date_obj -= timedelta(days=21)
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
        t6_temp = arr_result[6]
        t6 = t6_temp[0]
        t7_temp = arr_result[7]
        t7 = t7_temp[0]
        return [{"t1" : t1,
                "t2" : t2,
                "t3" : t3,
                "t4" : t4,
                "t5" : t5,
                "t6" : t6,
                "t7" : t7
                }]
    return result


def get_price_hose_SSI():
    url = "https://wgateway-iboard.ssi.com.vn/graphql"
    payload = json.dumps({
    "operationName": "stockRealtimes",
    "variables": {
        "exchange": "hose"
    },
    "query": "query stockRealtimes($exchange: String) {\n  stockRealtimes(exchange: $exchange) {\n    stockNo\n    ceiling\n    floor\n    refPrice\n    stockSymbol\n    stockType\n    exchange\n    matchedPrice\n    matchedVolume\n    priceChange\n    priceChangePercent\n    highest\n    avgPrice\n    lowest\n    nmTotalTradedQty\n    best1Bid\n    best1BidVol\n    best2Bid\n    best2BidVol\n    best3Bid\n    best3BidVol\n    best4Bid\n    best4BidVol\n    best5Bid\n    best5BidVol\n    best6Bid\n    best6BidVol\n    best7Bid\n    best7BidVol\n    best8Bid\n    best8BidVol\n    best9Bid\n    best9BidVol\n    best10Bid\n    best10BidVol\n    best1Offer\n    best1OfferVol\n    best2Offer\n    best2OfferVol\n    best3Offer\n    best3OfferVol\n    best4Offer\n    best4OfferVol\n    best5Offer\n    best5OfferVol\n    best6Offer\n    best6OfferVol\n    best7Offer\n    best7OfferVol\n    best8Offer\n    best8OfferVol\n    best9Offer\n    best9OfferVol\n    best10Offer\n    best10OfferVol\n    buyForeignQtty\n    buyForeignValue\n    sellForeignQtty\n    sellForeignValue\n    caStatus\n    tradingStatus\n    remainForeignQtty\n    currentBidQty\n    currentOfferQty\n    session\n    __typename\n  }\n}\n"
    })
    headers = {
    'authority': 'wgateway-iboard.ssi.com.vn',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'content-type': 'application/json',
    'g-captcha': '',
    'origin': 'https://iboard.ssi.com.vn',
    'referer': 'https://iboard.ssi.com.vn/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_object = json.loads(response.text)
    json_data = json_object['data']['stockRealtimes']
    stringdata = json.dumps(json_data).encode('utf8')
    with open("Price_HOSE.json", "w") as json_file:
        json_file.write(stringdata.decode('utf8'))
    data = pandas.read_json('Price_HOSE.json')
    data.to_excel("Price_HOSE.xlsx")


def get_price_hnx_SSI():
    url = "https://wgateway-iboard.ssi.com.vn/graphql"

    payload = json.dumps({
    "operationName": "stockRealtimes",
    "variables": {
        "exchange": "hnx"
    },
    "query": "query stockRealtimes($exchange: String) {\n  stockRealtimes(exchange: $exchange) {\n    stockNo\n    ceiling\n    floor\n    refPrice\n    stockSymbol\n    stockType\n    exchange\n    matchedPrice\n    matchedVolume\n    priceChange\n    priceChangePercent\n    highest\n    avgPrice\n    lowest\n    nmTotalTradedQty\n    best1Bid\n    best1BidVol\n    best2Bid\n    best2BidVol\n    best3Bid\n    best3BidVol\n    best4Bid\n    best4BidVol\n    best5Bid\n    best5BidVol\n    best6Bid\n    best6BidVol\n    best7Bid\n    best7BidVol\n    best8Bid\n    best8BidVol\n    best9Bid\n    best9BidVol\n    best10Bid\n    best10BidVol\n    best1Offer\n    best1OfferVol\n    best2Offer\n    best2OfferVol\n    best3Offer\n    best3OfferVol\n    best4Offer\n    best4OfferVol\n    best5Offer\n    best5OfferVol\n    best6Offer\n    best6OfferVol\n    best7Offer\n    best7OfferVol\n    best8Offer\n    best8OfferVol\n    best9Offer\n    best9OfferVol\n    best10Offer\n    best10OfferVol\n    buyForeignQtty\n    buyForeignValue\n    sellForeignQtty\n    sellForeignValue\n    caStatus\n    tradingStatus\n    remainForeignQtty\n    currentBidQty\n    currentOfferQty\n    session\n    __typename\n  }\n}\n"
    })
    headers = {
    'authority': 'wgateway-iboard.ssi.com.vn',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'content-type': 'application/json',
    'g-captcha': '',
    'origin': 'https://iboard.ssi.com.vn',
    'referer': 'https://iboard.ssi.com.vn/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response = requests.request("POST", url, headers=headers, data=payload)
    json_object = json.loads(response.text)
    json_data = json_object['data']['stockRealtimes']
    stringdata = json.dumps(json_data).encode('utf8')
    with open("Price_HNX.json", "w") as json_file:
        json_file.write(stringdata.decode('utf8'))
    data = pandas.read_json('Price_HNX.json')
    data.to_excel("Price_HNX.xlsx")



def rm_report_weekly(startDate):

    # Lay 5 ngay lien truoc

    url = "http://127.0.0.1:8080/back5days"

    payload = json.dumps({
    "startDate": startDate
    })
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_obj = json.loads(response.text)
    
    # if len(json_obj) != 0:
    t1 = json_obj[0]['t1']
    t2 = json_obj[0]['t2']
    t3 = json_obj[0]['t3']
    t4 = json_obj[0]['t4']
    t5 = json_obj[0]['t5']
    t6 = json_obj[0]['t6']

    class StockListHSX:
        def __init__(self, stockSymbol, name, exchange):
            self.stockSymbol = stockSymbol
            self.name = name
            self.exchange = exchange
        pass
    
    class StockListHNX:
        def __init__(self, stockSymbol, name, exchange):
            self.stockSymbol = stockSymbol
            self.name = name
            self.exchange = exchange
        pass

    # Tao mang stock
    url = "https://api.fireant.vn/instruments"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json_obj = json.loads(response.text)
    arrHNX = list()
    arrHSX = list()
    for index, item in enumerate(json_obj):
        if item['exchange'] == 'HNX':
            arrHNX.append(StockListHNX(stockSymbol=item['symbol'],name=item['name'],exchange=item['exchange']))
        elif item['exchange'] == 'HSX':
            arrHSX.append(StockListHSX(stockSymbol=item['symbol'],name=item['name'],exchange=item['exchange']))
    arrStock = arrHNX + arrHSX


    rm_report = []
    for index, item in enumerate(arrStock):
        # print("Endpoint /rm_report, processing symbol {} - {}".format(arrStock[index].stockSymbol, datetime.now()))

        url_price = "https://restv2.fireant.vn/symbols/{}/historical-quotes?startDate={}&endDate={}&offset=0&limit=30".format(arrStock[index].stockSymbol,t6,t1)

        payload_price={}
        headers_price = {
        'authority': 'restv2.fireant.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoxODg5NjIyNTMwLCJuYmYiOjE1ODk2MjI1MzAsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsiYWNhZGVteS1yZWFkIiwiYWNhZGVteS13cml0ZSIsImFjY291bnRzLXJlYWQiLCJhY2NvdW50cy13cml0ZSIsImJsb2ctcmVhZCIsImNvbXBhbmllcy1yZWFkIiwiZmluYW5jZS1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImludmVzdG9wZWRpYS1yZWFkIiwib3JkZXJzLXJlYWQiLCJvcmRlcnMtd3JpdGUiLCJwb3N0cy1yZWFkIiwicG9zdHMtd3JpdGUiLCJzZWFyY2giLCJzeW1ib2xzLXJlYWQiLCJ1c2VyLWRhdGEtcmVhZCIsInVzZXItZGF0YS13cml0ZSIsInVzZXJzLXJlYWQiXSwianRpIjoiMjYxYTZhYWQ2MTQ5Njk1ZmJiYzcwODM5MjM0Njc1NWQifQ.dA5-HVzWv-BRfEiAd24uNBiBxASO-PAyWeWESovZm_hj4aXMAZA1-bWNZeXt88dqogo18AwpDQ-h6gefLPdZSFrG5umC1dVWaeYvUnGm62g4XS29fj6p01dhKNNqrsu5KrhnhdnKYVv9VdmbmqDfWR8wDgglk5cJFqalzq6dJWJInFQEPmUs9BW_Zs8tQDn-i5r4tYq2U8vCdqptXoM7YgPllXaPVDeccC9QNu2Xlp9WUvoROzoQXg25lFub1IYkTrM66gJ6t9fJRZToewCt495WNEOQFa_rwLCZ1QwzvL0iYkONHS_jZ0BOhBCdW9dWSawD6iF1SIQaFROvMDH1rg',
        'origin': 'https://fireant.vn',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

        response_price = requests.request("GET", url_price, headers=headers_price, data=payload_price)
        json_obj_price = json.loads(response_price.text)


        if len(json_obj_price) == 6:
            volume_t1 = json_obj_price[0]['totalVolume']
            volume_t2 = json_obj_price[1]['totalVolume']
            volume_t3 = json_obj_price[2]['totalVolume']
            volume_t4 = json_obj_price[3]['totalVolume']
            volume_t5 = json_obj_price[4]['totalVolume']
            volume_t6 = json_obj_price[5]['totalVolume']
            closeprice_t6 = json_obj_price[5]['priceClose']
        elif len(json_obj_price) == 5:
            volume_t1 = json_obj_price[0]['totalVolume']
            volume_t2 = json_obj_price[1]['totalVolume']
            volume_t3 = json_obj_price[2]['totalVolume']
            volume_t4 = json_obj_price[3]['totalVolume']
            volume_t5 = json_obj_price[4]['totalVolume']
            volume_t6 = 0
            closeprice_t6 = 0
        elif len(json_obj_price) == 4:
            volume_t1 = json_obj_price[0]['totalVolume']
            volume_t2 = json_obj_price[1]['totalVolume']
            volume_t3 = json_obj_price[2]['totalVolume']
            volume_t4 = json_obj_price[3]['totalVolume']
            volume_t5 = 0
            volume_t6 = 0
            closeprice_t6 = 0
        elif len(json_obj_price) == 3:
            volume_t1 = json_obj_price[0]['totalVolume']
            volume_t2 = json_obj_price[1]['totalVolume']
            volume_t3 = json_obj_price[2]['totalVolume']
            volume_t4 = 0
            volume_t5 = 0
            volume_t6 = 0
            closeprice_t6 = 0
        elif len(json_obj_price) == 2:
            volume_t1 = json_obj_price[0]['totalVolume']
            volume_t2 = json_obj_price[1]['totalVolume']
            volume_t3 = 0
            volume_t4 = 0
            volume_t5 = 0
            volume_t6 = 0
            closeprice_t6 = 0
        elif len(json_obj_price) == 1:
            volume_t1 = json_obj_price[0]['totalVolume']
            volume_t2 = 0
            volume_t3 = 0
            volume_t4 = 0
            volume_t5 = 0
            volume_t6 = 0
            closeprice_t6 = 0
        elif len(json_obj_price) == 0:
            break
        
        

        url_profile = "https://restv2.fireant.vn/symbols/{}/profile".format(arrStock[index].stockSymbol)
        payload_profile={}
        headers_profile = {
        'authority': 'restv2.fireant.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoxODg5NjIyNTMwLCJuYmYiOjE1ODk2MjI1MzAsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsiYWNhZGVteS1yZWFkIiwiYWNhZGVteS13cml0ZSIsImFjY291bnRzLXJlYWQiLCJhY2NvdW50cy13cml0ZSIsImJsb2ctcmVhZCIsImNvbXBhbmllcy1yZWFkIiwiZmluYW5jZS1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImludmVzdG9wZWRpYS1yZWFkIiwib3JkZXJzLXJlYWQiLCJvcmRlcnMtd3JpdGUiLCJwb3N0cy1yZWFkIiwicG9zdHMtd3JpdGUiLCJzZWFyY2giLCJzeW1ib2xzLXJlYWQiLCJ1c2VyLWRhdGEtcmVhZCIsInVzZXItZGF0YS13cml0ZSIsInVzZXJzLXJlYWQiXSwianRpIjoiMjYxYTZhYWQ2MTQ5Njk1ZmJiYzcwODM5MjM0Njc1NWQifQ.dA5-HVzWv-BRfEiAd24uNBiBxASO-PAyWeWESovZm_hj4aXMAZA1-bWNZeXt88dqogo18AwpDQ-h6gefLPdZSFrG5umC1dVWaeYvUnGm62g4XS29fj6p01dhKNNqrsu5KrhnhdnKYVv9VdmbmqDfWR8wDgglk5cJFqalzq6dJWJInFQEPmUs9BW_Zs8tQDn-i5r4tYq2U8vCdqptXoM7YgPllXaPVDeccC9QNu2Xlp9WUvoROzoQXg25lFub1IYkTrM66gJ6t9fJRZToewCt495WNEOQFa_rwLCZ1QwzvL0iYkONHS_jZ0BOhBCdW9dWSawD6iF1SIQaFROvMDH1rg',
        'origin': 'https://fireant.vn',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

        rm_dict = {
        'stockSymbol':'',
        'name':'',
        'exchange':'',
        'shareoutstanding':'',
        'marketcap_{}'.format(t6):'',
        'volume_{}'.format(t6):'',
        'volume_{}'.format(t5):'',
        'volume_{}'.format(t4):'',
        'volume_{}'.format(t3):'',
        'volume_{}'.format(t2):'',
        'volume_{}'.format(t1):''
        }

        response_profile = requests.request("GET", url_profile, headers=headers_profile, data=payload_profile)
        json_obj_profile = json.loads(response_profile.text)
        shareoutstanding = json_obj_profile['listingVolume']
        # rm_report.append(reportrm(stockSymbol=arrStock[index].stockSymbol,exchange=arrStock[index].exchange,name=arrStock[index].name,shareoutstanding=shareoutstanding,marketcap=closeprice_t1*shareoutstanding ,volume_t1=volume_t1,volume_t2=volume_t2,volume_t3=volume_t3,volume_t4=volume_t4,volume_t5=volume_t5))
        rm_dict['stockSymbol'] = arrStock[index].stockSymbol
        rm_dict['exchange'] = arrStock[index].exchange
        rm_dict['name'] = arrStock[index].name
        rm_dict['shareoutstanding'] = shareoutstanding
        rm_dict['marketcap_{}'.format(t6)] = closeprice_t6 * shareoutstanding
        rm_dict['volume_{}'.format(t6)] = volume_t6
        rm_dict['volume_{}'.format(t5)] = volume_t5
        rm_dict['volume_{}'.format(t4)] = volume_t4
        rm_dict['volume_{}'.format(t3)] = volume_t3
        rm_dict['volume_{}'.format(t2)] = volume_t2
        rm_dict['volume_{}'.format(t1)] = volume_t1
        rm_report.append(rm_dict)
        # print(rm_report)
    

    stringdata = json.dumps(rm_report).encode('utf8')
    with open("RM_Report.json", "w") as json_file:
        json_file.write(stringdata.decode('utf8'))
    data = pandas.read_json('RM_Report.json')
    data.to_excel("RM_Report.xlsx")

# back5days("2022-10-20")
# rm_report_weekly("2022-11-07")