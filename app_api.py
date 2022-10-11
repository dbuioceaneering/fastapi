from ast import Starred
from tracemalloc import start
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from pydantic import BaseModel
from datetime import datetime
from fastapi.responses import FileResponse
from function import next5days, back5days, import_date
from function_get import get_event_in_month

database = Database("sqlite:///database/calendar.db")

class startDate(BaseModel):
    startDate: str

class year(BaseModel):
    year: str

app = FastAPI()
@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.post("/next5days")
async def fetch_data(startDate: startDate):
    # query = "select * from date where datekey between '2019-01-01' and '2019-02-01' and isholiday = 0"
    # results = await database.fetch_all(query=query)
    results = next5days(startDate.startDate)
    return  results

@app.post("/back5days")
async def fetch_data(startDate: startDate):
    # query = "select * from date where datekey between '2019-01-01' and '2019-02-01' and isholiday = 0"
    # results = await database.fetch_all(query=query)
    results = back5days(startDate.startDate)
    return  results

# @app.post("/importdates")
# async def fetch_data(year: year):
#     # query = "select * from date where datekey between '2019-01-01' and '2019-02-01' and isholiday = 0"
#     # results = await database.fetch_all(query=query)
#     results = import_date(year.year)
#     return  results

@app.get("/events_in_month")
async def fetch_data():
    # query = "select * from date where datekey between '2019-01-01' and '2019-02-01' and isholiday = 0"
    # results = await database.fetch_all(query=query)
    get_event_in_month()
    file_path = "Events_in_2_months.xlsx"
    return FileResponse(path=file_path, filename=file_path)

# @app.get("/test") #> Get method with param
# async def fetch_data(startDate: str):
#     # query = "select * from date where datekey between '2019-01-01' and '2019-02-01' and isholiday = 0"
#     # results = await database.fetch_all(query=query)
#     results = back5days(startDate)
#     return  results

# @app.post("/tradingdate/")
# async def fetch_data(startdate: str):
#     query = "select * from date where datekey between '{}' and '2020-01-01' and isholiday = 0".format(str(startdate))
#     results = await database.fetch_all(query=query)
#     return  results

##################### Tinh T+5#######################
# Request 20 ngay ke tu ngay nhap vao de lay mang trading date, lay 20 ngay de tranh roi vao cac ngay nghi le dai,co the dieu chinh sau do de phu hop hon. Lay ra next20days
# Request de lay mang rang time 20 ngay
# Dem phan tu trong mang. T+1 la phan tu thu tu la 1, tuong tu cho den T+5 la phan tu thu 5. Coi ngay nhap vao la T+0

# @app.post("/next5days/")
# async def fetch_data(startdate: str):
#     query = "select * from date where datekey between '{}' and '2020-01-01' and isholiday = 0".format(str(startdate))
#     results = await database.fetch_all(query=query)
#     return  results