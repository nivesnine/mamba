#!/usr/bin/env bash

python init_db.py
python wsgi.py > /dev/null

