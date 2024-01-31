# main.py

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import MainWindow
from splash_screen import SplashScreen
from login_screen import LoginScreen
import sys

app = QApplication(sys.argv)

splash = SplashScreen()
splash.show()
# login_screen = LoginScreen()
# login_screen.show()

# If the login is successful, create and show the main window

# Simulate some initialization or loading here
# if login_screen.check_login() == 0:
#     window = MainWindow(app)
#     window.show()

# Set the app icon
app_icon = QIcon("assets/logo.png")
app.setWindowIcon(app_icon)
window = MainWindow(app)
window.show()

splash.finish(window)  # Close the splash screen when the main window is fully loaded


app.exec()