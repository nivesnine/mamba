#!/usr/bin/env bash

python init_db.py

python wsgi.py &
LASTPID=$!
sleep 4; kill $LASTPID

py.test tests.py --cov=./app
