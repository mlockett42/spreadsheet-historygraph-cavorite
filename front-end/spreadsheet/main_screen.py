from __future__ import absolute_import, unicode_literals, print_function
try:
    import js
except ImportError:
    js = None
from cavorite.HTML import *
from . import myglobals
from cavorite.ajaxget import ajaxpost, ajaxget

public_sheets = None

class MainScreen(div):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        super(MainScreen, self).__init__(*args, **kwargs)
        if public_sheets is None:
            self.load_public_sheets()

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

    def public_sheets_result_handler(self, xmlhttp, response):
        if xmlhttp.status >= 200 and xmlhttp.status <= 299:
            print('Public sheet list retreived', ' self=', self, ', xmlhttp.responseText=', xmlhttp.responseText, ' response=', response)
            global public_sheets
            public_sheets = str(xmlhttp.responseText)
            # These XML fragments are Javascript objects so we need to navigate them with Javascript like constructs
            l = response.getElementsByTagName("Contents")
            print('l=', l)
            for i in range(l.length):
                print('i=', i)
                key_element = l[i].getElementsByTagName("Key")[0]
                print('key_elemen=', key_element)
                key = str(key_element.childNodes[0].nodeValue)
                print('key=', key)
            self.owner.mount_redraw()

    def load_public_sheets(self):
        ajaxget('/storage/public/', self.public_sheets_result_handler)

