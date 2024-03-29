# main_window.py
from datetime import datetime
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon, QPixmap, Qt
from PySide6.QtWidgets import QMainWindow, QSizePolicy, QHBoxLayout, QToolBar,QPushButton,QStatusBar,QLabel, QLineEdit, QVBoxLayout, QWidget, QStackedWidget, QSpinBox, QDialog, QComboBox
from pages.dashboard import Dashboard
from pages.admin_actions import AdminActions
from pages.personel_info_mgt import Pim
from pages.salary_setup import SalarySetup
from pages.job_setup import JobSetup
from pages.reports import Reports
from pages.my_account import MyAccount
from stylesheet import DARK_MODE_STYLESHEET,DARK_BLUE_MODE_STYLESHEET, DARK_GREEN_MODE_STYLESHEET,  LIGHT_GREEN_MODE_STYLESHEET, LIGHT_BLUE_MODE_STYLESHEET
from utils import convert_month, months, active_years

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.current_mode = 'light-green'
        self.dialog = QDialog(self)
        self.setStyleSheet(LIGHT_GREEN_MODE_STYLESHEET)
        self.dialog.setStyleSheet(LIGHT_GREEN_MODE_STYLESHEET)
        self.setWindowTitle("Akyerit Payslip HRM")
     
        self.login_page()
        self.show()
        

    def init_ui(self):
        
        
        current_datetime = datetime.now()
        # Extract the current month and year
        current_month = current_datetime.month
        current_year = current_datetime.year
        
        self.month = current_month
        self.year = current_datetime.year
        self.converted_month = convert_month(self.month)
        #Menubar and menus
        self.menu_bar = self.menuBar()
        
        # menu_bar.addAction("Dashboard").setStatusTip("Go To The Dashboard")
        self.menu_bar.triggered.connect(self.change_view)

        admin_menu = self.menu_bar.addMenu("Admin")
        admin_menu.addAction("Dashboard").setStatusTip("Go To The Dashboard")
        admin_menu.addAction("Transactional Actions").setStatusTip("Send Slips To All Staff, Input Bulk Transaction, Add New User")
        admin_menu.addAction("Salary Setup")
        admin_menu.addAction("Job Setup")
        admin_menu.addAction("Switch Month").setStatusTip(f'Choose a Different Month To Work With, Current Month Is {self.converted_month}')
        
        #A bunch of other menu options just for the fun of it
        self.menu_bar.addAction("Personel Info Management")
        self.menu_bar.addAction('Reports')
        settings_menu = self.menu_bar.addMenu("Settings")
        appearance_menu = settings_menu.addMenu("Appearance")
        appearance_menu.addAction('Default Mode', self.switch_to_default_mode)
        appearance_menu.addAction('Dark Mode', self.switch_to_dark_mode)
        appearance_menu.addAction('Light Green Mode', self.switch_to_light_green_mode)
        appearance_menu.addAction('Light Blue Mode', self.switch_to_light_blue_mode)
        appearance_menu.addAction('Dark Green Mode', self.switch_to_dark_green_mode)
        appearance_menu.addAction('Dark Blue Mode', self.switch_to_dark_blue_mode)
        settings_menu.addAction('Edit Account')
        settings_menu.addAction('Logout')
        
        help_menu = self.menu_bar.addMenu("Help")
        help_menu.addAction('About')

        self.menu_bar.addSeparator()
        self.l_date = QAction(f"Date is: {self.converted_month}, {self.year}")
        
        self.menu_bar.addAction(self.l_date)
    
        # Working with status bars
        self.setStatusBar(QStatusBar(self))
        
        # create the pages
        self.dashboard = Dashboard(date=self.converted_month)
        # self.send_slip_page = SendSlipPage()
        self.admin_actions = AdminActions()
        self.personel_info_mgt = Pim(mode=self.current_mode)
        self.my_account = MyAccount()
        self.salary_setup = SalarySetup()
        self.job_setup = JobSetup()
        self.reports = Reports()
        
        
        
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        
        # 
        self.stacked.addWidget(self.dashboard)
        self.stacked.addWidget(self.admin_actions)
        # self.stacked.addWidget(self.send_slip_page)
        self.stacked.addWidget(self.my_account)
        self.stacked.addWidget(self.salary_setup)
        self.stacked.addWidget(self.job_setup)
        self.stacked.addWidget(self.personel_info_mgt)
        self.stacked.addWidget(self.reports)
   
        
        #Working with toolbars
        self.toolbar = QToolBar("My main toolbar")
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        transac_actions = QAction("Transactional Actions", self)
        transac_actions.setStatusTip("Send Slips To All Staff, Input Bulk Transaction, Add New User")
        transac_actions.triggered.connect(self.go_to_admin_actions)
        transac_actions.setCheckable(True)
        self.toolbar.addAction(transac_actions)
        
        self.toolbar.addSeparator()
        salary_setup = QAction("Salary Setup", self)
        salary_setup.setStatusTip("Status message for some action")
        salary_setup.triggered.connect(self.go_to_salary_setup)
        salary_setup.setCheckable(True)
        self.toolbar.addAction(salary_setup)
        
        

        # icon = QIcon("assets/logo.png")
        self.toolbar.addSeparator()
        # job_setup = QPushButton("Some other action")
        job_setup = QAction("Job Setup", self)
        job_setup.setStatusTip("Job setup")
        job_setup.triggered.connect(self.go_to_job_setup)
        job_setup.setCheckable(True)
        self.toolbar.addAction(job_setup)

        self.toolbar.addSeparator()
        # toolbar.addWidget(QPushButton(text="Click here", icon=QIcon("assets/money.png")))


    def set_full_window_size(self):
        self.showMaximized()
        
    def set_default_window_size(self):
        self.resize(400, 400)

    def go_to_dashboard(self):
        self.stacked.setCurrentWidget(self.dashboard)
        
    def go_to_pim(self):
        self.stacked.setCurrentWidget(self.personel_info_mgt)
        
    def go_to_admin_actions(self):
        self.stacked.setCurrentWidget(self.admin_actions)
        
    def go_to_job_setup(self):
        self.stacked.setCurrentWidget(self.job_setup)
        
    def go_to_salary_setup(self):
        self.stacked.setCurrentWidget(self.salary_setup)
    
    def go_to_account_settings(self):
        self.stacked.setCurrentWidget(self.my_account)
    
    def create_month_dialog(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle('Switch Month')
        # self.dialog.setStyleSheet(self.style)
        self.dialog.resize(200, 100)  # Set the size of the dialog box

        # Create widgets
        m_label = QLabel("Select Month:")
        combo_month = QComboBox()
        # combo_month.setPlaceholderText(int(self.month))
        for item in months:
            month = item.get("month")
            if month:
                combo_month.addItem(month)

        # Connect activated signal to a custom slot
        combo_month.activated.connect(self.selected_month_changed)

        self.selected_month = None  # Initialize selected month

        y_label = QLabel("Select Year:")
        new_year = QSpinBox()
        self.year = int(self.year)
        new_year.setRange(2015, 3015)
        new_year.setValue(self.year)
       
       

        button = QPushButton("Submit")

        self.month_error_msg = QLabel("")
        # Create layout
        layout = QVBoxLayout(self.dialog)
        layout.addWidget(m_label)
        layout.addWidget(combo_month)
        layout.addWidget(y_label)
        layout.addWidget(new_year)
      
        layout.addWidget(self.month_error_msg)
        layout.addWidget(button)

        # Connect button clicked signal to a custom slot
        button.clicked.connect(lambda: self.submit_month(year=new_year.text()))

        self.dialog.exec_()

    def selected_month_changed(self, index):
        self.selected_month = index

    def submit_month(self, year:int):
        if self.selected_month is not None:
            month = months[self.selected_month]["value"]
            self.month = month
            self.year = year
            
            # Update the UI with the selected month and year
            formatted_date = convert_month(self.month) + f", {self.year}"
            self.statusBar().showMessage(f"Date set to: {formatted_date}")
            self.l_date.setText(f"Date is: {formatted_date}")
            # self.dashboard.change_date_label(new_text=formatted_date)
            self.dashboard.date = self.month
            
            # print(f"Month submitted: {self.month}, Year submitted: {self.year}")
            self.dialog.close()
        else:
            self.month_error_msg.setText("<p style='color: red;'>Please select a month first</p>")
            print("Please select a month first")


   
    def change_view(self, q):
        if q.text() == 'Transactional Actions':
            self.go_to_admin_actions()
        elif q.text() == 'Switch Month':
            self.create_month_dialog()
        elif q.text() == 'Edit Account':
            self.go_to_account_settings()
        elif q.text() == 'Job Setup':
            self.go_to_job_setup()
        elif q.text() == 'Dashboard':
            self.go_to_dashboard()
        elif q.text() == 'Salary Setup':
            self.go_to_salary_setup()
        elif q.text() == 'Personel Info Management':
            self.go_to_pim()
        elif q.text() == 'Reports':
            self.stacked.setCurrentWidget(self.reports)
        elif q.text() == 'Logout':
            self._log_out()
            
    #
    
    def switch_mode(self):
        if self.current_mode == "light-green":
            self.switch_to_light_green_mode
        elif self.current_mode == "light-blue": 
            self.switch_to_light_blue_mode
        elif self.current_mode == "dark-green": 
            self.switch_to_dark_green_mode
        elif self.current_mode == "dark-blue": 
            self.switch_to_dark_blue_mode
        elif self.current_mode == "dark": 
            self.switch_to_dark_mode
        elif self.current_mode == "default": 
            self.switch_to_default_mode

    def switch_to_light_green_mode(self):
        self.setStyleSheet(LIGHT_GREEN_MODE_STYLESHEET)
        self.dialog.setStyleSheet(LIGHT_GREEN_MODE_STYLESHEET)
        self.current_mode = "light-green"
        self.personel_info_mgt.setMode("light-green")
       
    def switch_to_light_blue_mode(self):
        self.setStyleSheet(LIGHT_BLUE_MODE_STYLESHEET)
        self.dialog.setStyleSheet(LIGHT_BLUE_MODE_STYLESHEET)
        self.current_mode = "light-blue"
        self.personel_info_mgt.setMode("light-blue")

    def switch_to_dark_mode(self):
        self.setStyleSheet(DARK_MODE_STYLESHEET)
        self.dialog.setStyleSheet(DARK_MODE_STYLESHEET)
        self.current_mode = "dark"
        self.personel_info_mgt.setMode("dark")
        
    def switch_to_dark_green_mode(self):
        self.setStyleSheet(DARK_GREEN_MODE_STYLESHEET)
        self.dialog.setStyleSheet(DARK_GREEN_MODE_STYLESHEET)
        self.current_mode = "dark-green"
        self.personel_info_mgt.setMode("dark-green")
        
    def switch_to_dark_blue_mode(self):
        self.setStyleSheet(DARK_BLUE_MODE_STYLESHEET)
        self.dialog.setStyleSheet(DARK_BLUE_MODE_STYLESHEET)
        self.current_mode = "dark-blue"
        self.personel_info_mgt.setMode("dark-blue")
     
    def switch_to_default_mode(self):
        self.setStyleSheet('default')
        self.current_mode = "default"
        self.current_mode = "default"
        self.personel_info_mgt.setMode("default")
    
    def set_default_window_size(self):
        # Set the default window size to 1200x600
        self.resize(QSize(1200, 600))
    
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app",3000)
        
    
    def login_page(self):
        self.switch_mode()
        self.resize(800, 400)
        login_layout = QHBoxLayout()
        layout = QVBoxLayout()

        self.trial_count = 5
        
        # Username input
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.textChanged.connect(self.check_text)
        # self.username_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Password input
        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.textChanged.connect(self.check_text)
        # self.password_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.password_input.setEchoMode(QLineEdit.Password)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self._check_login)
        self.error_message = QLabel("")

        # layout.addWidget(QLabel("<b style='font-size: 20px'>Login</b>"))
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.error_message)
        layout.addWidget(QWidget(), 3)

        r_layout = QVBoxLayout()
        r_layout.addWidget(QWidget(), 1)
        r_layout.addLayout(layout, 4)
        # r_layout.addWidget(QWidget(), 1)
        
        l_layout = QVBoxLayout()
        logo = QPixmap("assets/logo.png")
        logo = logo.scaled(50, 50)
        landing_logo = QLabel()
        landing_logo.setPixmap(logo)
        landing_logo.setAlignment(Qt.AlignCenter)
        landing_copy = QLabel("""<p style="font-size: 14px;" align='center'; >Welcome to Akyerite Payslip HRM Desktop Application, <br>
                              where powerful management tools meet seamless efficiency. <br> 
                              Simplify your business operations with our intuitive <br> database management system, 
                              enabling easy <br> organization and access to your company's data. <br>
                              From payroll processing to employee management, <br> our comprehensive features streamline your workflow, <br> saving you time and hassle.</p>""")
        l_layout.addWidget(QWidget(), 5)
        l_layout.addWidget(landing_logo)
        l_layout.addWidget(QLabel("<p style='font-size: 30px; font-weight: bold;' align='center';>PAYSLIP HRM</p>"), 1)
        l_layout.addWidget(landing_copy, 1)
        l_layout.addWidget(QLabel("<p style='font-style: italic; color: gray;' align='center'>All Rights Reserved By Akyerite Solutions</p>"))
        l_layout.addWidget(QWidget(), 5)
        
        
        login_layout.addLayout(l_layout, 1)
        login_layout.addLayout(r_layout, 1)
        self.login_p = QWidget()
        self.login_p.setLayout(login_layout)
        self.setCentralWidget(self.login_p)
        
    def check_text(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if username and password:
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def _check_login(self):
        # Simple login check (replace with your authentication logic)
        
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            self.login_p.close()
            self.trial_count = 5
            self.set_full_window_size()
            self.init_ui()
        
        elif self.trial_count == 1:
            self.close()
        else:
            self.trial_count = self.trial_count - 1
            self.error_message.setText(f"<p style='color: red'>InValid Credentials, You have {self.trial_count} attempts left<p>")

    
    def _log_out(self):
        self.stacked.close()
        self.menu_bar.close()
        self.toolbar.close()
        self.resize(800, 400)
        self.login_page()
      