# -*- coding: utf-8 -*-
"""Addressbook module docstring

This module have functions to help to manage an addressbook
"""
import cPickle as cp
import person_class


def addPerson(addressbookfile, Person):
    """savePerson
    Save person by name in the addressbook file"""

    # check when you add a person by first time or you already have
    try:
        f = file(addressbookfile, 'r')
    except IOError:
        f = file(addressbookfile, 'w')
        f.close()
        f = file(addressbookfile, 'r')

    if len(f.readline()) == 0:
        print 'Addressbook empty >> add the first person'
        store_person = {
            Person.name : {
                'name': Person.name,
                'email': Person.email,
                'phone': Person.phone
            }
        }
        save(addressbookfile, store_person)
    else:
        stored_persons = loadPersons(addressbookfile)
        print 'Addressbook with %d persons >> add a new person' % len(stored_persons)

        stored_persons[Person.name] = {
            'name': Person.name,
            'email': Person.email,
            'phone': Person.phone
        }
        save(addressbookfile,stored_persons)

    print 'contact added successful'


def save(addressbookfile, storeData):
    """save
    Save all data into file"""
    f = file(addressbookfile, 'w')
    cp.dump(storeData, f)
    f.close()


def loadPersons(addressbookfile):
    """loadPersons
    Lead all data from file"""
    f = file(addressbookfile)
    stored_persons = cp.load(f)
    return stored_persons


def searchPerson(addressbookfile, name):
    """SearchPerson
    Search person in the addressbook file, if it's found, show it"""
    f = file(addressbookfile)
    stored_persons = cp.load(f)
    p = person_class.Person(stored_persons[name]['name'], stored_persons[name]['email'], stored_persons[name]['phone'])
    p.showInfo()


def updatePerson(addressbookfile, name):
    """updatePerson
    Search person in the addressbook file, if it's found, update it"""
    f = file(addressbookfile)
    stored_persons = cp.load(f)
    if stored_persons.has_key(name):
        print stored_persons[name]
        del stored_persons[name]

        print 'Indica les noves dades'
        new_name = raw_input('Nom: ')
        new_email = raw_input('Email: ')
        new_phone = int(raw_input('Phone: '))

        stored_persons[new_name] = {
            'name': new_name,
            'email': new_email,
            'phone': new_phone
        }

        save(addressbookfile, stored_persons)
        print 'contact updated successful'
    else:
        raise KeyError


def deletePerson(addressbookfile, name):
    """deletePerson
    Search person in the addressbook file, if it's found, delete it"""
    f = file(addressbookfile)
    stored_persons = cp.load(f)
    if stored_persons.has_key(name):
        print stored_persons[name]
        del stored_persons[name]

        save(addressbookfile, stored_persons)
        print 'contact deleted successful'
    else:
        raise KeyError

version = '1.0.0'