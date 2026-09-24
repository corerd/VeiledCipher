import sys
import os
import wx

# Add the current directory (where steganographer_gui.py is located) to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main_frame import MainFrame

PROJECT_NAME = "Asset Packer"
PROJECT_VERSION = "0.1.0"


class MainApp(wx.App):
    """
    Main application class for the Steganographer tool.

    This class initializes and runs the wxPython application,
    creating and displaying the main frame window.
    """
    def OnInit(self):
        frame = MainFrame(PROJECT_NAME, PROJECT_VERSION)
        frame.Show()
        self.SetTopWindow(frame)
        return True


if __name__ == "__main__":
    app = MainApp(False)
    app.MainLoop()
