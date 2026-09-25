import sys
import wx

from password_dialog import PasswordDialog
from console_redirector import ConsoleRedirector

from asset_packer import asset_pack, asset_unpack

# Generated base class by wxFormBuilder (do not edit gui.py by hand)
from gui import MainFrameBase

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
    def __init__(self, app_name: str, app_version: str, parent=None):
        MainFrameBase.__init__(self, parent)
        self.app_name = app_name
        self.app_version = app_version
        self.SetTitle(f"{self.app_name} {self.app_version}")
        self.m_notebook.SetSelection(NOTEBOOK_TAB_ENCODER)
        self.setComputeButton()
        self.m_statusBar.SetStatusText("Ready")

        # Set up console redirection
        sys.stdout = ConsoleRedirector(self.m_console)

        # Optional: Reset the console output
        # sys.stdout = sys.__stdout__

    def setComputeButton(self: "MainFrame") -> None:
        """
        Sets the label of the compute button based on the current notebook tab.
        """
        currentPanel = self.m_notebook.GetSelection()
        if currentPanel == NOTEBOOK_TAB_ENCODER:
            self.btnCompute.SetLabel("Encode")
        elif currentPanel == NOTEBOOK_TAB_DECODER:
            self.btnCompute.SetLabel("Decode")

    def onEncode(self):
        """
        Event handler for the "Encode" button
        """
        dialog = PasswordDialog(self, "Create Password for Encode", confirmPassword=True)
        if dialog.ShowModal() != wx.ID_OK:
            return
        password = dialog.GetPassword()
        carrierFilePath = self.m_carrierFilePath.GetValue()
        secretFilePath = self.m_secretFilePath.GetValue()
        encodedFilePath = self.m_resultEncodedFilePath.GetValue()
        asset_pack(carrierFilePath, secretFilePath, password, encodedFilePath)

    def onDecode(self):
        """
        Event handler for the "Decode" button
        """
        dialog = PasswordDialog(self, "Password for Decode", confirmPassword=False)
        if dialog.ShowModal() != wx.ID_OK:
            return
        password = dialog.GetPassword()
        stegoImagePath = self.m_stegoImagePath.GetValue()
        recoveredSecretFilePath = self.m_resultDecodedFilePath.GetValue()
        asset_unpack(stegoImagePath, password, recoveredSecretFilePath)

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

    def onSelectStegoImage( self, event ):
        """
        Event handler for selecting a stego image file
        """
        # Open a file dialog to select an existing stegoo image file
        self.selectFileDialog(
            "Choose the stego-image file", 
            self.m_stegoImagePath, 
            self.m_statusBar, 
            fdWildcard="Image files (*.png, *.jpg)|*.png;*.jpg",
            fdStyle=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    def onSelectDecodedFile( self, event ):
        """
        Event handler for selecting the output path after decoding
        """
        # Open a file dialog to select the output path for the extracted file,
        # safety checking for existing files.
        self.selectFileDialog(
            "Choose the output path for the extracted file", 
            self.m_resultDecodedFilePath, 
            self.m_statusBar,
            fdStyle=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

    def OnAboutClick( self, event ):
        """
        Event handler for About menu item is clicked.
        Shows information about the application, including OS version and framework.
        """
        # Implementation goes here
        message = (f"This is a simple GUI for the {self.app_name} application.\n\n"
                   f"OS: {wx.GetOsDescription()}\n"
                   f"Framework: wxPython {wx.version()}")
        wx.MessageBox(message, f"About {self.app_name} {self.app_version}", wx.OK | wx.ICON_INFORMATION)

    def onTabChanged( self, event ):
        self.setComputeButton()

    def OnExitClick(self, event):
        self.Close(True)

    def onCompute( self, event ):
        if self.m_notebook.GetSelection() == NOTEBOOK_TAB_ENCODER:
            self.onEncode()
        else:
            self.onDecode()


if __name__ == "__main__":
    print("This script is intended to be run as a module, not as a standalone program.")
