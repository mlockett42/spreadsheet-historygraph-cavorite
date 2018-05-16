from historygraph_wrapper import DocumentCollection
from historygraph_wrapper import Document
from historygraph_wrapper import DocumentObject
from historygraph_wrapper import FieldText
from historygraph_wrapper import FieldIntRegister
from historygraph_wrapper import FieldIntCounter
from historygraph_wrapper import FieldList
from historygraph_wrapper import FieldCollection


dc1 = DocumentCollection()

class SpreadsheetCell(DocumentObject):
    content = FieldText()

class SpreadsheetColumn(Document):
    name = FieldText()
    items = FieldList(SpreadsheetCell)

class SpreadsheetShare(DocumentObject):
    email = FieldText()

class Spreadsheet(Document):
    name = FieldText()
    lists = FieldList(TrelloListLink)
    shares = FieldCollection(TrelloShare)

def CreateNewDocumentCollection(dcid):
    dc = DocumentCollection(dcid)
    dc.Register(Spreadsheet)
    dc.Register(SpreadsheetColumn)
    dc.Register(SpreadsheetCell)
    dc.Register(SpreadsheetShare)
    return dc

