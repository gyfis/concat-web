[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# Concat web service
Simple Flask web wrapper around the `concat` library (https://github.com/ArneVogel/concat) for easy heroku deployment. Uses two free dynos to work.

## Features
Using Flask as a web server and Celery for the asynchronous job performs. The idea is to asynchronously invoke the commandline `concat` tool and return current state when getting the status in the web page request. Note that this tool doesn't guarantee that the files will be present in any time after the donwload is ready, as Heroku doesn't guarantee it not removing the files. For this reason, it is advised to download the file as soon as you see the download link ready, to prevent unnecessary re-downloading.

## Endpoints
### `/<vod>/qualityinfo/`
Used for calling the -qualityinfo on the vod, currently returns ugly list of quality options

### `/<vod_id>`
Main endpoint, use for downloading and querying about download

Required query parameters
- `start`, `end` - in the `00-00-00` format (`hh-mm-ss`), e.g. `start=5-3-20&end=6-2-0`

Optional query parameters
- `quality` - use for specifying quality, e.g. ``&quality=360p30`
- `delete` - use for deleting existing .mp4 file, e.g. `&delete=true` - *WARNING you want to call the endpoint with this param only once to not remove the new downloaded file*

Example call (not guaranteed this app will be up and vod to exist)

First call (to invoke the downloading)

- https://fathomless-castle-57163.herokuapp.com/239817129?start=0-0-0&end=0-3-0&quality=360p30&delete=true

Subsequent calls (to check status)

- https://fathomless-castle-57163.herokuapp.com/239817129?start=0-0-0&end=0-3-0&quality=360p30

When the download is started, the web will list number of downloaded chunks.
After the download is ready, the web will list a download button, which can be either downloaded or viewed in browser.

### `/download/<vod_id>`
Endpoint for downloading or viewing in browser, doesn't have to be used directly (`/<void_id>` endpoint returns a link after download)

## Thanks
Many thanks to ArneVogel for the standalone `concat` commandline app.

## Licensing
Steps describing the build process for `concat` can be found in `concat-vendor-build.sh`, LICENSE file is included. The `ffmpeg` binary is taken from `http://flect.github.io/heroku-binaries/libs/ffmpeg.tar.gz`. This project uses GPL 3.0 because `concat` uses one.
