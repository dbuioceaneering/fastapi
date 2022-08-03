FROM python:3.9

# 
WORKDIR /code/app/

# 
COPY ./requirements.txt /code/requirements.txt
COPY ./database/calendar.db /code/app/database/calendar.db

#

EXPOSE 8080

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code/app

# 
CMD ["uvicorn", "app_api:app", "--host", "0.0.0.0", "--port", "8080"]