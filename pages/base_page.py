
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class BasePage(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel(self.title, self)
        layout.addWidget(label)