from PySide6.QtWidgets import QTabWidget, QWidget, QLabel, QLineEdit, QVBoxLayout,QHBoxLayout, QPushButton, QBoxLayout

class MyAccount(QTabWidget):
    def __init__(self):
        super().__init__()

        # Create three tabs
        self.my_account = QWidget()
        self.new_user = QWidget()

        # Add tabs to the SalarySetup widget
        self.addTab(self.my_account, "Edit Account")
        self.addTab(self.new_user, "Create New User")

        # Setup tab content
        self.my_account_tab()
        self.new_user_tab()
  
        

    def my_account_tab(self):
        layout = QHBoxLayout(self.my_account)
        main_layout = QVBoxLayout()
        
        layout.addWidget(QWidget(), 1)
        layout.addLayout(main_layout, 2)
        edit_acct_layout = QVBoxLayout()
        edit_acct_layout.addWidget(QLabel("<b style='font-size:20px'>Account Details</b>"))
        
         # first name
        l_first_name = QLabel("<i>First Name:</i>")
        new_first_name = QLineEdit()
        edit_acct_layout.addWidget(l_first_name)
        edit_acct_layout.addWidget(new_first_name)
        
         # last name
        l_last_name = QLabel("<i>Last Name:</i>")
        new_last_name = QLineEdit()
        edit_acct_layout.addWidget(l_last_name)
        edit_acct_layout.addWidget(new_last_name)
        
         # Address
        l_address_name = QLabel("<i>Address:</i>")
        new_address_name = QLineEdit()
        edit_acct_layout.addWidget(l_address_name)
        edit_acct_layout.addWidget(new_address_name)
        
        change_details_button = QPushButton("Update Details")
        edit_acct_layout.addWidget(change_details_button)
        edit_acct_layout.addWidget(QWidget(), 2)
        
        # Password Edit
        edit_password_layout = QVBoxLayout()
        edit_password_layout.addWidget(QLabel("<b style='font-size:20px'>Change Password</b>"))
        
         # Old Password
        l_old_password = QLabel("<i>Old Password:</i>")
        old_password = QLineEdit()
        edit_password_layout.addWidget(l_old_password)
        edit_password_layout.addWidget(old_password)
        
         # new pass word
        l_new_password = QLabel("<i>New Password:</i>")
        new_password = QLineEdit()
        edit_password_layout.addWidget(l_new_password)
        edit_password_layout.addWidget(new_password)
        
         # confirm new pass word
        l_c_new_password = QLabel("<i>Confirm New Password:</i>")
        c_new_password = QLineEdit()
        edit_password_layout.addWidget(l_c_new_password)
        edit_password_layout.addWidget(c_new_password)
        
        change_password_button = QPushButton("Change Password")
        edit_password_layout.addWidget(change_password_button)
        edit_password_layout.addWidget(QWidget(), 2)
        
        main_layout.addLayout(edit_acct_layout, 1)
        main_layout.addLayout(edit_password_layout, 1)
        layout.addWidget(QWidget(), 1)
        
        

    def new_user_tab(self):
        main_layout = QHBoxLayout(self.new_user)
        
        form_layout = QVBoxLayout()
        main_layout.addWidget(QWidget(), 1)
        
        # form
        form_layout.addWidget(QLabel("<b style='font-size:20px'>New User Form</b>"))
        
        # first name
        l_first_name = QLabel("<i>First Name:</i>")
        first_name = QLineEdit()
        form_layout.addWidget(l_first_name)
        form_layout.addWidget(first_name)
        
        # last name
        l_last_name = QLabel("<i>Last Name:</i>")
        last_name = QLineEdit()
        form_layout.addWidget(l_last_name)
        form_layout.addWidget(last_name)
        
        # user name
        l_user_name = QLabel("<i>User Name:</i>")
        user_name = QLineEdit()
        form_layout.addWidget(l_user_name)
        form_layout.addWidget(user_name)
        
        # Password
        l_password = QLabel("<i>Password:</i>")
        password = QLineEdit()
        form_layout.addWidget(l_password)
        form_layout.addWidget(password)
         
         # Confirm Password
        l_c_password = QLabel("<i>Confirm Password:</i>")
        c_password = QLineEdit()
        form_layout.addWidget(l_c_password)
        form_layout.addWidget(c_password)
        
         # Address
        l_address = QLabel("<i>Address:</i>")
        address = QLineEdit()
        form_layout.addWidget(l_address)
        form_layout.addWidget(address)
        
        submit_button = QPushButton("Create User")
        form_layout.addWidget(submit_button)
        
        form_layout.addWidget(QWidget(), 2)
        main_layout.addLayout(form_layout, 2)
        main_layout.addWidget(QWidget(),1)
        
       
        
        # password
        # confirm/password
        # address


