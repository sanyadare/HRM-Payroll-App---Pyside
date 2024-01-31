from PySide6.QtWidgets import QSizePolicy, QTabWidget, QWidget, QLabel,QGridLayout, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QDialog
from pages.employee import Employee
from dummy import d_staff


class Pim(QTabWidget):
    def __init__(self):
        super().__init__()

        # Create three tabs
        self.tab_create_new_staff = QWidget()
        self.tab_view_all_staff = QWidget()
        self.tab_new_user = QWidget()

        # Add tabs to the SalarySetup widget
        self.addTab(self.tab_view_all_staff, "All Staff")
        self.addTab(self.tab_create_new_staff, "Create New Staff")
        
   
        # Setup tab content
        self.create_new_staff_tab()
        self.view_all_staff_tab()
       
      

    def create_new_staff_tab(self):
        layout = QVBoxLayout()
        
        detail_button = QPushButton('Detail')
        layout.addWidget(detail_button)

    def view_all_staff_tab(self):
        layout = QVBoxLayout(self.tab_view_all_staff)
        detail_button = QPushButton('Detail')
        # Add table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(len(d_staff))
        self.table.setHorizontalHeaderLabels(["id", "firstname", 'lastname', 'more'])

        # Add sample data
        for row, data in enumerate(d_staff):
            id_item = QTableWidgetItem(str(data['id']))
            firstname_item = QTableWidgetItem(data['firstname'])
            lastname_item = QTableWidgetItem(data['lastname'])
            # action_btn =QTableWidgetItem(detail_button)
            self.table.setItem(row, 0, id_item)
            self.table.setItem(row, 1, firstname_item)
            self.table.setItem(row, 2, lastname_item)
            # self.table.setItem(row, 3, action_btn)

        # Set size policies for table
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        layout.addWidget(self.table)

        # Connect detail button clicked signal to a custom slot
        self.table.cellClicked.connect(self.detail_button_clicked)

    def detail_button_clicked(self, row, col):
        if col == 3:  # Check if the click occurred in the "action" column
            staff_id = int(self.table.item(row, 0).text())  # Get the staff ID from the first column
            staff_name = f"{self.table.item(row, 1).text()} {self.table.item(row, 2).text()}"  # Get the staff name from the first and second columns
            self.employee_details(staff_id, staff_name)

 
    def employee_details(self, staff_id=1, staff_name='Akyerit Solution'):
        
        # fetch the employee here first 
        
        
        
        # 
        dialog = QDialog()
        dialog.setWindowTitle(f'Staff Details of {staff_name}')
        dialog.resize(800, 600)  # Set the size of the dialog box
        
        employee_page = Employee(staff_id=staff_id )
        t_layout = QHBoxLayout()
        b_layout = QVBoxLayout(dialog)
        
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
        
        dialog.exec_()

# Assuming Employee class is defined elsewhere

