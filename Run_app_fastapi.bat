cd C:\Python\FastAPI\logs
del logfile.log
cd C:\Python\FastAPI\
C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts\uvicorn.exe app_api:app --host 0.0.0.0 --port 8080 --workers 4 --log-config config_log.ini --use-colors