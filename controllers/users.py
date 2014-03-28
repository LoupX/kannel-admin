# -*- coding: utf-8 -*-
from gluon.tools import Service


PAGE[0] = 'Usuarios'
MENU['users'] = 'current'
service = Service()


def api():
    return service()


@service.json
def login():
    #Validate fields and tries to do a login.
    usr = request.vars.username
    pwd = request.vars.password
    data = dict()
    error = dict()
    result = JSON

    try:
        auth.login_bare(usr, pwd)
        if auth.is_logged_in():
            data['success'] = True
            result['data'] = data
            return result
        else:
            error['code'] = 401
            error['message'] = 'Invalid credentials'
            result['error'] = error
            return result
    except Exception as e:
        error['code'] = 500
        error['message'] = 'Can\'t process request'
        result['error'] = error
        return result


@service.json
def logout():
    result = JSON
    auth.logout()
    if not auth.is_logged_in():
        data['success'] = True
        result['data'] = data
    else:
        error['code'] = 500
        error['message'] = 'No se pudo cerrar la sesión'
        result['error'] = error
        return result


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='ADMINISTRATOR'))
def index():
    SIDEBAR = False
    return dict(SIDEBAR=SIDEBAR)
