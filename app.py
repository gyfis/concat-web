from flask import Flask, request, send_from_directory
from flask_sslify import SSLify
from subprocess import Popen, PIPE

from vod import Vod

app = Flask(__name__)
sslify = SSLify(app)


@app.route('/<vod>/qualityinfo/')
def qualityinfo(vod):
    child = Popen('concat -vod {} -qualityinfo'.format(vod), stdout=PIPE, shell=True)
    result = child.communicate()
    return result[0]


@app.route('/<vod_id>')
def query(vod_id):
    start = request.args.get('start')
    end = request.args.get('end')
    quality = request.args.get('quality')

    if not start:
        return 'Missing start parameter'
    if not end:
        return 'Missing end parameter'

    vod = Vod(vod_id)
    if request.args.get('delete'):
        vod.delete()

    vod.query(start.replace('-', ' '), end.replace('-', ' '), quality)
    if vod.status == 'downloaded':
        return 'Downloaded! <a href={}>Download link</a>'.format('{}download/{}'.format(request.url_root, vod_id))
    else:
        return vod.status


@app.route('/download/<vod_id>')
def download(vod_id):
    vod = Vod(vod_id)
    if vod.status == 'downloaded':
        return send_from_directory(app.root_path, vod.filename)
    else:
        return 'Not downloaded yet'


@app.route('/')
def index():
    return 'A concat web'


def main():
    app.run(debug=True)
    # app.run(debug=False)


if __name__ == '__main__':
    main()
