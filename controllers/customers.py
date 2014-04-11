# -*- coding: utf-8 -*-
from gluon.tools import Service


PAGE[0] = 'Clientes'
MENU['customers'] = 'current'
service = Service()


def api():
    return service()

# Section: Web Services {{{1
#------------------------------------------------------------------------------


@service.json
def upload():
    #Upload a file from customer section to 'uploads' path.
    return str(request.vars)


# Section: Views {{{1
#------------------------------------------------------------------------------


@auth.requires(auth.has_membership(role='ADMIN') or
               auth.has_membership(role='SUPPORT'))
def index():
    SIDEBAR = False
    return dict(SIDEBAR=SIDEBAR)


def unsubscribe():
    SIDEBAR = False
    return dict()


def other():
    SIDEBAR = False
    return dict()