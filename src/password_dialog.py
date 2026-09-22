import wx

# Generated base class by wxFormBuilder (do not edit gui.py by hand)
from gui import PasswordDialogBase


class PasswordDialog(PasswordDialogBase):
    """
    A dialog box for entering a password for encryption/decryption.
    """
    def __init__(self, parent, title: str, confirmPassword: bool = True) -> None:
        """
        Initializes the password dialog window.

        :param parent: The parent widget of the dialog.
        :param title: The title text of the dialog window.
        :param confirmPassword: Whether to require a confirmation password field.
        """
        PasswordDialogBase.__init__(self, parent)
        self.confirm = confirmPassword
        self.password = ""
        self.SetTitle(title)
        if not self.confirm:
            self.m_confirmPasswordLineSeparator.Hide()
            self.m_lblConfirmPassword.Hide()
            self.m_confirmPasswordText.Hide()
            self.m_showConfirmPasswordCheckbox.Hide()

    def GetPasswordEnteredValue(
            self: "PasswordDialog", 
            selectPlainText: bool,
            maskedText: wx.TextCtrl, 
            plainText: wx.TextCtrl) -> str:
        """
        Retrieves the password value from the appropriate text control
        based on the selected display mode.

        :param selectPlainText: Whether the plain text view is currently selected.
        :param maskedText: The text control used for masking the password input.
        :param plainText: The text control used for displaying the password in plain text.
        :return: The string value of the password entered.
        """
        if selectPlainText:
            return plainText.GetValue()
        return maskedText.GetValue()

    def SetPassword(self, verify: bool) -> None:
        """
        Password setter.

        :param verify: If True, the password will be verified before being saved.
        """
        candidate_password = self.GetPasswordEnteredValue(
            self.m_showPasswordCheckbox.IsChecked(), 
            self.m_passwordText, 
            self.m_passwordTextPlain)
        if verify:
            confirm_password = self.GetPasswordEnteredValue(
                self.m_showConfirmPasswordCheckbox.IsChecked(), 
                self.m_confirmPasswordText, 
                self.m_confirmPasswordTextPlain)
            if confirm_password != candidate_password:
                wx.MessageBox("Passwords do not match.", "Error", wx.OK | wx.ICON_ERROR)
                return
        self.password = candidate_password

        # Close the dialog and return wx.ID_OK to indicate the user clicked the OK button
        self.EndModal(wx.ID_OK)

    def GetPassword(self) -> str:
        """
        Password getter.
        """
        return self.password

    def setVisibility(
            self: "PasswordDialog", 
            show: bool,
            maskedText: wx.TextCtrl, 
            plainText: wx.TextCtrl) -> None:
        """
        Toggles the visibility of the plain text password field.

        :param show: True to show plain text, False to show masked text.
        :param maskedText: The UI widget for masked input.
        :param plainText: The UI widget for unmasked input.
        """
        if show: # Set visibility of the plain text field
            # Capture the current cursor position in the masked text field
            cursor_position = maskedText.GetInsertionPoint()
            # Copy the value from the masked back to the plain text field
            plainText.SetValue(maskedText.GetValue())
            # Restores the cursor position and set the focus to the new visible field
            plainText.SetInsertionPoint(cursor_position)
            plainText.SetFocus()
            # Hide the masked and show the plain text field
            maskedText.Hide()
            plainText.Show()
        else: # Set visibility of the masked text field
            # Capture the current cursor position in the plain text field
            cursor_position = plainText.GetInsertionPoint()
            # Copy the value from the plain back to the masked text field.
            maskedText.SetValue(plainText.GetValue())
            # Restore the cursor position and sets the focus back to the masked field.
            maskedText.SetInsertionPoint(cursor_position)
            maskedText.SetFocus()
            # Hide the plain and show the masked text field
            plainText.Hide()
            maskedText.Show()
        self.Layout() # Update the layout

    def OnShowPassword(self, event):
        """
        # Toggle visibility between a masked password field and a plain text field.
        # These widgets share the same position in the layout.
        """
        self.setVisibility(
            self.m_showPasswordCheckbox.IsChecked(), 
            self.m_passwordText, 
            self.m_passwordTextPlain)

    def OnShowConfirmPassword(self, event):
        """
        # Toggle visibility between a masked confirm password field and a plain text field.
        # These widgets share the same position in the layout.
        """
        self.setVisibility(
            self.m_showConfirmPasswordCheckbox.IsChecked(), 
            self.m_confirmPasswordText, 
            self.m_confirmPasswordTextPlain)

    def OnPasswordEnter(self, event):
        """
        Handles the 'Enter' key event within the password input field.

        Focus on confirmation field if enabled.
        Otherwise, set the password without further verification.
        """
        if self.confirm:
            if self.m_showConfirmPasswordCheckbox.IsChecked():
                self.m_confirmPasswordTextPlain.SetFocus()
            else:
                self.m_confirmPasswordText.SetFocus()
        else:
            self.SetPassword(False)

    def OnConfirmPasswordEnter(self, event):
        """
        Handles the 'Enter' key event within the password confirm input field.

        The password will be verified before being saved.
        """
        self.SetPassword(True)

    def OnBtnOKClick(self, event):
        """
        Handles the click event for the OK button.

        If confirmation is enabled, the password will be verified before being saved.
        """
        self.SetPassword(self.confirm)


