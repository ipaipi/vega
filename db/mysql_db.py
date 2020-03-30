# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import mysql.connector.pooling

__confing = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "1224",
    "database": "vega"
}
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__confing,
        pool_size=10
    )
except Exception as e:
    print(e)