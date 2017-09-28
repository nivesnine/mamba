#!/usr/bin/env bash

python init_db.py

python wsgi.py &
LASTPID=$!
sleep 4; kill $LASTPID

coverage run tests.py

