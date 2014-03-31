# -*- coding: utf-8 -*-


try:
    db = DAL('postgres://{}:{}@{}:{}/{}'
             ''.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB))
    session.connect(request, response, db, masterapp=None)
except Exception as e:
    raise HTTP(503, e)
