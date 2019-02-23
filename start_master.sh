#!/usr/bin/env bash

cd $MASTER_ROOT
python -m scripts.runmaster
#if [ "$PRODUCTION" -eq "1" ];
#then
#    gunicorn  --log-level=debug --bind :8000 deans_api.wsgi:application;
#else
#    python3 manage.py runserver 0.0.0.0:8000;
#fi

