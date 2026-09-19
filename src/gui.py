# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"MainFrame"), pos = wx.DefaultPosition, size = wx.Size( 590,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar = wx.MenuBar( 0 )
        self.m_menuFile = wx.Menu()
        self.m_menuFileExit = wx.MenuItem( self.m_menuFile, wx.ID_ANY, _(u"E&xit")+ u"\t" + u"Alt+X", _(u"Quit this app"), wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuFileExit )

        self.m_menubar.Append( self.m_menuFile, _(u"&File") )

        self.m_menuHelp = wx.Menu()
        self.m_menuHelpAbout = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, _(u"&About")+ u"\t" + u"F1", _(u"Show about dialog"), wx.ITEM_NORMAL )
        self.m_menuHelp.Append( self.m_menuHelpAbout )

        self.m_menubar.Append( self.m_menuHelp, _(u"&Help") )

        self.SetMenuBar( self.m_menubar )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panelEncode = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panelEncode, wx.ID_ANY, _(u"Path to the carrier image file (PNG/JPG)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

        bSizerCarrier = wx.BoxSizer( wx.HORIZONTAL )

        self.m_carrierFilePath = wx.TextCtrl( self.m_panelEncode, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_carrierFilePath.SetMinSize( wx.Size( 380,-1 ) )

        bSizerCarrier.Add( self.m_carrierFilePath, 0, wx.ALL, 5 )

        self.btnOpenCarrierFile = wx.Button( self.m_panelEncode, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerCarrier.Add( self.btnOpenCarrierFile, 0, wx.ALL, 5 )


        bSizer3.Add( bSizerCarrier, 0, wx.EXPAND, 5 )

        self.m_staticline2 = wx.StaticLine( self.m_panelEncode, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panelEncode, wx.ID_ANY, _(u"Path to the secret file to hide"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

        bSizerSecret = wx.BoxSizer( wx.HORIZONTAL )

        self.m_secretFilePath = wx.TextCtrl( self.m_panelEncode, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_secretFilePath.SetMinSize( wx.Size( 380,-1 ) )

        bSizerSecret.Add( self.m_secretFilePath, 0, wx.ALL, 5 )

        self.btnOpenSecretFile = wx.Button( self.m_panelEncode, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerSecret.Add( self.btnOpenSecretFile, 0, wx.ALL, 5 )


        bSizer3.Add( bSizerSecret, 0, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self.m_panelEncode, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panelEncode, wx.ID_ANY, _(u"Path to save the resulting stego-image"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

        bSizerSave = wx.BoxSizer( wx.HORIZONTAL )

        self.m_resultEncodedFilePath = wx.TextCtrl( self.m_panelEncode, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_resultEncodedFilePath.SetMinSize( wx.Size( 380,-1 ) )

        bSizerSave.Add( self.m_resultEncodedFilePath, 0, wx.ALL, 5 )

        self.btnOpenResultFile = wx.Button( self.m_panelEncode, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerSave.Add( self.btnOpenResultFile, 0, wx.ALL, 5 )


        bSizer3.Add( bSizerSave, 1, wx.EXPAND, 5 )


        self.m_panelEncode.SetSizer( bSizer3 )
        self.m_panelEncode.Layout()
        bSizer3.Fit( self.m_panelEncode )
        self.m_notebook.AddPage( self.m_panelEncode, _(u"Encode"), False )
        self.m_panelDecode = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook.AddPage( self.m_panelDecode, _(u"Decode"), False )

        bSizer1.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.btnClearFields = wx.Button( self, wx.ID_ANY, _(u"Clear\nFields"), wx.DefaultPosition, wx.Size( -1,40 ), 0 )
        bSizer6.Add( self.btnClearFields, 0, wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btnCompute = wx.Button( self, wx.ID_ANY, _(u"Compute"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnCompute, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.OnExitClick, id = self.m_menuFileExit.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAboutClick, id = self.m_menuHelpAbout.GetId() )
        self.m_notebook.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onTabChanged )
        self.btnOpenCarrierFile.Bind( wx.EVT_BUTTON, self.onSelectCarrierFile )
        self.btnOpenSecretFile.Bind( wx.EVT_BUTTON, self.onSelectSecretFile )
        self.btnOpenResultFile.Bind( wx.EVT_BUTTON, self.onSelectEncodedFile )
        self.btnClearFields.Bind( wx.EVT_BUTTON, self.onClearFields )
        self.btnCompute.Bind( wx.EVT_BUTTON, self.onCompute )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnExitClick( self, event ):
        event.Skip()

    def OnAboutClick( self, event ):
        event.Skip()

    def onTabChanged( self, event ):
        event.Skip()

    def onSelectCarrierFile( self, event ):
        event.Skip()

    def onSelectSecretFile( self, event ):
        event.Skip()

    def onSelectEncodedFile( self, event ):
        event.Skip()

    def onClearFields( self, event ):
        event.Skip()

    def onCompute( self, event ):
        event.Skip()


