from __future__ import absolute_import, unicode_literals, print_function


_users = []

def set_users(users):
    global _users
    _users = users

def get_users():
    global _users
    return _users

_dc = None

def set_dc(dc):
    global _dc
    _dc = dc

def get_dc():
    global _dc
    return _dc

