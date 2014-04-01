# -*- coding: utf-8 -*-


PAGE[0] = 'Clientes'
MENU['customers'] = 'current'


@auth.requires(auth.has_membership(role='ADMIN') or
               auth.has_membership(role='SUPPORT'))
def index():
    SIDEBAR = False
    return dict(SIDEBAR=SIDEBAR)
