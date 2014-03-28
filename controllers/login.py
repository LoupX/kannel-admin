# -*-coding: utf-8 -*-


PAGE[0] = 'Login'


def index():
    if auth.is_logged_in():
        redirect(URL('init', 'default', 'index'))
    return dict()
