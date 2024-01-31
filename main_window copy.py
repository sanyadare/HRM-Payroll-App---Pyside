# main_window.py
from datetime import datetime
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow,QToolBar,QPushButton,QStatusBar,QLabel, QVBoxLayout, QWidget, QStackedWidget, QLineEdit, QDialog, QComboBox
# from pages_ import NewUserPage, SendSlipPage, SwitchMonthPage, InputBulkTransactionPage
# from pages.salary_setup.allowance_setup import AllowanceSetup
from pages.dashboard import Dashboard
from pages.admin_actions import AdminActions
from pages.personel_info_mgt import Pim
from pages.salary_setup import SalarySetup
from pages.job_setup import JobSetup
from pages.reports import Reports
from stylesheet import DARK_MODE_STYLESHEET, LIGHT_MODE_STYLESHEET
from utils import convert_month, months, active_years

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.current_mode = 'light'
        self.setWindowTitle("Akyerit Payslip HRM")
        self.set_default_window_size()
        
        self.update()
        self.init_ui()
        self.show()
        

    def init_ui(self):
        current_datetime = datetime.now()
        # Extract the current month and year
        current_month = current_datetime.month
        current_year = current_datetime.year
        
        self.month = current_month
        self.year = current_datetime.year
        # self.formatted_date = current_datetime.strftime("%B %Y")
        self.converted_month = convert_month(self.month)
        #Menubar and menus
        menu_bar = self.menuBar()
        
        # menu_bar.addAction("Dashboard").setStatusTip("Go To The Dashboard")
        menu_bar.triggered.connect(self.change_view)
        
        # quit_action = file_menu.addAction("Quit")
        # quit_action.triggered.connect(self.quit_app)

        admin_menu = menu_bar.addMenu("Admin")
        admin_menu.addAction("Dashboard").setStatusTip("Go To The Dashboard")
        admin_menu.addAction("Transactional Actions").setStatusTip("Send Slips To All Staff, Input Bulk Transaction, Add New User")
        admin_menu.addAction("Salary Setup")
        admin_menu.addAction("Job Setup")
        admin_menu.addAction("Switch Month").setStatusTip(f'Choose a Different Month To Work With, Current Month Is {self.converted_month}')
        # admin_menu.triggered.connect(self.change_view)
        
        # salary_setup = admin_menu.addMenu('Salary Setup')
        # salary_setup.addAction('Allowance Setup')
        # salary_setup.addAction('Deduction Setup')
        # salary_setup.addAction('Salary Grade')
        # salary_setup.triggered.connect(self.change_view)
        
        # job_setup = admin_menu.addMenu('Job Setup')
        # job_setup.addAction('Title Setup')
        # job_setup.addAction('Status Setup')
        # job_setup.addAction('Description Grade')
        # job_setup.addAction('Job Category')
        # job_setup.addAction('Bank Setup')
        # job_setup.addAction('State Setup')
        # job_setup.addAction('College Setup')
        
        #A bunch of other menu options just for the fun of it
        menu_bar.addAction("Personel Info Management")
        # pim_menu = menu_bar.addMenu("Personel Info Management")
        # pim_menu.addAction('Create New Staff')
        # pim_menu.addAction('View All Staff')
        
        menu_bar.addAction('Reports')
        # report_menu = menu_bar.addMenu("Report")
        # report_menu.addAction('Report 1')
        # report_menu.addAction('Report 2')
        # report_menu.addAction('Report 3')
        # report_menu.addAction('Report 4')
        # report_menu.addAction('Report 5')
        
        settings_menu = menu_bar.addMenu("Settings")
        appearance_menu = settings_menu.addMenu("Appearance")
        appearance_menu.addAction('Default Mode', self.switch_to_default_mode)
        appearance_menu.addAction('Light Mode', self.switch_to_light_mode)
        appearance_menu.addAction('Dark Mode', self.switch_to_dark_mode)
        settings_menu.addAction('Add New User')
        settings_menu.addAction('Logout')
        
        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction('About')

        menu_bar.addSeparator()
        menu_bar.addAction(f'Date is: {self.converted_month}, {self.year}')
        # Working with status bars
        self.setStatusBar(QStatusBar(self))

        # button1 = QPushButton("BUTTON1")
        # button1.clicked.connect(self.button1_clicked)
        # self.setCentralWidget(button1)
        
        # create the pages
        self.dashboard = Dashboard(username=self.converted_month)
        # self.send_slip_page = SendSlipPage()
        self.admin_actions = AdminActions()
        self.personel_info_mgt = Pim()
        # self.allowance_setup = AllowanceSetup()
        self.salary_setup = SalarySetup()
        self.job_setup = JobSetup()
        self.reports = Reports()
        
        
        
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        
        # 
        self.stacked.addWidget(self.dashboard)
        self.stacked.addWidget(self.admin_actions)
        # self.stacked.addWidget(self.send_slip_page)
        # self.stacked.addWidget(self.allowance_setup)
        self.stacked.addWidget(self.salary_setup)
        self.stacked.addWidget(self.job_setup)
        self.stacked.addWidget(self.personel_info_mgt)
        self.stacked.addWidget(self.reports)
   
        
        #Working with toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        salary_setup = QAction("Transactional Actions", self)
        salary_setup.setStatusTip("Send Slips To All Staff, Input Bulk Transaction, Add New User")
        salary_setup.triggered.connect(self.go_to_admin_actions)
        toolbar.addAction(salary_setup)
        
        salary_setup = QAction("Salary Setup", self)
        salary_setup.setStatusTip("Status message for some action")
        salary_setup.triggered.connect(self.go_to_salary_setup)
        toolbar.addAction(salary_setup)
        
        # l_month = QLabel(self.converted_month, self)
        # toolbar.addLa

        # icon = QIcon("assets/logo.png")
        toolbar.addSeparator()
        # job_setup = QPushButton("Some other action")
        job_setup = QAction("Job Setup", self)
        # job_setup.setStatusTip("Status message for some other action")
        job_setup.triggered.connect(self.go_to_job_setup)
        #action2.setCheckable(True)
        toolbar.addAction(job_setup)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))


    def set_default_window_size(self):
        self.resize(800, 600)

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
    
 
    def create_dialog(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle('Switch Month')
        self.dialog.resize(200, 100)  # Set the size of the dialog box
        
        # Create widgets
        m_label = QLabel("Select Month:")
        combo_month = QComboBox()
        for item in months:
            month = item.get("month")
            if month:
                combo_month.addItem(month)
                
        # Connect activated signal to a custom slot
        combo_month.activated.connect(self.selected_month_changed)
        
        self.selected_month = None  # Initialize selected month
        
        y_label = QLabel("Select Year:")
        year_combo = QComboBox()
        for year in active_years:
            year_combo.addItem(year)
        
        button = QPushButton("Submit")

        # Create layout
        layout = QVBoxLayout(self.dialog)
        layout.addWidget(m_label)
        layout.addWidget(combo_month)
        layout.addWidget(y_label)
        layout.addWidget(year_combo)
        layout.addWidget(button)

        # Connect button clicked signal to a custom slot
        button.clicked.connect(lambda: self.submit_month(year=year_combo.currentText()))

        
        self.dialog.exec()

    def selected_month_changed(self, index):
        self.selected_month = index

    def submit_month(self, year):
        if self.selected_month is not None:
            month = months[self.selected_month]["value"]
            self.month = month
            self.year = year
            print(f"""
                 Month submitted: {self.month}  
                 Year Submitted: {self.year}
                  """)
            self.update()
        else:
            print("Please select a month first")

        self.dialog.close()

    def change_view(self, q):
        if q.text() == 'Transactional Actions':
            self.go_to_admin_actions()
        elif q.text() == 'Switch Month':
            self.create_dialog()
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
            
    # 
    def button1_clicked(self):
        print("Clicked on the button")
    
    def switch_mode(self):
        if self.current_mode == "light":
            self.setStyleSheet(DARK_MODE_STYLESHEET)
            self.current_mode = "dark"
        else:
            self.setStyleSheet(LIGHT_MODE_STYLESHEET)
            self.current_mode = "light"

    def switch_to_light_mode(self):
        self.setStyleSheet(LIGHT_MODE_STYLESHEET)
        self.current_mode = "light"

    def switch_to_dark_mode(self):
        self.setStyleSheet(DARK_MODE_STYLESHEET)
        self.current_mode = "dark"
      
    def switch_to_default_mode(self):
        self.setStyleSheet('default')
        self.current_mode = "default"
    
    def set_default_window_size(self):
        # Set the default window size to 800x600
        self.resize(QSize(800, 600))
    
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app",3000)
       