from __future__ import absolute_import, unicode_literals, print_function
try:
    import js
except ImportError:
    js = None
from cavorite.HTML import *
from . import myglobals


class MainScreen(div):
    def get_children(self):
        return [ p('Users') ] + [p(u['email']) for u in myglobals.get_users()]


