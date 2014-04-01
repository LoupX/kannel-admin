# -*- coding: utf-8 -*-


PAGE[0] = 'Publicaciones'
MENU['posts'] = 'current'


@auth.requires(auth.has_membership(role='ADMIN') or
               auth.has_membership(role='EDITOR'))
def index():
    SIDEBAR = False
    return dict(SIDEBAR=SIDEBAR)
