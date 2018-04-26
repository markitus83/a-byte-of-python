# -*- coding: utf-8 -*-

# Creació d'una agenda
# Permet: afegir, modificar, eliminar o cercar contactes i la seva informació com adreça de correu i/o telèfon

import addressbook_module as ab
import helper_module as helper
import person_class as person
import sys


addressbook = {}
addressbookfile = 'addressbook.txt'

while True:
    helper.showMenu()
    option = helper.getMenuOption()
    if option == 0:
        # exit
        print 'Gràcies'
        sys.exit()
    elif option == 1:
        # add new contact
        print '** Crear contacte **'
        name = raw_input('Nom: ')
        email = raw_input('Email: ')
        phone = int(raw_input('Phone: '))

        p = person.Person(name, email, phone)
        ab.addPerson(addressbookfile, p)
    elif option == 2:
        # update contact
        print '** Actualitzar contacte **'
        try:
            ab.updatePerson(addressbookfile, raw_input('Nom a buscar: '))
        except KeyError:
            print 'Contact not found'
        except IOError:
            print 'No such file or directory'
    elif option == 3:
        # delete contact
        print '** Eliminar contacte **'
        try:
            ab.deletePerson(addressbookfile, raw_input('Nom a buscar: '))
        except KeyError:
            print 'Contact not found'
        except IOError:
            print 'No such file or directory'
    elif option == 4:
        # search contact and show the info
        print '** Cercar contacte **'
        try:
            ab.searchPerson(addressbookfile, raw_input('Nom a buscar: '))
        except KeyError:
            print 'Contact not found'
        except IOError:
            print 'No such file or directory'
    elif option == 5:
        # show info from addressbook
        print '** Info de l\'agenda **'
        try:
            addressbook = ab.loadPersons(addressbookfile)
            print 'Your addressbook have: %d contact/s' % len(addressbook)
            for key in addressbook.keys():
                contact = addressbook[key]
                p = person.Person(contact['name'], contact['email'], contact['phone'])
                p.showInfo()
        except EOFError:
            print 'Your addressbook is empty'
        except IOError:
            print 'No such file or directory'
