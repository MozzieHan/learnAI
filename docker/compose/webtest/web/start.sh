#!/bin/bash
pip install -r /opt/webapp/chainfrontier/requirements.txt -i https://pypi.douban.com/simple && 
python /opt/webapp/chainfrontier/manage.py migrate && 
python /opt/webapp/chainfrontier/manage.py collectstatic --noinput &&
python /opt/webapp/chainfrontier/manage.py runserver 0.0.0.0:8000
