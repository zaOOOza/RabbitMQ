from PIL import Image

from celery import Celery

app = Celery('celery_worker', broker='pyamqp://guest@localhost//')


@app.task
def task1(name):
    basewidth = 512
    hsize = 512
    img = Image.open(name)
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(name)
    return True
