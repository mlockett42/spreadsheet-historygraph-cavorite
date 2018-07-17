from __future__ import absolute_import, unicode_literals, print_function
try:
    import js
except ImportError:
    js = None
from cavorite.HTML import *
import rsa
import random
from cavorite.ajaxget import ajaxpost, ajaxget
import base64
from cavorite import SimpleProxy
from cavorite.timeouts import set_timeout
from .main_screen import MainScreen
from . import myglobals
import json

_public_key = None

def set_public_key(key):
    global _public_key
    _public_key = key

def get_public_key():
    global _public_key
    return _public_key

_private_key = None

def set_private_key(key):
    global _private_key
    _private_key = key

def get_private_key():
    global _private_key
    return _private_key

def new_keys_from_passphrase(passphrase):
    def custom_random(bytes):
        l = [random.randrange(256) for i in xrange(bytes)]
        return str(bytearray(l))
    rsa.set_custom_urandom(custom_random)
    random.seed(passphrase)
    (pubkey, privkey) = rsa.newkeys(512)
    print('Random pubkey/private key generateed. ')
    print('pubkey=', pubkey)
    print('privkey=', privkey)
    return (pubkey, privkey)

class ChooseSpreadsheetView(SimpleProxy):
    def __init__(self, *args, **kwargs):
        #print('ChooseSpreadsheetView __init__ called')
        set_public_key(str(js.globals.document.body.getAttribute('data-current-user-public-key')))    
        self.display_main_screen = False
        super(ChooseSpreadsheetView, self).__init__(*args, **kwargs)

    def change_to_main_screen(self):
        #print('Updating screen after timeout self=', self)
        self.display_main_screen = True
        self.mount_redraw()

    def users_result_handler(self, xmlhttp, response):
        if xmlhttp.status >= 200 and xmlhttp.status <= 299:
            print('User list retreived', ' self=', self)
            myglobals.set_users(json.loads(str(xmlhttp.responseText)))
            self.mount_redraw()

    def load_user_list(self):
        ajaxget('/api/accounts/', self.users_result_handler)


    def onclick_new_passphrase(self, e):
        (pubkey, privkey) = new_keys_from_passphrase(str(js.globals.document.getElementById('id_new_passphrase_input').value))
        print('Sending public key to the server')
        pubkey_bin = base64.b64encode(pubkey.save_pkcs1(format='DER'))
        print('pubkey_bin=', pubkey_bin)
        form_data = {'public_key': pubkey_bin}
        def ajaxpost_result_handler(xmlhttp, response):
            print('ajaxpost_result_handler called')
            set_public_key(pubkey)
            set_private_key(privkey)
            set_timeout(self.change_to_main_screen, 1000)
            self.load_user_list()
            self.mount_redraw()
        ajaxpost('/api/accounts/setpublickey/', form_data, ajaxpost_result_handler)

    def onclick_existing_passphrase(self, e):
        (pubkey, privkey) = new_keys_from_passphrase(str(js.globals.document.getElementById('id_new_passphrase_input').value))
        pubkey_bin = base64.b64encode(pubkey.save_pkcs1(format='DER'))
        if pubkey_bin == get_public_key():
            print('Public keys match')
            set_public_key(pubkey)
            set_private_key(privkey)
            set_timeout(self.change_to_main_screen, 1000)
            self.load_user_list()
            self.mount_redraw()
        else:
            print('public keys do not match')

    def get_proxy(self):
        #print('get_proxy called self.display_main_screen=', self.display_main_screen, ' self=', self)
        global display_main_screen
        if get_public_key() == '':
            return div([
                         p('You haven''t set up your key yet'),
                         p('Please enter a passphrase to generate your key'),
                         html_input({'id': 'id_new_passphrase_input'}),
                         html_button({'onclick': self.onclick_new_passphrase}, 'Submit') 
                       ])
        elif get_private_key() is None:
            return div([
                         p('You have generated a key previously. Please enter your passphrase to continue') ,
                         html_input({'id': 'id_new_passphrase_input'}),
                         html_button({'onclick': self.onclick_existing_passphrase}, 'Submit') 
                       ])
        elif not self.display_main_screen:
            #print('1 get_proxy')
            return div([ p('Congratulations you are logged in and your key is set up correctly') ])
        else:
            #print('2 get_proxy')
            return MainScreen(self)

def choose_spreadsheet_view():
    return ChooseSpreadsheetView()
