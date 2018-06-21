from __future__ import absolute_import, unicode_literals, print_function
try:
    import js
except ImportError:
    js = None
from cavorite.HTML import *
from . import myglobals
from cavorite.ajaxget import ajaxpost, ajaxget
from cavorite.timeouts import set_interval

public_sheets_loader_running = False
downloaded_public_sheet_edges = set()

class MainScreen(div):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        super(MainScreen, self).__init__(*args, **kwargs)
        global public_sheets_loader_running
        if public_sheets_loader_running is False:
            set_interval(self.load_public_sheets, 5000)
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

    def public_sheet_edge_downloaded(self, xmlhttp, response, key):
        #print('public_sheet_edge_downloaded called key=', key)
        global downloaded_public_sheet_edges
        downloaded_public_sheet_edges.add(key)

    def public_sheets_result_handler(self, xmlhttp, response):
        if xmlhttp.status >= 200 and xmlhttp.status <= 299:
            #print('public_sheets_result_handler called')
            #print('Public sheet list retreived', ' self=', self, ', xmlhttp.responseText=', xmlhttp.responseText, ' response=', response)
            global downloaded_public_sheet_edges
            # These XML fragments are Javascript objects so we need to navigate them with Javascript like constructs
            l = response.getElementsByTagName("Contents")
            for i in range(l.length):
                key_element = l[i].getElementsByTagName("Key")[0]
                key = str(key_element.childNodes[0].nodeValue)
                #print('Found key = ', key)
                if key not in downloaded_public_sheet_edges:
                    ajaxget('/storage/public/' + key, lambda xmlhttp, response, key=key: self.public_sheet_edge_downloaded(xmlhttp, response, key))
                else:
                    pass
                    #print('key=', key, ' already downloaded skippign')
            self.owner.mount_redraw()

    def load_public_sheets(self):
        global public_sheets_loader_running
        public_sheets_loader_running = True
        ajaxget('/storage/public/', self.public_sheets_result_handler)

