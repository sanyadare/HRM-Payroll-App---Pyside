# splash_screen.py

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSplashScreen, QLabel

class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__(QPixmap("splash_image.png"))  # Replace "splash_image.png" with your image file
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showMessage("Loading...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)
        self.progressBar = QLabel(self)
        self.progressBar.setGeometry(10, self.height() - 30, self.width() - 20, 20)
        self.progressBar.setStyleSheet("QLabel { border: 1px solid white; background-color: white; }")
        self.progressBar.setAlignment(Qt.AlignLeft)
        self.progressBar.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)  # Adjust the interval for smoother animation

    def update_progress(self):
        # Simulate loading progress
        value = self.progressBar.width() * 0.01
        self.progressBar.setFixedWidth(self.progressBar.width() + value)

        if self.progressBar.width() >= self.width() - 20:
            self.timer.stop()
            self.close()
