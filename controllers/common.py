# -*- coding: utf-8 -*-
from gluon.tools import Service


service = Service()


def api():
    return service()


@service.json
def change_theme():
    user_id = auth.user.id
    theme = request.vars['theme']

    result = JSON
    error = {}
    data = {}

    if theme not in THEMES:
        error['code'] = 401
        error['message'] = 'Invalid value {}'.format(theme)
        result['error'] = error
        return result

    try:
        table = db.auth_user
        user = db(table.id==user_id).select().first()
        user.update_record(theme=theme)
        auth.user.update(theme=theme)
        data['success'] = True
        result['data'] = data
    except:
        db.rollback()
        error['code'] = 500
        error['message'] = 'Unexpected error while processing your request'
        result['error'] = error

    return result
