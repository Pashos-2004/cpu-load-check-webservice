from fastapi import BackgroundTasks, FastAPI
import uvicorn
import psycopg2
import datetime
app = FastAPI()

connection = psycopg2.connect(dbname='CPU_LOAD', user='postgres', password='1111', host='127.0.0.1');

@app.get("/")
def read_root():
    date=datetime.datetime.now()+datetime.timedelta(hours=-1);

    date = str(date.date()) + " " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
    with connection.cursor() as cursor:
        cursor.execute(f"Begin select * from cpu_load_info where cur_data>='{date}' commit")
        data=cursor.fetchall()
        print(data)
    return data

uvicorn.run(
        app,
        host='localhost',
        port=8080
    )

