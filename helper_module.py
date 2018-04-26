# -*- coding: utf-8 -*-
"""Helper module docstring

This module have functions to help to develop
"""
menu_option = None


def showMenu():
    """showMenu
    Show the menu with options for the user and catch the user's option"""
    print '''\nIndica una opció:
        1 Afegir contacte
        2 Modificar contacte
        3 Eliminar contacte
        4 Cercar contacte
        5 Info de l'agenda
        0 Sortir\n'''

    try:
        global menu_option
        menu_option = int(raw_input('Opció escollida: '))
    except ValueError:
        print 'Error al escollir l\'opció'


def getMenuOption():
    """Return the user's option"""
    return menu_option





version = '1.0.0'