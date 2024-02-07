from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Username input
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        # Password input
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)



    def check_login(self):
        # Simple login check (replace with your authentication logic)
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            print("Login successful!")
            # self.accept() # Close the login screen
            # self.accept()
            self.close()
            return True
        
        else:
            print("Invalid credentials")

    def accept(self):
        self.close()