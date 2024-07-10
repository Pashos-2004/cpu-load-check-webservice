import psutil
import datetime
from time import  sleep
import psycopg2

connection = psycopg2.connect(dbname='CPU_LOAD', user='postgres', password='1111', host='127.0.0.1');


while (True):
    cur_load= psutil.cpu_percent(0.1)
    cur_time = datetime.datetime.now();
    #cur_time = (str(cur_time)).replace('.'+str(cur_time.microsecond),"")
    cur_time=str(cur_time.date())+" "+str(cur_time.hour)+":"+str(cur_time.minute)+":"+str(cur_time.second)
    print(cur_load," ",cur_time,)
    #print(datetime.datetime.now()+datetime.timedelta(hours=-1));


    try:
        fetch = f'''begin;
         insert into cpu_load_info(cur_data,cpu_load_in_percent) 
        values ('{cur_time}',{cur_load});
        commit;'''


        with connection.cursor() as cursor:
            cursor.execute(fetch)
            connection.commit()
    except:
        print("Ошибка доступа к БД");

    sleep(4.9)
