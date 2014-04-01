# -*- coding: utf-8 -*-


PAGE[0] = 'Dashboard'
MENU['dashboard'] = 'current'


@auth.requires_login()
def index():
    if 'SUPPORT' in auth.user_groups.values():
        redirect(URL('init', 'customers', 'index'))
    SIDEBAR = False
    return dict(SIDEBAR=SIDEBAR)
