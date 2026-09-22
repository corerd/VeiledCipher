import sys
import os
import wx

# Add the current directory (where steganographer_gui.py is located) to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from password_dialog import PasswordDialog

# Generated base class by wxFormBuilder (do not edit gui.py by hand)
from gui import MainFrameBase


PROJECT_NAME = "Steganographer"
PROJECT_VERSION = "0.1.0"

# --- NOTEBOOK TABS
NOTEBOOK_TAB_ENCODER = 0
NOTEBOOK_TAB_DECODER = 1
 

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
        self.setComputeButton()
        self.m_statusBar.SetStatusText("Ready")

    def setComputeButton(self: "MainFrame") -> None:
        """
        Sets the label of the compute button based on the current notebook tab.
        """
        currentPanel = self.m_notebook.GetSelection()
        if currentPanel == NOTEBOOK_TAB_ENCODER:
            self.btnCompute.SetLabel("Encode")
        elif currentPanel == NOTEBOOK_TAB_DECODER:
            self.btnCompute.SetLabel("Decode")

    def selectFileDialog(
            self: "MainFrame", 
            fileDialogMessage: str, 
            textControl: wx.TextCtrl, 
            statusBar: wx.StatusBar, 
            fdWildcard: str = wx.FileSelectorDefaultWildcardStr, 
            fdStyle: int = wx.FD_DEFAULT_STYLE) -> str | None:
        """
        Opens a generic file dialog to select a file and updates the given text control and status bar.

        Args:
            fileDialogMessage: A string indicating the purpose of the file selection dialog.
            textControl: The text control to update with the selected file path.
            statusBar: The status bar to display the selected file path.
            fdWildcard: The wildcard string for file selection. Defaults to the default wildcard string.
            fdStyle: The style of the file dialog. Defaults to the default style.

        Returns:
            The full path of the selected file, or None if no file was selected.
        """
        dialog = wx.FileDialog(
            self, 
            message=fileDialogMessage,
            wildcard=fdWildcard,
            style=fdStyle)
        dialog.SetDirectory(os.path.expanduser("~"))
        if dialog.ShowModal() == wx.ID_OK:
            selected_file_path = dialog.GetPath()
            textControl.SetValue(selected_file_path)
            statusBar.SetStatusText(f"Selected file: {dialog.GetFilename()}")
            return selected_file_path
        else:
            return None

    def onSelectCarrierFile( self, event ):
        """
        Event handler for selecting a carrier image file
        """
        # Open a file dialog to select an existing image file
        self.selectFileDialog(
            "Choose the carrier image file", 
            self.m_carrierFilePath, 
            self.m_statusBar, 
            fdWildcard="Image files (*.png, *.jpg)|*.png;*.jpg",
            fdStyle=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    def onSelectSecretFile( self, event ):
        """
        Event handler for selecting a secret file
        """
        # Open a file dialog to select an existing secret file
        self.selectFileDialog(
            "Choose the secret file to hide", 
            self.m_secretFilePath, 
            self.m_statusBar,
            fdStyle=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    def onSelectEncodedFile( self, event ):
        """
        Event handler for selecting the output path after encoding
        """
        # Open a file dialog to select the destination path for the stego-image
        # with a safety check for existing files.
        self.selectFileDialog(
            "Choose the file path to save the resulting stego-image", 
            self.m_resultEncodedFilePath, 
            self.m_statusBar,
            fdStyle=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

    def OnAboutClick( self, event ):
        """
        Event handler for About menu item is clicked.
        Shows information about the application, including OS version and framework.
        """
        # Implementation goes here
        message = (f"This is a simple GUI for the {PROJECT_NAME} application.\n\n"
                   f"OS: {wx.GetOsDescription()}\n"
                   f"Framework: wxPython {wx.version()}")
        wx.MessageBox(message, f"About {PROJECT_NAME} {PROJECT_VERSION}", wx.OK | wx.ICON_INFORMATION)

    def onTabChanged( self, event ):
        self.setComputeButton()

    def OnExitClick(self, event):
        self.Close(True)

    def onCompute( self, event ):
        dialog = PasswordDialog(self, "Create Password for Encode", confirmPassword=True)
        if dialog.ShowModal() == wx.ID_OK:
            password = dialog.GetPassword()
            print(f"Password: >{password}<")



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
