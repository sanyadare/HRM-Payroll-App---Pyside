from PySide6.QtWidgets import QRadioButton, QDateEdit, QSizePolicy, QTabWidget, QWidget, QLabel, QLineEdit, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QComboBox
from PySide6.QtGui import QAction, QIcon
from pages.employee import Employee
from dummy import d_staff
from stylesheet import DARK_MODE_STYLESHEET,DARK_GREEN_MODE_STYLESHEET, LIGHT_GREEN_MODE_STYLESHEET, LIGHT_BLUE_MODE_STYLESHEET, DARK_BLUE_MODE_STYLESHEET


class Pim(QTabWidget):
    def __init__(self, mode="light-green"):
        super().__init__()

        self.current_mode = mode
        # Create three tabs
        self.tab_create_new_staff = QWidget()
        self.tab_view_all_staff = QWidget()

        # Add tabs to the SalarySetup widget
        self.addTab(self.tab_view_all_staff, "All Staff")
        self.addTab(self.tab_create_new_staff, "Create New Staff")
        
   
        # Setup tab content
        self.create_new_staff_tab()
        self.view_all_staff_tab()
       
      

    def switch_mode(self):
        if self.current_mode == "light-green":
            self.dialog.setStyleSheet(LIGHT_GREEN_MODE_STYLESHEET)
            # self.current_mode = "dark"
        elif self.current_mode == "light-blue":
            self.dialog.setStyleSheet(LIGHT_BLUE_MODE_STYLESHEET)
            # self.current_mode = "light"
        elif self.current_mode == "dark":
            self.dialog.setStyleSheet(DARK_MODE_STYLESHEET)
            # self.current_mode = "light"
        elif self.current_mode == "dark-green":
            self.dialog.setStyleSheet(DARK_GREEN_MODE_STYLESHEET)
            # self.current_mode = "light"
        elif self.current_mode == "dark-blue":
            self.dialog.setStyleSheet(DARK_BLUE_MODE_STYLESHEET)
            # self.current_mode = "light"


    def create_new_staff_tab(self):
        main_layout = QHBoxLayout(self.tab_create_new_staff)
        
        form_layout = QVBoxLayout()
        main_layout.addWidget(QWidget(), 1)
        
        # form
        form_layout.addWidget(QLabel("<b style='font-size:20px'>New Staff Form</b>"))
        
         # sur name
        l_surname = QLabel("<i>SurName:</i>")
        surname = QLineEdit()
        form_layout.addWidget(l_surname)
        form_layout.addWidget(surname)
        
        # first name
        l_first_name = QLabel("<i>First Name:</i>")
        first_name = QLineEdit()
        form_layout.addWidget(l_first_name)
        form_layout.addWidget(first_name)
        
         # other name
        l_other_name = QLabel("<i>Other Name:</i>")
        other_name = QLineEdit()
        form_layout.addWidget(l_other_name)
        form_layout.addWidget(other_name)
        
        # staff ID
        # l_staff_id = QLabel("<i>Staff ID:</i>")
        # staff_id = QSpinBox()
        # form_layout.addWidget(l_staff_id)
        # form_layout.addWidget(staff_id)
        
        # DOB
        l_dob = QLabel("<i>Date Of Birth:</i>")
        dob = QDateEdit()
        form_layout.addWidget(l_dob)
        form_layout.addWidget(dob)
         
         # Sex
        form_layout.addWidget(QLabel("Sex:"))
        cont_sex = QHBoxLayout()
        male = QRadioButton("Male")
        female = QRadioButton("Female")
        male.setChecked(True)
        cont_sex.addWidget(male)
        cont_sex.addWidget(female)
        form_layout.addLayout(cont_sex)
        
        submit_button = QPushButton("Create Staff")
        form_layout.addWidget(submit_button)
        
        form_layout.addWidget(QWidget(), 2)
        main_layout.addLayout(form_layout, 2)
        main_layout.addWidget(QWidget(),1)
        
       

    def view_all_staff_tab(self):
        main_layout = QHBoxLayout(self.tab_view_all_staff)
        
        l_layout = QVBoxLayout()
        detail_button = QPushButton('Detail')
        # Add table
        columns = ["ID", "File Number", "Last Name", "First Name", "Middle Name", "Job Title", "Employment", "Level", "Step", "more"]
        self.table = QTableWidget()
        self.table.setColumnCount(len(columns))
        self.table.setRowCount(len(d_staff))
        self.table.setHorizontalHeaderLabels(columns)

        # Add sample data
        for row, data in enumerate(d_staff):
            id_item = QTableWidgetItem(str(data['id']))
            firstname_item = QTableWidgetItem(data['firstname'])
            lastname_item = QTableWidgetItem(data['lastname'])
            # action_btn =QTableWidgetItem(detail_button)
            self.table.setItem(row, 0, id_item)
            self.table.setItem(row, 2, lastname_item)
            self.table.setItem(row, 3, firstname_item)
            # self.table.setItem(row, 3, action_btn)

        # Set size policies for table
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        l_layout.addWidget(self.table)
        
        r_layout = QVBoxLayout()
        
        r_layout.addWidget(QLabel("Find A Staff"))
        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search a Staff By Staff ID")
        search_button = QPushButton(icon=QIcon("assets/logo.png"))
        search_layout.addWidget(search_input, 7)
        search_layout.addWidget(search_button, 1)
        r_layout.addLayout(search_layout)
        
        
        # Staff Name
        l_name = QLabel("Name:")
        name = QLineEdit()
        r_layout.addWidget(l_name)
        r_layout.addWidget(name)
        
        # Staff ID
        l_staff_id = QLabel("Staff ID:")
        staff_id = QSpinBox()
        r_layout.addWidget(l_staff_id)
        r_layout.addWidget(staff_id)
        
        # ComboBox
        l_combo = QLabel("Employed:")
        combo = QComboBox()
        combo.addItem('Staff')
        combo.addItem('NYSC')
        r_layout.addWidget(l_combo)
        r_layout.addWidget(combo)
        
        # Button Container
        cont_buttons = QHBoxLayout()
        view_all_button = QPushButton("View All")
        view_negative_button = QPushButton("View Negative")
        cont_buttons.addWidget(view_all_button)
        cont_buttons.addWidget(view_negative_button)
        r_layout.addLayout(cont_buttons)
        
        
        r_layout.addWidget(QWidget(), 3)
        main_layout.addLayout(l_layout, 3)
        main_layout.addLayout(r_layout, 1)
        # Add table to layout

        # Connect detail button clicked signal to a custom slot
        self.table.cellClicked.connect(self.detail_button_clicked)

    def detail_button_clicked(self, row, col):
        if col == 9:  # Check if the click occurred in the "action" column
            staff_id = int(self.table.item(row, 0).text())  # Get the staff ID from the first column
            staff_name = f"{self.table.item(row, 3).text()} {self.table.item(row, 2).text()}"  # Get the staff name from the first and second columns
            self.employee_details(staff_id, staff_name)

 
    def employee_details(self, staff_id=1, staff_name='Akyerit Solution'):
        
        self.dialog = QDialog()
        self.switch_mode()
        # fetch the employee here first 
        
        # 
        self.dialog.setWindowTitle(f'Staff Details of {staff_name}')
        self.dialog.resize(900, 400)  # Set the size of the dialog box
        
        employee_page = Employee(staff_id=staff_id )
        t_layout = QHBoxLayout()
        b_layout = QVBoxLayout(self.dialog)
        
        # staff Number
        staff_number_cont = QVBoxLayout()
        l_staff_number = QLabel('Staff Number:')
        staff_number = QLabel(f'<b>{staff_id}</b>')
        staff_number_cont.addWidget(l_staff_number)
        staff_number_cont.addWidget(staff_number)
        t_layout.addLayout(staff_number_cont)
        
        # department
        department_cont = QVBoxLayout()
        l_department = QLabel('Department/Unit:')
        department = QLabel(f'<b>Fetched Department</b>')
        department_cont.addWidget(l_department)
        department_cont.addWidget(department)
        t_layout.addLayout(department_cont)
        
        # post
        post_cont = QVBoxLayout()
        l_post = QLabel('Post:')
        post = QLabel(f'<b>Senior</b>')
        post_cont.addWidget(l_post)
        post_cont.addWidget(post)
        t_layout.addLayout(post_cont)
        
        # jobtile
        job_title_cont = QVBoxLayout()
        l_job_title = QLabel('Job Title:')
        job_title = QLabel(f'<b>Developer</b>')
        job_title_cont.addWidget(l_job_title)
        job_title_cont.addWidget(job_title)
        t_layout.addLayout(job_title_cont)
        
        # location
        location_cont = QVBoxLayout()
        l_location = QLabel('Location:')
        location = QLabel(f'<b>osogbo</b>')
        location_cont.addWidget(l_location)
        location_cont.addWidget(location)
        t_layout.addLayout(location_cont)

        
        
        
        b_layout.addLayout(t_layout)
        b_layout.addWidget(employee_page)
        
        self.dialog.exec_()

    def setMode(self, new_mode):
        self.current_mode = new_mode
        # self.dialog.update()

