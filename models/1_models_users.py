# -*- coding: utf-8 -*-
from gluon.tools import Auth

auth = Auth(db)
auth.settings.extra_fields['auth_user'] = [
    Field('theme', 'string', length=9, default='default')]
auth.define_tables(username=True, migrate=MIGRATE)
auth.settings.controller = 'login'
auth.settings.function = 'index'
auth.settings.login_url = URL('login', 'index')
auth.settings.login_next = URL('default', 'index')
auth.settings.logout_next = URL('login', 'index')
auth.settings.login_after_registration = False
auth.settings.expiration = 18000

try:
    if db(db.auth_group).isempty():
        god_group_id = auth.add_group('GOD', 'Sys Admin')
        auth.add_group('ADMINISTRATOR', 'Administrador')
        auth.add_group('EDITOR', 'Editor de contenido'),
        auth.add_group('SUPPORT', 'Operador de soporte')
    else:
        god_group_id = db(db.auth_group.role=='GOD').select().first()
        god_group_id = god_group_id.id

    if db(db.auth_user).isempty():
        password = db.auth_user.password.validate(GOD_PASSWORD)[0]
        data = dict()
        data['first_name'] = 'Juan D.'
        data['last_name'] = 'Romero'
        data['username'] = GOD_USER
        data['password'] = password
        data['email'] = 'jd@beardcode.mx'
        god_user_id = db.auth_user.insert(**data)
        auth.add_membership(god_group_id, god_user_id)
except Exception as e:
    db.rollback()
    raise HTTP(503, 'There\'s a problem with the database connection {}'.format(e))
else:
    db.commit()
