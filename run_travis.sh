#!/usr/bin/env bash

python init_db.py
python wsgi.py &
LASTPID=$!
sleep 10; kill $LASTPID
