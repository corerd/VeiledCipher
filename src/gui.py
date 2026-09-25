# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.stc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"MainFrame"), pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

        mainVerticalBoxSizer = wx.BoxSizer( wx.VERTICAL )

        mainHorizontalBoxSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panelEncode = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panelEncode, wx.ID_ANY, _(u"Path to the carrier image file (PNG/JPG)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

        bSizerCarrier = wx.BoxSizer( wx.HORIZONTAL )

        self.m_carrierFilePath = wx.TextCtrl( self.m_panelEncode, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_carrierFilePath.SetMinSize( wx.Size( 500,-1 ) )

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
        self.m_secretFilePath.SetMinSize( wx.Size( 500,-1 ) )

        bSizerSecret.Add( self.m_secretFilePath, 0, wx.ALL, 5 )

        self.btnOpenSecretFile = wx.Button( self.m_panelEncode, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerSecret.Add( self.btnOpenSecretFile, 0, wx.ALL, 5 )


        bSizer3.Add( bSizerSecret, 0, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self.m_panelEncode, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panelEncode, wx.ID_ANY, _(u"Path to save the resulting stego-image"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

        bSizerEncodeResult = wx.BoxSizer( wx.HORIZONTAL )

        self.m_resultEncodedFilePath = wx.TextCtrl( self.m_panelEncode, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_resultEncodedFilePath.SetMinSize( wx.Size( 500,-1 ) )

        bSizerEncodeResult.Add( self.m_resultEncodedFilePath, 0, wx.ALL, 5 )

        self.btnSaveEncodedFile = wx.Button( self.m_panelEncode, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerEncodeResult.Add( self.btnSaveEncodedFile, 0, wx.ALL, 5 )


        bSizer3.Add( bSizerEncodeResult, 1, wx.EXPAND, 5 )


        self.m_panelEncode.SetSizer( bSizer3 )
        self.m_panelEncode.Layout()
        bSizer3.Fit( self.m_panelEncode )
        self.m_notebook.AddPage( self.m_panelEncode, _(u"Encode"), True )
        self.m_panelDecode = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer31 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText11 = wx.StaticText( self.m_panelDecode, wx.ID_ANY, _(u"Path to the stego-image file"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer31.Add( self.m_staticText11, 0, wx.ALL, 5 )

        bSizerStegoImage = wx.BoxSizer( wx.HORIZONTAL )

        self.m_stegoImagePath = wx.TextCtrl( self.m_panelDecode, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_stegoImagePath.SetMinSize( wx.Size( 500,-1 ) )

        bSizerStegoImage.Add( self.m_stegoImagePath, 0, wx.ALL, 5 )

        self.btnSelectStegoImage = wx.Button( self.m_panelDecode, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerStegoImage.Add( self.btnSelectStegoImage, 0, wx.ALL, 5 )


        bSizer31.Add( bSizerStegoImage, 0, wx.EXPAND, 5 )

        self.m_staticline21 = wx.StaticLine( self.m_panelDecode, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer31.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText31 = wx.StaticText( self.m_panelDecode, wx.ID_ANY, _(u"Path to save the recovered secret file"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        bSizer31.Add( self.m_staticText31, 0, wx.ALL, 5 )

        bSizerDecodeResult = wx.BoxSizer( wx.HORIZONTAL )

        self.m_resultDecodedFilePath = wx.TextCtrl( self.m_panelDecode, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_resultDecodedFilePath.SetMinSize( wx.Size( 500,-1 ) )

        bSizerDecodeResult.Add( self.m_resultDecodedFilePath, 0, wx.ALL, 5 )

        self.btnSaveDecodedFile = wx.Button( self.m_panelDecode, wx.ID_ANY, _(u"Browse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDecodeResult.Add( self.btnSaveDecodedFile, 0, wx.ALL, 5 )


        bSizer31.Add( bSizerDecodeResult, 1, wx.EXPAND, 5 )


        self.m_panelDecode.SetSizer( bSizer31 )
        self.m_panelDecode.Layout()
        bSizer31.Fit( self.m_panelDecode )
        self.m_notebook.AddPage( self.m_panelDecode, _(u"Decode"), False )

        mainHorizontalBoxSizer.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.btnClearFields = wx.Button( self, wx.ID_ANY, _(u"Clear\nFields"), wx.DefaultPosition, wx.Size( -1,40 ), 0 )
        bSizer6.Add( self.btnClearFields, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btnCompute = wx.Button( self, wx.ID_ANY, _(u"Compute"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btnCompute, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        mainHorizontalBoxSizer.Add( bSizer6, 1, wx.EXPAND, 5 )


        mainVerticalBoxSizer.Add( mainHorizontalBoxSizer, 1, wx.EXPAND, 5 )

        self.m_console = wx.stc.StyledTextCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_console.SetUseTabs ( True )
        self.m_console.SetTabWidth ( 4 )
        self.m_console.SetIndent ( 4 )
        self.m_console.SetTabIndents( True )
        self.m_console.SetBackSpaceUnIndents( True )
        self.m_console.SetViewEOL( False )
        self.m_console.SetViewWhiteSpace( False )
        self.m_console.SetMarginWidth( 2, 0 )
        self.m_console.SetIndentationGuides( True )
        self.m_console.SetReadOnly( False )
        self.m_console.SetMarginType ( 1, wx.stc.STC_MARGIN_SYMBOL )
        self.m_console.SetMarginMask ( 1, wx.stc.STC_MASK_FOLDERS )
        self.m_console.SetMarginWidth ( 1, 16)
        self.m_console.SetMarginSensitive( 1, True )
        self.m_console.SetProperty ( "fold", "1" )
        self.m_console.SetFoldFlags ( wx.stc.STC_FOLDFLAG_LINEBEFORE_CONTRACTED | wx.stc.STC_FOLDFLAG_LINEAFTER_CONTRACTED )
        self.m_console.SetMarginWidth ( 0, 0 )
        self.m_console.MarkerDefine( wx.stc.STC_MARKNUM_FOLDER, wx.stc.STC_MARK_BOXPLUS )
        self.m_console.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDER, wx.BLACK)
        self.m_console.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDER, wx.WHITE)
        self.m_console.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.stc.STC_MARK_BOXMINUS )
        self.m_console.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.BLACK )
        self.m_console.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.WHITE )
        self.m_console.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERSUB, wx.stc.STC_MARK_EMPTY )
        self.m_console.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEREND, wx.stc.STC_MARK_BOXPLUS )
        self.m_console.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEREND, wx.BLACK )
        self.m_console.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEREND, wx.WHITE )
        self.m_console.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.stc.STC_MARK_BOXMINUS )
        self.m_console.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.BLACK)
        self.m_console.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.WHITE)
        self.m_console.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERMIDTAIL, wx.stc.STC_MARK_EMPTY )
        self.m_console.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERTAIL, wx.stc.STC_MARK_EMPTY )
        self.m_console.SetSelBackground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_console.SetSelForeground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        mainVerticalBoxSizer.Add( self.m_console, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( mainVerticalBoxSizer )
        self.Layout()
        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.OnExitClick, id = self.m_menuFileExit.GetId() )
        self.Bind( wx.EVT_MENU, self.OnAboutClick, id = self.m_menuHelpAbout.GetId() )
        self.m_notebook.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onTabChanged )
        self.btnOpenCarrierFile.Bind( wx.EVT_BUTTON, self.onSelectCarrierFile )
        self.btnOpenSecretFile.Bind( wx.EVT_BUTTON, self.onSelectSecretFile )
        self.btnSaveEncodedFile.Bind( wx.EVT_BUTTON, self.onSelectEncodedFile )
        self.btnSelectStegoImage.Bind( wx.EVT_BUTTON, self.onSelectStegoImage )
        self.btnSaveDecodedFile.Bind( wx.EVT_BUTTON, self.onSelectDecodedFile )
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

    def onSelectStegoImage( self, event ):
        event.Skip()

    def onSelectDecodedFile( self, event ):
        event.Skip()

    def onClearFields( self, event ):
        event.Skip()

    def onCompute( self, event ):
        event.Skip()


###########################################################################
## Class PasswordDialogBase
###########################################################################

class PasswordDialogBase ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Password"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetToolTip( _(u"Enter password") )

        MainSizer  = wx.BoxSizer( wx.VERTICAL )

        self.m_lblPassword = wx.StaticText( self, wx.ID_ANY, _(u"Password"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lblPassword.Wrap( -1 )

        MainSizer .Add( self.m_lblPassword, 0, wx.ALL, 5 )

        passwordSizer  = wx.BoxSizer( wx.HORIZONTAL )

        self.m_passwordText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
        self.m_passwordText.SetToolTip( _(u"Enter password") )
        self.m_passwordText.SetMinSize( wx.Size( 300,-1 ) )

        passwordSizer .Add( self.m_passwordText, 0, wx.ALL, 5 )

        self.m_passwordTextPlain = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.m_passwordTextPlain.Hide()
        self.m_passwordTextPlain.SetToolTip( _(u"Enter password") )
        self.m_passwordTextPlain.SetMinSize( wx.Size( 300,-1 ) )

        passwordSizer .Add( self.m_passwordTextPlain, 0, wx.ALL, 5 )


        passwordSizer .Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_showPasswordCheckbox  = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        passwordSizer .Add( self.m_showPasswordCheckbox , 0, wx.ALL, 5 )


        MainSizer .Add( passwordSizer , 1, wx.EXPAND, 5 )

        self.m_confirmPasswordLineSeparator = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        MainSizer .Add( self.m_confirmPasswordLineSeparator, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_lblConfirmPassword = wx.StaticText( self, wx.ID_ANY, _(u"Confirm"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_lblConfirmPassword.Wrap( -1 )

        MainSizer .Add( self.m_lblConfirmPassword, 0, wx.ALL, 5 )

        confirmPasswordSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_confirmPasswordText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
        self.m_confirmPasswordText.SetToolTip( _(u"Confirm password") )
        self.m_confirmPasswordText.SetMinSize( wx.Size( 300,-1 ) )

        confirmPasswordSizer.Add( self.m_confirmPasswordText, 0, wx.ALL, 5 )

        self.m_confirmPasswordTextPlain = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.m_confirmPasswordTextPlain.Hide()
        self.m_confirmPasswordTextPlain.SetToolTip( _(u"Confirm password") )
        self.m_confirmPasswordTextPlain.SetMinSize( wx.Size( 300,-1 ) )

        confirmPasswordSizer.Add( self.m_confirmPasswordTextPlain, 0, wx.ALL, 5 )


        confirmPasswordSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_showConfirmPasswordCheckbox = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        confirmPasswordSizer.Add( self.m_showConfirmPasswordCheckbox, 0, wx.ALL, 5 )


        MainSizer .Add( confirmPasswordSizer, 1, wx.EXPAND, 5 )

        self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        MainSizer .Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

        buttonsSizer  = wx.BoxSizer( wx.HORIZONTAL )

        self.btnOK  = wx.Button( self, wx.ID_OK, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
        buttonsSizer .Add( self.btnOK , 0, wx.ALL, 5 )

        self.btnCancel  = wx.Button( self, wx.ID_CANCEL, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        buttonsSizer .Add( self.btnCancel , 0, wx.ALL, 5 )


        MainSizer .Add( buttonsSizer , 1, wx.ALIGN_CENTER, 5 )


        self.SetSizer( MainSizer  )
        self.Layout()
        MainSizer .Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_passwordText.Bind( wx.EVT_TEXT_ENTER, self.OnPasswordEnter )
        self.m_passwordTextPlain.Bind( wx.EVT_TEXT_ENTER, self.OnPasswordEnter )
        self.m_showPasswordCheckbox .Bind( wx.EVT_CHECKBOX, self.OnShowPassword )
        self.m_confirmPasswordText.Bind( wx.EVT_TEXT_ENTER, self.OnConfirmPasswordEnter )
        self.m_confirmPasswordTextPlain.Bind( wx.EVT_TEXT_ENTER, self.OnConfirmPasswordEnter )
        self.m_showConfirmPasswordCheckbox.Bind( wx.EVT_CHECKBOX, self.OnShowConfirmPassword )
        self.btnOK .Bind( wx.EVT_BUTTON, self.OnBtnOKClick )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnPasswordEnter( self, event ):
        event.Skip()


    def OnShowPassword( self, event ):
        event.Skip()

    def OnConfirmPasswordEnter( self, event ):
        event.Skip()


    def OnShowConfirmPassword( self, event ):
        event.Skip()

    def OnBtnOKClick( self, event ):
        event.Skip()


