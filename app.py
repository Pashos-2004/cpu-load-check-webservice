from fastapi import BackgroundTasks, FastAPI
import uvicorn
import psycopg2
import datetime
import  matplotlib.pyplot as plt
import  matplotlib.dates as plt_d
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


def save_graphs_as_png():

    cur_date = datetime.datetime.now()

    date = cur_date + datetime.timedelta(hours=-1);
    _date = date + datetime.timedelta(seconds=-1);
    interval = 5/(24*60*60)

    date = str(date.date()) + " " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
    cur_date = str(cur_date.date()) + " " + str(cur_date.hour) + ":" + str(cur_date.minute) + ":" + str(cur_date.second)
    with connection.cursor() as cursor:
        cursor.execute(f"select * from cpu_load_info where cur_data>='{date}'")
        data = cursor.fetchall()
    x=[]
    y=[]
    x2=[]
    y2=[]
    summ=0;
    count = 1;
    prev_date=_date
    x.append(_date)
    y.append(0)

    x2.append(_date+datetime.timedelta(minutes=-1))
    y2.append(0)
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])
        if(prev_date.minute==data[i][0].minute):
            summ+=data[i][1]
            count+=1;
        else:
            x2.append(prev_date)
            y2.append(summ/count)
            prev_date=data[i][0]
            summ=data[i][1]
            count=1

    x.append(datetime.datetime.now()+datetime.timedelta(seconds=+1))
    y.append(0)
    x2.append(datetime.datetime.now() + datetime.timedelta(minutes=+1))
    y2.append(0)
    #plt.plot(x,y)
    plt.bar(x,y,interval)

    plt.savefig("First_graph.png")
    plt.close('all')

    interval = 1 / (24 * 60)
    plt.bar(x2,y2,interval)
    plt.savefig("Second_graph.png")

@app.get("/show_graphs")
def show_graphs():
    save_graphs_as_png()
    return ("print")
    pass

uvicorn.run(
        app,
        host='localhost',
        port=8080
    )

