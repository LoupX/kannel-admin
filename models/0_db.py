# -*- coding: utf-8 -*-


try:
    db = DAL('sqlite://storage.db')
except Exception as e:
    raise HTTP(503)
