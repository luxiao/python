# -*- coding: cp936 -*-
import win32com
from win32com.client import Dispatch, constants

def myword():
  w = win32com.client.Dispatch('Word.Application')
  # 或者使用下面的方法，使用启动独立的进程：
  # w = win32com.client.DispatchEx('Word.Application')

  # 后台运行，不显示，不警告
  w.Visible = 0
  w.DisplayAlerts = 0

  # 打开新的文件
  doc = w.Documents.Open( FileName = filenamein )
  # worddoc = w.Documents.Add() # 创建新的文档

  # 插入文字
  myRange = doc.Range(0,0)
  myRange.InsertBefore('Hello from Python!')

  # 使用样式
  wordSel = myRange.Select()
  wordSel.Style = constants.wdStyleHeading1

  # 正文文字替换
  w.Selection.Find.ClearFormatting()
  w.Selection.Find.Replacement.ClearFormatting()
  w.Selection.Find.Execute(OldStr, False, False, False, False, False, True, 1, True, NewStr, 2)

  # 页眉文字替换
  w.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
  w.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
  w.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(OldStr, False, False, False, False, False, True, 1, False, NewStr, 2)

  # 表格操作
  doc.Tables[0].Rows[0].Cells[0].Range.Text ='123123'
  worddoc.Tables[0].Rows.Add() # 增加一行

  # 转换为html
  wc = win32com.client.constants
  w.ActiveDocument.WebOptions.RelyOnCSS = 1
  w.ActiveDocument.WebOptions.OptimizeForBrowser = 1
  w.ActiveDocument.WebOptions.BrowserLevel = 0 # constants.wdBrowserLevelV4
  w.ActiveDocument.WebOptions.OrganizeInFolder = 0
  w.ActiveDocument.WebOptions.UseLongFileNames = 1
  w.ActiveDocument.WebOptions.RelyOnVML = 0
  w.ActiveDocument.WebOptions.AllowPNG = 1
  w.ActiveDocument.SaveAs( FileName = filenameout, FileFormat = wc.wdFormatHTML )

  # 打印
  doc.PrintOut()

  # 关闭
  # doc.Close()
  w.Documents.Close(wc.wdDoNotSaveChanges)
  w.Quit()
class WordWrap:
  """Wrapper around Word 8 documents to make them easy to build.
  Has variables for the Applications, Document and Selection; 
  most methods add things at the end of the document"""
  def __init__(self,start,templatefile=None):
    self.wordApp = Dispatch('Word.Application')
    if templatefile == None:
      self.wordDoc = self.wordApp.Documents.Add()
    else:
      self.wordDoc = self.wordApp.Documents.Add(Template=templatefile)
    
    #set up the selection wii 870,871
    self.wordDoc.Range(start,int(start)+1).Select()
    self.wordSel = self.wordApp.Selection
    #fetch the styles in the document - see below
    #self.getStyleDictionary()
  def quit(self):
    self.wordApp.Quit()
  def show(self):
    # convenience when developing
    self.wordApp.Visible = 1  

  def saveAs(self, filename):
    self.wordDoc.SaveAs(filename)
     
  def printout(self):
    self.wordDoc.PrintOut()

  def selectEnd(self):
    # ensures insertion point is at the end of the document
    self.wordSel.Collapse(0)
    # 0 is the constant wdCollapseEnd; don't want to depend
    # on makepy support.

  def addText(self, text):
    self.wordSel.InsertAfter(text)
    self.selectEnd()
  def inTextObj(self,filename):
    self.wordSel.InsertFile(filename)
  def textReplace(self,oldStr,newStr):
    self.wordSel.Find.ClearFormatting()
    self.wordSel.Find.Replacement.ClearFormatting()
    self.wordSel.Find.Execute(oldStr, False, False, False, False, False, True, 1, True, newStr, 2)

  def  addInlineObj(self, filename, caption='', 
                 height=65, width=60):
    # adds a chart inline within the text, caption below.
    
    # add an InlineShape to the InlineShapes collection 
    #- could appear anywhere
    shape = self.wordDoc.InlineShapes.AddOLEObject(
        ClassType='Excel.Chart',
        FileName=filename
        )
    # set height and width in points
    shape.Height = height
    shape.Width = width
    
    # put it where we want
    shape.Range.Cut()

    #self.wordSel.InsertAfter('TOM')
    self.wordSel.Range.Paste()  # goes in selection
    #self.addStyledPara(caption, 'Normal')
