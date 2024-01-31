from PySide6.QtWidgets import QTextEdit,QSpinBox, QComboBox,QGroupBox, QRadioButton, QDateEdit, QSizePolicy, QTabWidget, QLabel, QWidget,QGridLayout, QFormLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtGui import QIntValidator
from dummy import d_bank_names, d_countries, d_job_titles, d_nature_of_appointment, d_employment_status, d_job_designation, d_values

class Employee(QTabWidget):
    def __init__(self, staff_id=1):
        super().__init__()

        self.edit = True
        self.countries = d_countries
        self.bank_names = d_bank_names
        self.pension_bank_names = d_bank_names
        self.job_titles = d_job_titles
        self.nature_of_appointment =d_nature_of_appointment
        self.job_designation = d_job_designation
        self.employment_status = d_employment_status
        self.d_values = d_values
        
        # Create three tabs
        self.tab_personal_details = QWidget()
        self.tab_contact_details = QWidget()
        self.tab_emergency_details = QWidget()
        # self.tab_dependants = QWidget()
        self.tab_job = QWidget()
        self.tab_salary = QWidget()
        self.tab_qualifications = QWidget()
        self.tab_account_details = QWidget()

        # Add tabs to the SalarySetup widget
        self.addTab(self.tab_personal_details, "Personal Details")
        self.addTab(self.tab_contact_details, "Contact Details")
        self.addTab(self.tab_account_details, "Account Details")
        self.addTab(self.tab_emergency_details, "Emergency Details")
        # self.addTab(self.tab_dependants, "Dependants")
        self.addTab(self.tab_job, "Job")
        self.addTab(self.tab_salary, "Salary")
        self.addTab(self.tab_qualifications, "Qualifications")
        
   
        # Setup tab content
        self.personal_details_tab()
        self.contact_details_tab()
        self.account_details_tab()
        self.emergency_contact_tab()
        self.job_tab()
       
    def set_Edit(self):
        self.edit = True
        print('editing ', self.edit)
        self.update()
        # self.tab_personal_details.close()
        # self.personal_details_tab(True)
        # self.personal_details_tab()
        # return self.edit

    def personal_details_tab(self):
        main_layout = QHBoxLayout(self.tab_personal_details)
        
        # Form elements for edit
        grid_layout = QGridLayout()
        full_name_layout = QVBoxLayout()
        # l_full_name = QLabel('Full Name')
        # full_name_layout.addWidget(l_full_name)
        
        # surname
        g_surname = QVBoxLayout()
        l_surname = QLabel('<i>Surname:</i>')
        new_surname = QLineEdit()
        # new_surname.setEnabled(self.edit)
        new_surname.setText('current surname')
        new_surname.setPlaceholderText('')
        g_surname.addWidget(l_surname)
        g_surname.addWidget(new_surname)
        full_name_layout.addLayout(g_surname)
        
        # first name
        g_first_name = QVBoxLayout()
        l_first_name = QLabel('<i>First Name:</i>')
        new_first_name = QLineEdit()
        new_first_name.setPlaceholderText('current first name')
        g_surname.addWidget(l_first_name)
        g_surname.addWidget(new_first_name)
        full_name_layout.addLayout(g_first_name)
        
        # Middle name
        g_middle_name = QVBoxLayout()
        l_middle_name = QLabel('<i>Middle Name:</i>')
        new_middle_name = QLineEdit()
        new_middle_name.setPlaceholderText('current middle name')
        full_name_layout.addWidget(l_middle_name)
        full_name_layout.addWidget(new_middle_name)
        full_name_layout.addLayout(g_middle_name)
        
        
        employee_layout = QVBoxLayout()
        # Employee id
        g_employee_id = QVBoxLayout()
        l_employee_id = QLabel('<i>Employee ID:</i>')
        new_employee_id = QLineEdit()
        new_employee_id.setPlaceholderText('current employee id')
        full_name_layout.addWidget(l_employee_id)
        full_name_layout.addWidget(new_employee_id)
        full_name_layout.addLayout(g_employee_id)
        
        # Email Address
        g_employee_email = QVBoxLayout()
        l_employee_email = QLabel('<i>Email Address:</i>')
        new_employee_email = QLineEdit()
        new_employee_email.setPlaceholderText('current email address')
        full_name_layout.addWidget(l_employee_email)
        full_name_layout.addWidget(new_employee_email)
        full_name_layout.addLayout(g_employee_email)
        
        # Government ID
        g_gov_id = QVBoxLayout()
        l_gov_id = QLabel('<i>Govenment ID:</i>')
        new_gov_id = QLineEdit()
        new_gov_id.setPlaceholderText('current')
        full_name_layout.addWidget(l_gov_id)
        full_name_layout.addWidget(new_gov_id)
        full_name_layout.addLayout(g_gov_id)
        
        # Expiring Date
        g_exp_date = QVBoxLayout()
        l_exp_date = QLabel('<i>Expiring Date:</i>')
        new_exp_date = QDateEdit()
        # new_exp_date.setPlaceholderText('current')
        full_name_layout.addWidget(l_exp_date)
        full_name_layout.addWidget(new_exp_date)
        full_name_layout.addLayout(g_exp_date)
        
        # nationality, dob
        
        # gender
        
        male = QRadioButton("Male")
        female = QRadioButton("Female")    
        male.setChecked(True)    
        l_gender = QLabel('<i>Gender:</i>')
        g_gender = QHBoxLayout()
        g_gender.addWidget(l_gender)
        g_gender.addWidget(male)
        g_gender.addWidget(female)
        # gender.setLayout(g_gender)
        full_name_layout.addLayout(g_gender)
        
        # marital Status   
        g_marital_status = QVBoxLayout()
        l_marital_status = QLabel('<i>Marital Status:</i>')
        c_marital_status =QComboBox()
        c_marital_status.addItem('Single')
        c_marital_status.addItem('Married')
        c_marital_status.addItem('Divorced')
        g_marital_status.addWidget(l_marital_status)
        g_marital_status.addWidget(c_marital_status)
        full_name_layout.addLayout(g_marital_status)
        
        # marital Status   
        g_nationality = QVBoxLayout()
        l_nationality = QLabel('<i>Nationality:</i>')
        c_nationality =QComboBox()
        c_nationality.addItem('Nigerian')
        c_nationality.addItem('Other')
        g_nationality.addWidget(l_nationality)
        g_nationality.addWidget(c_nationality)
        full_name_layout.addLayout(g_nationality)
        
        # dob
        g_dob = QVBoxLayout()
        l_dob = QLabel('<i>Date Of Birth:</i>')
        c_dob =QDateEdit()
        g_dob.addWidget(l_dob)
        g_dob.addWidget(c_dob)
        full_name_layout.addLayout(g_dob)
        
        if self.edit:
            submit_button = QPushButton('Submit')
            
            main_layout.addLayout(full_name_layout )
            main_layout.addLayout(employee_layout )
            main_layout.addWidget(submit_button)
        else:
            edit_button = QPushButton('Edit')
            edit_button.clicked.connect(self.set_Edit)
            main_layout.addLayout(full_name_layout )
            main_layout.addLayout(employee_layout )
            main_layout.addWidget(edit_button)
            
        
       
        # main_layout.addStretch()

    def contact_details_tab(self):
        main_layout = QHBoxLayout(self.tab_contact_details)
        
        # Form elements for edit
        form_layout = QVBoxLayout()        
        # Address Street 1
        l_address_1 = QLabel('<i>Address Street 1:</i>')
        new_address_1 = QLineEdit()
        # new_address_1.setText('current surname')
        new_address_1.setPlaceholderText('')
        form_layout.addWidget(l_address_1)
        form_layout.addWidget(new_address_1)
        
        # Address Street 2
        l_address_2 = QLabel('<i>Address Street 2:</i>')
        new_address_2 = QLineEdit()
        new_address_2.setPlaceholderText('')
        form_layout.addWidget(l_address_2)
        form_layout.addWidget(new_address_2)
        
        # City
        l_city = QLabel('<i>City:</i>')
        new_city = QLineEdit()
        new_city.setPlaceholderText('current city')
        form_layout.addWidget(l_city)
        form_layout.addWidget(new_city)        
        
        # State/Province
        l_state_province = QLabel('<i>State/Province:</i>')
        new_state_province = QLineEdit()
        # new_state_province.setPlaceholderText('current employee id')
        form_layout.addWidget(l_state_province)
        form_layout.addWidget(new_state_province)
        
        # Zip/Postal Code
        l_zip_code = QLabel('<i>Zip Code:</i>')
        new_zip_code = QLineEdit()
        # new_zip_code.setPlaceholderText('current')
        form_layout.addWidget(l_zip_code)
        form_layout.addWidget(new_zip_code)
        
        # Country
        l_country = QLabel('<i>Country:</i>')
        new_country = QComboBox()
        for country in self.countries:
            item = country.get('name')
            if item:
                new_country.addItem(item)
        # new_country.setPlaceholderText('current email address')
        form_layout.addWidget(l_country)
        form_layout.addWidget(new_country)
        
        # Mobile Telephone
        l_mobile_tel = QLabel('<i>Mobile Telephone:</i>')
        new_mobile_tel = QLineEdit()
        # new_mobile_tel.setValidator(QIntValidator)
        # new_exp_date.setPlaceholderText('current')
        form_layout.addWidget(l_mobile_tel)
        form_layout.addWidget(new_mobile_tel)
        
        # Mobile Telephone
        l_work_tel = QLabel('<i>Work Telephone:</i>')
        new_work_tel = QLineEdit()
        # new_work_tel.setValidator(QIntValidator)
        # new_exp_date.setPlaceholderText('current')
        form_layout.addWidget(l_work_tel)
        form_layout.addWidget(new_work_tel)
        
        # Email Address
        l_email_address = QLabel('<i>Email Address:</i>')
        new_email_address = QLineEdit()
        # new_exp_date.setPlaceholderText('current')
        form_layout.addWidget(l_email_address)
        form_layout.addWidget(new_email_address)
    
        submit_button = QPushButton('Submit')
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
     
    def account_details_tab(self):
        main_layout = QHBoxLayout(self.tab_account_details)
        
        # Form elements for edit
        form_layout = QVBoxLayout()        
        # bank name
        l_bank_name = QLabel('<i>Bank Name:</i>')
        new_bank_name = QComboBox()
        for country in self.bank_names:
            item = country.get('name')
            if item:
                new_bank_name.addItem(item)
        form_layout.addWidget(l_bank_name)
        form_layout.addWidget(new_bank_name)
        
        # account number
        l_account_name = QLabel('<i>Account Number:</i>')
        new_account_name = QLineEdit()
        # new_account_name.setValidator(QIntValidator)
        form_layout.addWidget(l_account_name)
        form_layout.addWidget(new_account_name)
        
        # sort code
        l_sort_code = QLabel('<i>Sort Code:</i>')
        new_sort_code = QSpinBox()
        form_layout.addWidget(l_sort_code)
        form_layout.addWidget(new_sort_code)        
        
        # bvn number
        l_bvn = QLabel('<i>BVN Number:</i>')
        new_bvn = QLineEdit()
        form_layout.addWidget(l_bvn)
        form_layout.addWidget(new_bvn)
        
        # nin number
        l_nin = QLabel('<i>Nigeria Identification Number (NIN):</i>')
        new_nin = QLineEdit()
        form_layout.addWidget(l_nin)
        form_layout.addWidget(new_nin)
        
        # pension bank name
        l_pension_bank_name = QLabel('<i>Pension Bank Name:</i>')
        new_pension_bank_name = QComboBox()
        for country in self.bank_names:
            item = country.get('name')
            if item:
                new_pension_bank_name.addItem(item)
        form_layout.addWidget(l_pension_bank_name)
        form_layout.addWidget(new_pension_bank_name)
        
        # pension account number
        l_pension_account_name = QLabel('<i>Account Number:</i>')
        new_pension_account_name = QLineEdit()
        # new_account_name.setValidator(QIntValidator)
        form_layout.addWidget(l_pension_account_name)
        form_layout.addWidget(new_pension_account_name)
        
        submit_button = QPushButton('Submit')
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
     
    
    def emergency_contact_tab(self):
        main_layout = QHBoxLayout(self.tab_emergency_details)
        
        # Form elements for edit
        form_layout = QVBoxLayout()        
        # company
        l_company = QLabel('<i>Company:</i>')
        new_company = QLineEdit()
        # new_address_1.setText('current surname')
        new_company.setPlaceholderText('')
        form_layout.addWidget(l_company)
        form_layout.addWidget(new_company)
        
        # job title
        l_job_title = QLabel('<i>Job Title:</i>')
        new_job_title = QLineEdit()
        new_job_title.setPlaceholderText('')
        form_layout.addWidget(l_job_title)
        form_layout.addWidget(new_job_title)
        
        # from date
        l_from_date = QLabel('<i>From Date:</i>')
        new_from_date = QDateEdit()
        form_layout.addWidget(l_from_date)
        form_layout.addWidget(new_from_date)        
        
        # to date
        l_to_date = QLabel('<i>To Date:</i>')
        new_to_date = QLineEdit()
        form_layout.addWidget(l_to_date)
        form_layout.addWidget(new_to_date)
        
        # comment
        l_comment = QLabel('<i>Comment:</i>')
        new_comment = QTextEdit()
        form_layout.addWidget(l_comment)
        form_layout.addWidget(new_comment)
        
    
        submit_button = QPushButton('Submit')
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
     
 
    def job_tab(self):
        main_layout = QHBoxLayout(self.tab_job)
        
        # Form elements for edit
        l_layout = QVBoxLayout()     
           
        # job title
        l_job_title = QLabel('<i>Job Title:</i>')
        new_job_title = QComboBox()
        for country in self.job_titles:
            item = country.get('title')
            if item:
                new_job_title.addItem(item)
        l_layout.addWidget(l_job_title)
        l_layout.addWidget(new_job_title)
        
        # Nature of Appointment
        l_NOA = QLabel('<i>Nature Of Appointment:</i>')
        new_NOA = QComboBox()
        for nature in self.nature_of_appointment:
            item = nature.get('title')
            if item:
                new_NOA.addItem(item)
        l_layout.addWidget(l_NOA)
        l_layout.addWidget(new_NOA)
        
        # job designation
        l_job_designation = QLabel('<i>Job Designation:</i>')
        new_job_designation = QComboBox()
        for job in self.job_designation:
            item = job.get('name')
            if item:
                new_job_designation.addItem(item)
        l_layout.addWidget(l_job_designation)
        l_layout.addWidget(new_job_designation)     
        
        # Employment Status
        l_employment_status = QLabel('<i>Employment Status:</i>')
        new_employment_status = QComboBox()
        for status in self.employment_status:
            item = status.get('name')
            if item:
                new_employment_status.addItem(item)
        l_layout.addWidget(l_employment_status)
        l_layout.addWidget(new_employment_status)     
        
        # Job Category
        l_job_category = QLabel('<i>Job Category:</i>')
        new_job_category = QComboBox()
        # new_job_category.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_job_category.addItem(item)
        l_layout.addWidget(l_job_category)
        l_layout.addWidget(new_job_category)     
        
        # Grade level
        l_grade_level = QLabel('<i>Level:</i>')
        new_grade_level = QComboBox()
        new_grade_level.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_grade_level.addItem(item)
        l_layout.addWidget(l_grade_level)
        l_layout.addWidget(new_grade_level)  
        
        # Unit
        l_unit = QLabel('<i>Unit:</i>')
        new_unit = QComboBox()
        new_unit.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_unit.addItem(item)
        l_layout.addWidget(l_unit)
        l_layout.addWidget(new_unit)  
        
        # Sub Unit
        l_sub_unit = QLabel('<i>Sub Unit:</i>')
        new_sub_unit = QComboBox()
        new_sub_unit.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_sub_unit.addItem(item)
        l_layout.addWidget(l_sub_unit)
        l_layout.addWidget(new_sub_unit)  
        
        # Location
        l_location = QLabel('<i>Location:</i>')
        new_location = QComboBox()
        new_location.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_location.addItem(item)
        l_layout.addWidget(l_location)
        l_layout.addWidget(new_location)  
        
        r_layout = QVBoxLayout()
        # joined date
        l_joined_date = QLabel('<i>Joined Date:</i>')
        new_joined_date = QDateEdit()
        r_layout.addWidget(l_joined_date)
        r_layout.addWidget(new_joined_date)
        
         # start date
        l_start_date = QLabel('<i>End Date:</i>')
        new_start_date = QDateEdit()
        r_layout.addWidget(l_start_date)
        r_layout.addWidget(new_start_date)
        
         # end date
        l_end_date = QLabel('<i>End Date:</i>')
        new_end_date = QDateEdit()
        r_layout.addWidget(l_end_date)
        r_layout.addWidget(new_end_date)
        
         # Pay Percentage
        l_p_pay = QLabel('<i>Percentage Pay:</i>')
        new_p_pay = QSpinBox()
        new_p_pay.setRange(0, 100)
        r_layout.addWidget(l_p_pay)
        r_layout.addWidget(new_p_pay)
        
         # Days
        l_day = QLabel('<i>Day:(Total Days in a month)</i>')
        new_day = QSpinBox()
        new_day.setRange(0, 31)
        r_layout.addWidget(l_day)
        r_layout.addWidget(new_day)
        
         # Year Of Service
        l_year_of_service = QLabel('<i>Year Of Service:</i>')
        new_year_of_service = QSpinBox()
        new_day.setRange(2000, 3000)
        r_layout.addWidget(l_year_of_service)
        r_layout.addWidget(new_year_of_service)
        
         # Year Of Service
        l_comment = QLabel('<i>Comment:</i>')
        new_comment = QLineEdit()
        r_layout.addWidget(l_comment)
        r_layout.addWidget(new_comment)
    
        submit_button = QPushButton('Submit')
        main_layout.addLayout(l_layout, 1)
        main_layout.addLayout(r_layout, 1)
        # main_layout.addWidget(submit_button)
     

  
    