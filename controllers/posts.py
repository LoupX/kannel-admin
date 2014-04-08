# -*- coding: utf-8 -*-
PAGE[0] = 'Publicaciones'
MENU['posts'] = 'current'
sidebar = {'index': '', 'new': ''}


@auth.requires(auth.has_membership(role='ADMIN') or
               auth.has_membership(role='EDITOR'))
def index():
    SIDEBAR = True
    sidebar['index'] = 'current'
    return dict(SIDEBAR=SIDEBAR, sidebar=sidebar)


@auth.requires(auth.has_membership(role='ADMIN') or
               auth.has_membership(role='EDITOR'))
def new():
    SIDEBAR = True
    sidebar['new'] = 'current'
    return dict(SIDEBAR=SIDEBAR, sidebar=sidebar)
