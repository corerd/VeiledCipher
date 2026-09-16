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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"MainFrame"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
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


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.OnExitClick, id = self.m_menuFileExit.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAboutClick, id = self.m_menuHelpAbout.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnExitClick( self, event ):
        event.Skip()

    def OnAboutClick( self, event ):
        event.Skip()


