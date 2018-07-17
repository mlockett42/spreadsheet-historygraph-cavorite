from historygraph_wrapper import DocumentCollection
from historygraph_wrapper import Document
from historygraph_wrapper import DocumentObject
from historygraph_wrapper import fields


dc1 = DocumentCollection()

class SpreadsheetCell(DocumentObject):
    content = fields.CharRegister()

class SpreadsheetColumn(DocumentObject):
    name = fields.CharRegister()
    cells = fields.List(SpreadsheetCell)

class SpreadsheetShare(DocumentObject):
    email = fields.CharRegister()

class Spreadsheet(Document):
    name = fields.CharRegister()
    columns = fields.List(SpreadsheetColumn)
    shares = fields.Collection(SpreadsheetShare)

def CreateNewDocumentCollection():
    dc = DocumentCollection()
    dc.register(Spreadsheet)
    dc.register(SpreadsheetColumn)
    dc.register(SpreadsheetCell)
    dc.register(SpreadsheetShare)
    return dc
