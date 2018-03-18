import os
import tasks


class Vod(object):
    def __init__(self, number):
        self.number = number

    @property
    def status(self):
        tmp_dir = '_{}'.format(self.number)
        if os.path.exists(tmp_dir):
            files = os.listdir(tmp_dir)
            chunks = sorted(list(map(lambda file: int(file.split('_')[1][:-3]), files)))
            return 'downloading ({} chunks downloaded, current first: {}, current last: {})'.format(len(chunks), chunks[0], chunks[-1])
        elif os.path.exists('{}.mp4'.format(self.number)):
            return 'downloaded'
        else:
            return 'not downloaded'

    @property
    def filename(self):
        return '{}.mp4'.format(self.number)

    def query(self, start_at, end_at, quality=None):
        if self.status == 'not downloaded':
            tasks.run(self.number, start_at, end_at, quality)

    def delete(self):
        if self.status == 'downloaded':
            os.remove(self.filename)
