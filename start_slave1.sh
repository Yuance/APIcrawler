#!/usr/bin/env bash

cd $MASTER_ROOT
#scrapy crawl -s TELNETCONSOLE=6024 -a key=RGAPI-f79e026a-3484-4273-85b1-9dcb9daa7da7 lol_slave
python -m scripts.runslave