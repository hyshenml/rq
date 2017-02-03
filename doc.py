# -*- coding: utf-8 -*-

import zipfile
import re
from xml.dom.minidom import parse
import xml.dom.minidom
'''
document = zipfile.ZipFile('e:\\workspace\\rq\llj.docx')
xml_content = document.read('word/document.xml')

f=open('e:\\test.xml','wb')
f.write(xml_content)
f.close()
'''
class TextParser():
    def __init__(self):
        self.str=''

    def getNodeText(self,element):
        self.str = ''
        self._getNodeText(element)
        return self.str

    def _getNodeText(self,element):
        subNodes = element.childNodes

        if len(subNodes) >= 1:
            for subNode in subNodes:
                self._getNodeText(subNode)
        if element.firstChild is None:
            pass
        else:
            try:
                self.str=self.str+element.firstChild.data
            except Exception, e:
                pass

document = zipfile.ZipFile('e:\\workspace\\rq\wx.docx')
dom = xml.dom.minidom.parseString(document.read('word/document.xml'))
t=TextParser()

tabs=dom.getElementsByTagName('w:tbl')
for tab in tabs:
    print '##################'
    lines=tab.getElementsByTagName('w:tr')
    for line in lines:
        cells=line.getElementsByTagName('w:tc')
        if len(cells)==2:
            try:
                name=t.getNodeText(cells[0])
                data=t.getNodeText(cells[1])
                print '$',name,':',data
            except Exception ,e:
                print e
'''

from win32com import client as wc
word = wc.Dispatch('Word.Application')
doc = word.Documents.Open('e:\\workspace\\rq\wl.doc')
doc.SaveAs('c:/test1.text', 4)
doc.Close()
'''