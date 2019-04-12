#!/usr/bin/env bash

cd $MASTER_ROOT
python -m scripts.runmaster
#scrapy crawl -a key=RGAPI-f79e026a-3484-4273-85b1-9dcb9daa7da7 lol_master

#if [ "$PRODUCTION" -eq "1" ];
#then
#    gunicorn  --log-level=debug --bind :8000 deans_api.wsgi:application;
#else
#    python3 manage.py runserver 0.0.0.0:8000;
#fi

