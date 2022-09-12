import uuid

from PIL import Image

import datetime
import time

from celery import Celery

app = Celery('celery_worker', broker='pyamqp://guest@localhost//')


@app.task
def task1(name):
    start_time = datetime.datetime.now()
    time.sleep(10)
    end_time = datetime.datetime.now()

    img = Image.open(name)
    basewidth = 512
    hsize = 512
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'C:/Users/zaooo/OneDrive/Рабочий стол/test/new{name}')

    file_obj = open('tasks.txt', 'a')
    file_obj.write(f'uuid: {uuid.uuid4()} start time: {start_time}, end time: {end_time}\r\n')
    file_obj.close()
    return True
