#!/usr/bin/env python

'''Configures the environment variables for AirBnb clone based on the current
value of the env varibale AIRBNB_ENV. From the api directory, use the command
`python -m app.models.base`.
'''

import os

status = os.environ.get('AIRBNB_ENV')

DEBUG = True
HOST = "localhost"
PORT = 3333
DATABASE = {"host": "158.69.70.204", "user": "airbnb_user_dev", "database":"airbnb_dev", "port": 3306, "charset": "utf8", "password": "airbnb_user_dev"}

if status == 'production':
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 3000
    DATABASE = {"host": "158.69.70.204", "user": "airbnb_user_prod", "database":"airbnb_prod", "port": 3306, "charset": "utf8", "password": "airbnb_user_prod"}
