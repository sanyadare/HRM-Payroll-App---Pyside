# main.py

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import MainWindow
from splash_screen import SplashScreen
import sys

app = QApplication(sys.argv)

splash = SplashScreen()
splash.show()

# Set the app icon
app_icon = QIcon("assets/logo.png")
app.setWindowIcon(app_icon)

# Set the default font for the app
font = app.font()
font.setFamily("Helvetica")
font.setPointSize(10)
app.setFont(font)
 
window = MainWindow(app)
window.show()

splash.finish(window)  # Close the splash screen when the main window is fully loaded


app.exec()