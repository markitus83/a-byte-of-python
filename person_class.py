# -*- coding: utf-8 -*-


class Person:
    """Represents a person to save into the addressbook"""

    def __init__(self, name, email, phone):
        """Constructor"""
        self.name = name
        self.email = email
        self.phone = phone

    def showInfo(self):
        """Show person's info"""
        print 'Name: %s - Email: %s - Phone: %d' % (self.name, self.email, self.phone)
