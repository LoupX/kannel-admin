# -*- coding: utf-8 -*-
from gluon.tools import Service


PAGE[0] = 'Usuarios'
MENU['users'] = 'current'
service = Service()


def api():
    return service()


# Section: Web Services {{{1
#------------------------------------------------------------------------------
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


@service.json
@auth.requires_membership('ADMIN')
def create():
    result = JSON
    error = dict()
    data = dict()
    v = request.vars
    user = {}
    user['first_name'] = v.first_name
    user['last_name'] = v.last_name
    user['username'] = v.username
    user['email'] = v.email
    group_id = v.group

    for value in user.values():
        if str(value).strip() == '':
            error['code'] = 400
            error['message'] = 'todos los campos son obligatorios'
            result['error'] = error
            return result

    if not group_id:
        error['code'] = 400
        error['message'] = 'Todos los campos son obligatorios'
        result['error'] = error
        return result

    try:
        table = db.auth_user
        query = table.username == user['username'].strip()
        if db(query).count():
            error['code'] = 400
            error['message'] = 'el nombre de usuario ya está en uso'
            result['error'] = error
            return result
    except Exception as e:
        error['code'] = 500
        error['message'] = 'no se pudo procesar su petición'
        result['error'] = error
        return result

    try:
        password = db.auth_user.password.validate(user['username'])[0]
        user['password'] = password
        user['id'] = db.auth_user.insert(**user)
        auth.add_membership(group_id, user['id'])
        db.commit()
        data['success'] = True
        result['data'] = data
    except Exception as e:
        db.rollback()
        error['code'] = 500
        error['message'] = 'no se pudo actualizar el registro {}'.format(e)
        result['error'] = error
    return result


@service.json
@auth.requires_membership('ADMIN')
def read():
    result = JSON
    user_id = request.vars.user
    table = db.auth_user
    fields = [field for field in table.fields]
    fields.remove('password')
    fields = [table[field] for field in fields]
    user = db(table.id==user_id).select(*fields).first()
    table = db.auth_membership
    group = db(table.user_id==user_id).select(table.group_id).first()
    user['group_id'] = group.group_id
    result['data'] = user
    return result


@service.json
@auth.requires_membership('ADMIN')
def update():
    result = JSON
    error = dict()
    data = dict()
    v = request.vars
    user = {}
    user['id'] = v.id
    user['first_name'] = v.first_name
    user['last_name'] = v.last_name
    user['username'] = v.username
    user['email'] = v.email
    group_id = v.group

    for value in user.values():
        if str(value).strip() == '':
            error['code'] = 400
            error['message'] = 'Todos los campos son obligatorios'
            result['error'] = error
            return result

    if not group_id:
        error['code'] = 400
        error['message'] = 'Todos los campos son obligatorios'
        result['error'] = error
        return result

    try:
        table = db.auth_user
        query = table.id != user['id']
        query &= table.username == user['username'].strip()
        if db(query).count():
            error['code'] = 400
            error['message'] = 'El nombre de usuario ya está en uso'
            result['error'] = error
            return result
    except Exception as e:
        error['code'] = 500
        error['message'] = 'No se pudo procesar su petición'
        result['error'] = error
        return result

    try:
        table = db.auth_user
        db(table.id==user['id']).update(**user)
        table = db.auth_membership
        db(table.user_id==user['id']).update(group_id=group_id)
        db.commit()
        if user['id'] == auth.user.id:
            auth.user.update(**user)
        data['success'] = True
        result['data'] = data
    except Exception as e:
        db.rollback()
        error['code'] = 500
        error['message'] = 'No se pudo actualizar el registro {}'.format(e)
        result['error'] = error
    return result


@service.json
@auth.requires_membership('ADMIN')
def delete():
    pass


# Section: Views {{{1
#------------------------------------------------------------------------------
@auth.requires_membership('ADMIN')
def index():
    SIDEBAR = False
    table = db.auth_user
    users = db(table).select(table.username, table.id)
    table = db.auth_group
    groups = db(table).select()
    return dict(SIDEBAR=SIDEBAR, users=users, groups=groups)
