import argparse
from lxml import etree

parser = argparse.ArgumentParser(description='Tool for consuming xml"s produced by pdfminer')
parser.add_argument("-f","--file",dest="xmlfile", type=file,help="Consume the xml file",metavar="PATH")

args = parser.parse_args()
def process_file():
    if args.xmlfile:
        #we now consume the xml file,first open then read
        file = open(args.xmlfile.name,'r')
        data = file.read()
        root = etree.fromstring(data)
        #we now cosume the formatted xml with lxml 
    return root
print process_file()

