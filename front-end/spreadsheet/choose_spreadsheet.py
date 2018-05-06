from __future__ import absolute_import, unicode_literals, print_function
try:
    import js
except ImportError:
    js = None
from cavorite.HTML import *
import rsa
import random

_public_key = None

def set_public_key(key):
    global _public_key
    _public_key = key

def get_public_key():
    global _public_key
    return _public_key

class ChooseSpreadsheetView(div):
    def __init__(self, *args, **kwargs):
        set_public_key(str(js.globals.document.body.getAttribute('data-current-user-public-key')))
        super(ChooseSpreadsheetView, self).__init__(*args, **kwargs)

    def onclick_new_passphrase(self, e):
        def custom_random(bytes):
            l = [random.randrange(256) for i in xrange(bytes)]
            return str(bytearray(l))
        rsa.set_custom_urandom(custom_random)
        passphrase = str(js.globals.document.getElementById('id_new_passphrase_input').value)
        random.seed(passphrase)
        (pubkey, privkey) = rsa.newkeys(512)
        print('Random pubkey/private key generateed. ')
        print('pubkey=', pubkey)
        print('privkey=', privkey)
        print('Sending public key to the server')

    def get_children(self):
        if get_public_key() == '':
            return [
                     p('You haven''t set up your key yet'),
                     p('Please enter a passphrase to generate your key'),
                     html_input({'id': 'id_new_passphrase_input'}),
                     html_button({'onclick': self.onclick_new_passphrase}, 'Submit') 
                   ]
        else:
            return [ p('Please enter your passphrase to continue') ]


def choose_spreadsheet_view():
    return ChooseSpreadsheetView()
