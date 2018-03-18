import celery
from subprocess import Popen
import os

app = celery.Celery('concat')
app.conf.update(BROKER_URL=os.environ['REDIS_URL'], CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


@app.task
def run(vod, start, end, quality=None):
    command = 'concat -vod {} -start "{}" -end "{}"'.format(vod, start, end)
    if quality:
        command = 'concat -vod {} -start "{}" -end "{}" -quality {}'.format(vod, start, end, quality)

    Popen(command, shell=True)
