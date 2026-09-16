import wx

from gui import MainFrameBase  # generated base class by wxFormBuilder (do not edit gui.py by hand)

PROJECT_NAME = "Steganographer"
PROJECT_VERSION = "0.1.0"


class MainFrame(MainFrameBase):
    """
    Main application frame for the Steganographer tool.

    This class handles the primary user interface and event handling
    for the steganography application, providing functionality for
    encoding and decoding messages within images.
    """
    def __init__(self, parent=None):
        MainFrameBase.__init__(self, parent)
        self.SetTitle(f"{PROJECT_NAME} {PROJECT_VERSION}")
        self.m_statusBar.SetStatusText("Ready")

    def OnAboutClick( self, event ):
        message = (f"This is a simple GUI for the {PROJECT_NAME} application.\n\n"
                   f"OS: {wx.GetOsDescription()}\n"
                   f"Framework: wxPython {wx.version()}")
        wx.MessageBox(message, f"About {PROJECT_NAME} {PROJECT_VERSION}", wx.OK | wx.ICON_INFORMATION)

    def OnExitClick(self, event):
        self.Close(True)


class MainApp(wx.App):
    """
    Main application class for the Steganographer tool.

    This class initializes and runs the wxPython application,
    creating and displaying the main frame window.
    """
    def OnInit(self):
        frame = MainFrame()
        frame.Show()
        self.SetTopWindow(frame)
        return True


if __name__ == "__main__":
    app = MainApp(False)
    app.MainLoop()
