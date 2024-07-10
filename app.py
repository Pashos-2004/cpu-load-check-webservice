from fastapi import BackgroundTasks, FastAPI
import uvicorn
import psycopg2
import datetime
app = FastAPI()

connection = psycopg2.connect(dbname='CPU_LOAD', user='postgres', password='1111', host='127.0.0.1');

@app.get("/")
def read_root():
    cur_date=datetime.datetime.now()
    date=cur_date+datetime.timedelta(hours=-1);

    date = str(date.date()) + " " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
    cur_date=str(cur_date.date()) + " " + str(cur_date.hour) + ":" + str(cur_date.minute) + ":" + str(cur_date.second)
    with connection.cursor() as cursor:
        cursor.execute(f"select * from cpu_load_info where cur_data>='{date}'")
        data=cursor.fetchall()

    return data

uvicorn.run(
        app,
        host='localhost',
        port=8080
    )

