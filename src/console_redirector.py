"""
This module provides a helper class to redirect standard output (sys.stdout)
to a wxWidgets UI component, such as a wxRichTextCtrl.

It captures `print()` statements and redirects them to the widget's append
method, allowing command-line style output to be displayed directly in
the graphical user interface.

Note: If the extraction happens in a background thread, 
wxRichTextCtrl.AppendText() must be called on the Main Thread. 
In that case, you would need to use wx.CallAfter(self.widget.AppendText, message) inside the write method.
"""
import wx


class ConsoleRedirector:
    def __init__(self, widget=None):
        self.widget = widget

    def write(self, message):
        """
        Redirects the string message to the widget's output method.
        Uses wx.CallAfter to ensure the UI update is performed on the
        main thread, making it safe for use in multi-threaded environments.
        """
        if self.widget is None:
            # Fallback for no widget
            print(message) 
            return

        if hasattr(self.widget, "AppendText"):
            # If using widget like wxRichTextCtrl, append the text
            wx.CallAfter(self.widget.AppendText, message)
        else:
            # Fallback for other text widgets
            wx.CallAfter(self.widget.SetValue, self.widget.GetValue() + message)
        
    def flush(self):
        pass


if __name__ == "__main__":
    print("This script is intended to be run as a module, not as a standalone program.")
