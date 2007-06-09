# -*- coding: utf8 -*-
"""Interface module, it enables communication beetwen user and program"""
import sys
import wx
import os

sys.path.append(sys.path[0]+"/files")

from control import *
class GUI(Control) :
    """Grafical interface"""
    def showInterface(self) :
        """Opens grafical interface (an object wx.Frame class)"""
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        Snakereader = MyFrame(None, -1, "")
        app.SetTopWindow(Snakereader)
        Snakereader.Show()
        app.MainLoop()
class CommandLine(Control) :
    """Program starts from command line"""
    def readCommandLine(self) :
        """Reads and changes options"""
        for i in range (0, len(sys.argv)):
            if sys.argv[i] == '-d':
                self.options[0] = sys.argv[i+1]
            if sys.argv[i] == '-s':
                self.options[1] = sys.argv[i+1]
            if sys.argv[i] == '-r':
                self.options[2] = sys.argv[i+1]
            if sys.argv[i] == '-q':
                self.options[3] = sys.argv[i+1]

#-----------------GUI----------------#

ID_OPEN = 11
ID_SAVE = 12
ID_EXIT = 13

ID_OPT = 21
ID_DEF = 22
ID_SAVE_O = 23

ID_RECOG = 31

ID_DOCUM = 41
ID_REQUIR = 42
ID_ABOUT = 43

ID_OPEN_B = 51
ID_RECOG_B = 52
ID_SAVE_B = 53
ID_OPT_B = 54

