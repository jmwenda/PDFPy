import argparse
from lxml import etree

parser = argparse.ArgumentParser(description='Tool for consuming xml"s produced by pdfminer')
parser.add_argument("-f","--file",dest="xmlfile", type=file,help="Consume the xml file",metavar="PATH")

args = parser.parse_args()

def process_textlines(textbox):
    textlines = textbox.getchildren()
    lines = []
    for textline in textlines:
        texts = textline.getchildren()
        cellvalue = ''
        for text in texts:
            cellvalue = cellvalue + text.text 
            #cellbox = text.attrib['bbox']
        lines.append(cellvalue)
    return lines
def process_page(page):
    #script that gets a page element and creates the csv
    page_bounds = page.attrib['bbox'] 
    textboxes = page.getchildren()
    for textbox in textboxes:
        textbox_bounds = textbox.attrib['bbox']
        text_string = process_textlines(textbox)
        print text_string
def process_file():
    if args.xmlfile:
        #we now consume the xml file,first open then read
        file = open(args.xmlfile.name,'r')
        data = file.read()
        root = etree.fromstring(data)
        #we now cosume the formatted xml with lxml 
        #we get the page with the bbox items
        pages = root.getchildren()
        for page in pages:
            process_page(page);
    return root
print process_file()

