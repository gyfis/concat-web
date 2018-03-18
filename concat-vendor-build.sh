#!/bin/bash
# Run this file on Heroku
# e.g. `heroku run /bin/bash` and paste or ./concat-vendor-build.sh

# Go
curl -O https://dl.google.com/go/go1.10.linux-amd64.tar.gz
tar -C . -xzf go1.10.linux-amd64.tar.gz
export GOROOT=$HOME/go
export PATH=$PATH:$GOROOT/bin

# Concat
git clone https://github.com/ArneVogel/concat
cd concat
export GOPATH=$HOME/concat

# Build concat
go get github.com/abiosoft/semaphore
go build

# Upload concat to transfer.sh
curl --upload-file ./concat https://transfer.sh/concat
