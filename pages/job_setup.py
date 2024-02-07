from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QSizePolicy, QLineEdit, QSpinBox, QTabWidget, QWidget, QFormLayout, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PySide6.QtGui import QIntValidator
from dummy import d_job_titles

class JobSetup(QTabWidget):
    def __init__(self):
        super().__init__()

        self.job_titles = d_job_titles
        
        # Create three tabs
        self.tab_title = QWidget()
        self.tab_status = QWidget()
        self.tab_grade = QWidget()
        self.tab_category = QWidget()
        self.tab_bank = QWidget()
        self.tab_state = QWidget()
        self.tab_college = QWidget()

        # Add tabs to the SalarySetup widget
        self.addTab(self.tab_title, "Title Setup")
        self.addTab(self.tab_status, "Status Setup")
        self.addTab(self.tab_grade, "Description Grade")
        self.addTab(self.tab_category, "Job Category")
        self.addTab(self.tab_bank, "Bank Setup")
        self.addTab(self.tab_state, "State Setup")
        self.addTab(self.tab_college, "College Setup")

        # Setup/Show The tab content
        self._setup_title_tab()
        self._setup_status_tab()
        self._setup_grade_tab()
        self._setup_category_tab()
        self._setup_bank_tab()
        self._setup_state_tab()
        self._setup_college_tab()

    def _setup_title_tab(self):
        main_layout = QHBoxLayout(self.tab_title)
        
        
        # Add table
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(["ID", "Title Name"])

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New Title</b>")
        l_title_name = QLabel('<i>Title Name:</i>')
        title_name = QLineEdit()
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_title_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        title_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_title_name)
        form_layout.addWidget(title_name)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()

    def _setup_status_tab(self):
        main_layout = QHBoxLayout(self.tab_status)
        
        
        # Add table
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(["ID", "Status Name"])

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New Status</b>")
        l_status_name = QLabel('<i>Status Name:</i>')
        status_name = QLineEdit()
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_status_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        status_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_status_name)
        form_layout.addWidget(status_name)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()

    def _setup_grade_tab(self):
        main_layout = QHBoxLayout(self.tab_grade)
        
        
        # Add table
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(["ID", "Grade Name"])

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New Grade</b>")
        l_grade_name = QLabel('<i>Grade Name:</i>')
        grade_name = QLineEdit()
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_grade_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        grade_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_grade_name)
        form_layout.addWidget(grade_name)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()
    
    def _setup_category_tab(self):
        main_layout = QHBoxLayout(self.tab_category)
        
        
        # Add table
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(["ID", "Category Name"])

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New Category</b>")
        l_category_name = QLabel('<i>Category Name:</i>')
        category_name = QLineEdit()
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_category_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        category_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_category_name)
        form_layout.addWidget(category_name)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()
    
    def _setup_bank_tab(self):
        main_layout = QHBoxLayout(self.tab_bank)
        
        
        # Add table
        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(["ID", "Bank Name", 'Sort Code'])

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New Bank</b>")
        l_bank_name = QLabel('<i>Bank Name:</i>')
        bank_name = QLineEdit()
        l_sort_code = QLabel('<i>Sort Code:</i>')
        sort_code = QLineEdit()
        sort_code.setValidator(QIntValidator(0, 200000000))
        # sort_code.setInt
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_bank_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        bank_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_bank_name)
        form_layout.addWidget(bank_name)
        form_layout.addWidget(l_sort_code)
        form_layout.addWidget(sort_code)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()
    
    def _setup_state_tab(self):
        main_layout = QHBoxLayout(self.tab_state)
        
        
        # Add table
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(["ID", "State Name"])

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New State</b>")
        l_state_name = QLabel('<i>State Name:</i>')
        state_name = QLineEdit()
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_state_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        state_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_state_name)
        form_layout.addWidget(state_name)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()
    
    def _setup_college_tab(self):
        main_layout = QHBoxLayout(self.tab_college)
        
        
        # Add table
        table = QTableWidget()
        table.setColumnCount(4)
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(["ID", "Title Name", "Unit", "Sub Unit"])

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New College</b>")
        l_job_title = QLabel('<i>Job Title:</i>')
        job_title = QComboBox()
        for title in self.job_titles:
            job_title.addItem(title['title'])
        l_unit_name = QLabel('<i>Unit Name:</i>')
        unit_name = QLineEdit()
        l_sub_unit_name = QLabel('<i>Sub-Unit Name:</i>')
        sub_unit_name = QLineEdit()
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_job_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        job_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_job_title)
        form_layout.addWidget(job_title)
        form_layout.addWidget(l_unit_name)
        form_layout.addWidget(unit_name)
        form_layout.addWidget(l_sub_unit_name)
        form_layout.addWidget(sub_unit_name)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()