class Options(wx.Frame):
    def __init__(self, dicList, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_4 = wx.StaticText(self, -1, "")
        self.radio_box_1 = wx.RadioBox(self, -1, "Choose a dictonary", choices=dicList, majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_2 = wx.RadioBox(self, -1, "Choose quality", choices=["good","poor"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.static_line_1 = wx.StaticLine(self, -1)
        self.label_5 = wx.StaticText(self, -1, "Technical data:")
        self.label_6 = wx.StaticText(self, -1, "Font size   ")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "")
        self.label_7 = wx.StaticText(self, -1, "Scan resolution   ")
        self.text_ctrl_4 = wx.TextCtrl(self, -1, "")
        self.static_line_2 = wx.StaticLine(self, -1)
        self.button_1 = wx.Button(self, -1, "OK")
        self.Bind(wx.EVT_BUTTON, self.OnOK)
        self.__set_properties()
        self.__do_layout()
        
        # end wxGlade
        
    def OnOK(self, e = None):
        interface.options[0] = interface.dictionaries[self.radio_box_1.GetSelection()]
        interface.options[1] = self.text_ctrl_3.GetValue()
        interface.options[2] = self.text_ctrl_4.GetValue()
        if self.radio_box_2.GetSelection()==0:
            interface.options[3] = "good"
        else:
            interface.options[3] = "poor"
        self.Close(True)

    def OnCancel(self, e = None):
        self.Close(True)
        
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Options")
        self.SetSize((300, 264))
        self.SetBackgroundColour(wx.Colour(236, 233, 216))
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.radio_box_1.SetSelection(0)
        self.radio_box_1.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11.Add(self.label_4, 0, 0, 0)
        sizer_12.Add(self.radio_box_1, 0, wx.SHAPED, 0)
        sizer_11.Add(sizer_12, 0, wx.EXPAND, 0)
        sizer_11.Add(self.radio_box_2, 0, wx.SHAPED, 0)
        sizer_11.Add(self.static_line_1, 2, wx.EXPAND, 0)
        sizer_10.Add(sizer_11, 3, wx.EXPAND, 0)
        sizer_13.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 0, 0, 0)
        grid_sizer_1.Add(self.label_7, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 0, 0, 0)
        sizer_15.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_14.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_13.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_13.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_10.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_10.Add(self.button_1, 0, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(sizer_10, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class Options

class MyScroll(wx.ScrolledWindow):
    def __init__(self, parent, id = -1, size = 356, bitmap=None):
        wx.ScrolledWindow.__init__(self, parent, id, wx.Point(0, 0), (350,700), wx.SUNKEN_BORDER)
        if bitmap!=None:
            self.buffer=wx.Bitmap(bitmap)
        else:
            self.buffer=wx.EmptyBitmap(350,700)
        dc=wx.BufferedDC(None, self.buffer)

        wx.EVT_PAINT(self,self.OnPaint)
        
    def OnPaint(self,event):
        dc = wx.BufferedPaintDC(self,self.buffer)

# end of class MyScroll

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.Snakereader_menubar = wx.MenuBar()
        self.SetMenuBar(self.Snakereader_menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(11, "Open", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(12, "Save", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(13, "Exit", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(21, "Options", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(22, "Default", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(23, "Save Options", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "Options")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(31, "Recognize", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "Recognize")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(41, "Documention", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(42, "Requirements", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(43, "About Snakereader", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "Help")
        # Menu Bar end
        
        # Tool Bar
        self.Snakereader_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.Snakereader_toolbar)
        self.Snakereader_toolbar.AddLabelTool(51, "Open", wx.Bitmap(".//files//Open.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Open", "")
        self.Snakereader_toolbar.AddLabelTool(52, "Recognize", wx.Bitmap(".//files//Recognize.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Recognize", "")
        self.Snakereader_toolbar.AddLabelTool(53, "Save", wx.Bitmap(".//files//Save.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Save", "")
        self.Snakereader_toolbar.AddSeparator()
        self.Snakereader_toolbar.AddLabelTool(54, "Options", wx.Bitmap(".//files//Options.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Options", "")
        # Tool Bar end

        
        self.bitmap = MyScroll(self)
        
        self.static_line = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        self.picture = None
        scroll=wx.ScrolledWindow(self,-1)
        self.text = "An outcome text will be there"
        self.text_ctrl = wx.TextCtrl(self, -1, self.text, style=wx.TE_MULTILINE)
        
        self.__set_properties()
        self.__do_layout(self.bitmap)

        self.Bind(wx.EVT_MENU, self.a, id=11)
        # end wxGlade
        

        wx.EVT_MENU(self, ID_OPEN, self.OnOpen)
        wx.EVT_MENU(self, ID_SAVE, self.OnSave)
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, ID_OPT, self.OnOpt)
        wx.EVT_MENU(self, ID_DEF, self.OnDef)
        wx.EVT_MENU(self, ID_SAVE_O, self.OnSaveO)
        wx.EVT_MENU(self, ID_RECOG, self.OnRecog)
        #wx.EVT_MENU(self, ID_DOCUM, self.OnDocum)
        wx.EVT_MENU(self, ID_REQUIR, self.OnRequir)
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
        wx.EVT_TOOL(self, ID_OPEN_B, self.OnOpen)
        wx.EVT_TOOL(self, ID_RECOG_B, self.OnRecog)
        wx.EVT_TOOL(self, ID_SAVE_B, self.OnSave)
        wx.EVT_TOOL(self, ID_OPT_B, self.OnOpt)
      


    def OnOpen(self,e):
        """ Open a file"""
        self.dirname = ''
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.filename=dialog.GetFilename()
            self.dirname=dialog.GetDirectory()
            self.picture = interface.inputFile(unicode.encode(self.dirname+"\\"+self.filename))
            self.bitmap_1 = (unicode.encode(self.dirname+"\\"+self.filename))

            """ tu jest skalowanie, ale na obrazku,
                po skalowaniu otrzymujemy tez obrazek.
                No i nie mozna go podac do MyScroll,
                tzn. nie mozna zrobic czegos takiego:
                self.bitmap = MyScroll(self, bitmap = self.bitmap_2)
                nie bylo by problemu gdyby bitmap_2 byla zadana jak 7 linijek wyzej.
                Rozwiazaniem mogloby byc zapisanie bitmap_2
                do jakiegos pliku tymczasowego, wywolanie MyScroll
                i zniszczenie pliku, ale to troche niefajna metoda
                moze masz jakis pomysl??
            
            self.bitmap_2 = wx.Image(unicode.encode(self.dirname+"\\"+self.filename), wx.BITMAP_TYPE_ANY) 
            W = self.bitmap_2.GetWidth()
            H = self.bitmap_2.GetHeight()
            if (W/H > 350/700):
                NewW = 350
                NewH = 350 * H / W
            else:   
                NewH = 700
                NewW = 700 * W / H
            self.bitmap_2 = self.bitmap_2.Scale(NewW,NewH)"""
            
            self.bitmap = MyScroll(self)
            self.__do_layout(self.bitmap)
            self.bitmap = MyScroll(self, bitmap = self.bitmap_1)
            self.__do_layout(self.bitmap)

        dialog.Destroy()

    def OnSave(self,e):
        self.dirname = ''
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            self.filename=dialog.GetFilename()+".txt"
            self.dirname=dialog.GetDirectory()
            outputFile = open(os.path.join(self.dirname, self.filename), "w")
            outputFile.write(self.text_ctrl.GetValue())
            outputFile.close()

    def OnExit(self,e):
        self.Close(True)
    
    def OnOpt(self,e):
        optionsWindow=Options(interface.dictionaries, None)
        optionsWindow.Show()

    def OnDef(self,e):
        interface.options=['None','','',"poor"]

    def OnSaveO(self,e):
        interface.saveOptions()

    def OnRecog(self,e):
        dialog = wx.ProgressDialog("Progress", "Please, wait a while...", style = wx.PD_ELAPSED_TIME)
        try:
            self.text=interface.textRecognition(self.picture)
        except IOError, details:
            print "Error:", details
        self.text_ctrl.Destroy()
        self.text_ctrl = wx.TextCtrl(self, 1, self.text, style=wx.TE_MULTILINE)
        self.__do_layout(self.bitmap)
        dialog.Destroy()

    #def OnDocum(self,e):
    
    def OnRequir(self,e):
        dialog = wx.MessageDialog(self, "INPUT DATA:\n"
                                  "text document as a picture (bmp or jpg format):\n"
                                  "\t - polish language,\n"
                                  "\t - not handwriting,\n"
                                  "\t - text (and background) in one colour and tint,\n"
                                  "\t - contrast between text and background,\n"
                                  "\t - resolution min 300dpi,\n"
                                  "\t - homogeneous arrangement (without text areas, pictures, etc.)\n\n"
                                  "OUTPUT DATA:\n"
                                  "document converted to an electronic form and saved in txt format", "Requirements", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

        
    def OnAbout(self,e):
        dialog = wx.MessageDialog(self, "Snakereader is an Open Source project \n"
                                  "created by students of Wroclaw University of Technology \n\n"
                                  "Wroclaw, 2007","About", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()     
    

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Snakereader")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap(".//files//Snake.bmp", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((901, 581))
        self.Snakereader_toolbar.SetToolBitmapSize((30, 30))
        self.Snakereader_toolbar.Realize()
        self.text_ctrl.SetMinSize((100, 100))
        # end wxGlade

    def __do_layout(self, bitmap):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.bitmap, 0, 0, 0)
        sizer_1.Add(self.static_line, 0, wx.EXPAND, 0)
        sizer_1.Add(self.text_ctrl, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def a(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `a' not implemented!"
        event.Skip()

# end of class MyFrame







#-----------------INTERFACE----------------#
                
#sys.argv.append('l1.jpg')
#sys.argv.append('a.txt')
#sys.argv.append('-q')
#sys.argv.append('poor')
if len(sys.argv)>1:
    commandLine=CommandLine()
    commandLine.readCommandLine()
    try:
        picture=commandLine.inputFile(sys.argv[1])
    except IOError, details:
        print "Error:", details
    else:
        try:
            text=commandLine.textRecognition(picture)
        except IOError, details:
            print "Error:", details
        else:
            outputFile=open(sys.argv[2],'w')
            outputFile.write(text)
            outputFile.close()
else:
    interface=GUI()
    interface.showInterface()
