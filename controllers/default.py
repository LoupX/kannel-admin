# -*- coding: utf-8 -*-


PAGE[0] = 'Dashboard'
MENU['dashboard'] = 'current'


@auth.requires_login()
def index():
    SIDEBAR = False
    return dict(SIDEBAR=SIDEBAR)
