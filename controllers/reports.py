# -*- coding: utf-8 -*-


PAGE[0] = 'Reportes'
MENU['reports'] = 'current'


@auth.requires_membership('ADMIN')
def index():
    SIDEBAR = False
    return dict(SIDEBAR=SIDEBAR)
