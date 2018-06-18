from __future__ import absolute_import, unicode_literals, print_function
try:
    import js
except ImportError:
    js = None
from cavorite.HTML import *
from . import myglobals


class MainScreen(div):
    def get_children(self):
        #print('MainScreen get_children')
        ret = [ p('Users')  ] + list([p(u['email']) for u in myglobals.get_users()])
        #print('MainScreen get_children ret=', ret)
        #print('MainScreen user names = ', [u['email'] for u in myglobals.get_users()])
        return ret

    def get_attribs(self):
        #print('MainScreen get_attribs called')
        attribs = super(MainScreen, self).get_attribs()
        attribs['class'] = 'main-screen'
        return attribs


