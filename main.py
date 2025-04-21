from pdfrw import PdfWriter
from pdfrw.objects.pdfname import PdfName
from pdfrw.objects.pdfstring import PdfString
from pdfrw.objects.pdfdict import PdfDict
from pdfrw.objects.pdfarray import PdfArray


def create_page(width: int, height: int) -> PdfDict:
    page = PdfDict()
    page.Type = PdfName.Page
    page.MediaBox = PdfArray([0, 0, width, height])

    page.Resources = PdfDict()
    page.Resources.Font = PdfDict()
    page.Resources.Font.F1 = PdfDict()
    page.Resources.Font.F1.Type = PdfName.Font
    page.Resources.Font.F1.Subtype = PdfName.Type1
    page.Resources.Font.F1.BaseFont = PdfName.Courier

    return page


def create_script(js) -> PdfDict:
    action = PdfDict()
    action.S = PdfName.JavaScript
    action.JS = js
    return action


writer = PdfWriter()
page = create_page(500, 500)
page.Contents = PdfDict()
page.AA = PdfDict()
page.AA.o = create_script("app.alert('hi)")
with open("./code.js", "r") as f:
    page.AA.O = create_script(f.read())
writer.addpage(page)
writer.write("./scriptTest.pdf")
