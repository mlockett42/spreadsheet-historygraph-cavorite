# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import json
from spreadsheet.storage import message_media_storage
import hashlib
from StringIO import StringIO

def create_public_spreadsheet():
    from historygraph_backend.documents.documents import CreateNewDocumentCollection, Spreadsheet, SpreadsheetColumn, SpreadsheetCell

    dc = CreateNewDocumentCollection()
    spreadsheet = Spreadsheet()
    dc.add_document_object(spreadsheet)
    for i in range(5):
        col = SpreadsheetColumn()
        spreadsheet.columns.append(col)
        dc.add_document_object(col)
        for j in range(5):
            cell = SpreadsheetCell()
            col.cells.append(cell)
            dc.add_document_object(cell)

    for edge in dc.get_all_edges()[0]:
        json_text = json.dumps(edge)
        message_media_storage.save('public/{0}'.format( 
                                   hashlib.sha256(json_text).hexdigest()), StringIO(json_text))

