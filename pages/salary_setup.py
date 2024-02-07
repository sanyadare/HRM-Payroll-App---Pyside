from PySide6.QtWidgets import QComboBox, QSpinBox,QSizePolicy, QTabWidget, QLabel, QWidget, QFormLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtGui import QIntValidator
from dummy import d_account_name, d_currencies


class SalarySetup(QTabWidget):
    def __init__(self):
        """
        This Class create the Salary Setup Page(TabWidget)
        """
        
        super().__init__()

        self.account_names = d_account_name
        self.currencies = d_currencies
        
        # Create three tabs
        self.tab_allowance = QWidget()
        self.tab_deduction = QWidget()
        self.tab_grade = QWidget()
        
        # Add tabs to the SalarySetup widget
        self.addTab(self.tab_allowance, "Allowance Setup")
        self.addTab(self.tab_deduction, "Deduction Setup")
        self.addTab(self.tab_grade, "Salary Grade")

        # Setup tab content
        self._setup_allowance_tab()
        self._setup_deduction_tab()
        self._setup_grade_tab()

    def _setup_allowance_tab(self):
        main_layout = QHBoxLayout(self.tab_allowance)
        
        # Add table
        table = QTableWidget()
        columns = ["ID", "Allowance Name"]
        table.setColumnCount(len(columns))
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(columns)

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
        form_title = QLabel("<b style='font-size:20px'>Add New Salary</b>")
        l_salary_name = QLabel('<i>Salary Name:</i>')
        salary_name = QLineEdit()
        submit_button = QPushButton('Submit')
               
        # Set size policies for form elements
        form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        l_salary_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        salary_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        form_layout = QVBoxLayout()
        form_layout.addWidget(form_title)
        form_layout.addWidget(l_salary_name)
        form_layout.addWidget(salary_name)
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2) # This only function is to space
        
        l_layout = QVBoxLayout() 
        l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(l_layout, 1)
        main_layout.addStretch()

    def handle_add_allowance(self):
        pass


    def _setup_deduction_tab(self):
        main_layout = QHBoxLayout(self.tab_deduction)
        
        # Add table
        table = QTableWidget()
        columns = ["ID", "Deduction Name"]
        table.setColumnCount(len(columns))
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(columns)

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        form_layout = QVBoxLayout()
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New Deduction</b>")
        form_layout.addWidget(form_title)
        # deduction name
        l_deduction_name = QLabel('<i>Deduction Name:</i>')
        deduction_name = QLineEdit()
        form_layout.addWidget(l_deduction_name)
        form_layout.addWidget(deduction_name)
        
        # account name
        l_acct_name = QLabel('<i>Account Name:</i>')
        acct_name_combo = QComboBox()
        for account in self.account_names:
            acct_name_combo.addItem(account)
        form_layout.addWidget(l_acct_name)
        form_layout.addWidget(acct_name_combo)
        
        # account number
        l_acct_number = QLabel('<i>Account Number:</i>')
        acct_number = QLineEdit()
        form_layout.addWidget(l_acct_number)
        form_layout.addWidget(acct_number)
        
        # sort code
        l_sort_code = QLabel('<i>Sort Code:</i>')
        sort_code = QLineEdit()
        form_layout.addWidget(l_sort_code)
        form_layout.addWidget(sort_code)
        
        submit_button = QPushButton('Submit')
        form_layout.addWidget(submit_button)
        form_layout.addWidget(QWidget(), 2)
        # Set size policies for form elements
        # form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # l_deduction_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # deduction_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        
        
        
        # l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(form_layout, 1)
        main_layout.addStretch()

    def handle_add_deduction(self):
        pass


    def _setup_grade_tab(self):
        main_layout = QHBoxLayout(self.tab_grade)
        
        # Add table
        columns = ["ID","Name", "Amount", "Rent", "Percular", "Currency", "Teaching", "Rural", "Call Duty", "Level", "Step"]
        table = QTableWidget()
        table.setColumnCount(len(columns))
        table.setRowCount(3)
        table.setHorizontalHeaderLabels(columns)

        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                table.setItem(row, col, item)

        # Set size policies for table
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        main_layout.addWidget(table, 3)
        
        form_layout = QVBoxLayout()
        
        # Form elements for add
        form_title = QLabel("<b style='font-size:20px'>Add New Salary Grade</b>")
        form_layout.addWidget(form_title)
        # grade name
        l_deduction_name = QLabel('<i>Grade Name:</i>')
        deduction_name = QLineEdit()
        form_layout.addWidget(l_deduction_name)
        form_layout.addWidget(deduction_name)
        
        # currency
        l_currency = QLabel('<i>Currency:</i>')
        currency_combo = QComboBox()
        for currency in self.currencies:
            currency_combo.addItem(currency)
        form_layout.addWidget(l_currency)
        form_layout.addWidget(currency_combo)
        
        # amount
        l_acct_number = QLabel('<i>Account Number:</i>')
        acct_number = QSpinBox()
        acct_number.setRange(0, 900000000)
        form_layout.addWidget(l_acct_number)
        form_layout.addWidget(acct_number)
        
        # teaching allowance
        l_t_allownce = QLabel('<i>Teaching Allowance:</i>')
        t_allownce = QSpinBox()
        t_allownce.setRange(0, 900000000)
        form_layout.addWidget(l_t_allownce)
        form_layout.addWidget(t_allownce)
        
         # shifting allowance
        l_s_allowance = QLabel('<i>Shifting Allowance:</i>')
        s_allowance = QSpinBox()
        s_allowance.setRange(0, 900000000)
        form_layout.addWidget(l_s_allowance)
        form_layout.addWidget(s_allowance)
        
         # call duty
        l_call_duty = QLabel('<i>Call Duty:</i>')
        call_duty = QSpinBox()
        # call_duty.setValidator(QIntValidator(0, 200000000))
        form_layout.addWidget(l_call_duty)
        form_layout.addWidget(call_duty)
        
         # call duty thearter
        l_call_thearter = QLabel('<i>Call Thearter:</i>')
        call_thearter = QSpinBox()
        call_thearter.setRange(0, 900000000)
        form_layout.addWidget(l_call_thearter)
        form_layout.addWidget(call_thearter)
        
         # rural
        l_rural = QLabel('<i>Rural:</i>')
        rural = QSpinBox()
        rural.setRange(0, 900000000)
        form_layout.addWidget(l_rural)
        form_layout.addWidget(rural)
        
         # level
        l_level = QLabel('<i>Level:</i>')
        level = QSpinBox()
        level.setRange(1, 15)
        form_layout.addWidget(l_level)
        form_layout.addWidget(level)
        
         # step
        l_step = QLabel('<i>Step:</i>')
        step = QSpinBox()
        step.setRange(0, 900000000)
        form_layout.addWidget(l_step)
        form_layout.addWidget(step)
        
         # step
        l_comment = QLabel('<i>Comment:</i>')
        comment = QLineEdit()
        form_layout.addWidget(l_comment)
        form_layout.addWidget(comment)
        
        submit_button = QPushButton('Submit')
        form_layout.addWidget(submit_button)
        # Set size policies for form elements
        # form_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # l_deduction_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # deduction_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        
        
        
        # l_layout.addLayout(form_layout, 1)
        main_layout.addLayout(form_layout, 1)
        main_layout.addStretch()

    def handle_add_salary(self):
        pass