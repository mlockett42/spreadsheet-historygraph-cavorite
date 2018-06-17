from __future__ import absolute_import, unicode_literals, print_function


_users = []

def set_users(users):
    global _users
    _users = users

def get_users():
    global _users
    return _users

