from PySide6.QtWidgets import QTextEdit,QSpinBox, QComboBox,QGroupBox,QRadioButton, QDateEdit, QSizePolicy, QTabWidget, QLabel, QWidget,QGridLayout, QFormLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
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
        self.salary_tab()
        self.qualifications_tab()
       
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
        full_name_layout = QVBoxLayout()
        
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
        g_first_name.addWidget(l_first_name)
        g_first_name.addWidget(new_first_name)
        # full_name_layout.addLayout(g_first_name)
        
        # Middle name
        g_middle_name = QVBoxLayout()
        l_middle_name = QLabel('<i>Middle Name:</i>')
        new_middle_name = QLineEdit()
        new_middle_name.setPlaceholderText('current middle name')
        g_middle_name.addWidget(l_middle_name)
        g_middle_name.addWidget(new_middle_name)
        # full_name_layout.addLayout(g_middle_name)
        
        # first and middle name
        f_m_cont = QHBoxLayout()
        f_m_cont.addLayout(g_first_name)
        f_m_cont.addLayout(g_middle_name)
        full_name_layout.addLayout(f_m_cont)
        
        employee_layout = QVBoxLayout()
        # Employee id
        g_employee_id = QVBoxLayout()
        l_employee_id = QLabel('<i>Employee ID:</i>')
        new_employee_id = QLineEdit()
        new_employee_id.setPlaceholderText('current employee id')
        g_employee_id.addWidget(l_employee_id)
        g_employee_id.addWidget(new_employee_id)
        
        # Email Address
        g_employee_email = QVBoxLayout()
        l_employee_email = QLabel('<i>Email Address:</i>')
        new_employee_email = QLineEdit()
        new_employee_email.setPlaceholderText('current email address')
        g_employee_email.addWidget(l_employee_email)
        g_employee_email.addWidget(new_employee_email)

         # employee ID + Email
        id_e_cont = QHBoxLayout()
        id_e_cont.addLayout(g_employee_id)
        id_e_cont.addLayout(g_employee_email)
        full_name_layout.addLayout(id_e_cont)
        
        # Government ID
        g_gov_id = QVBoxLayout()
        l_gov_id = QLabel('<i>Govenment ID:</i>')
        new_gov_id = QLineEdit()
        new_gov_id.setPlaceholderText('current')
        g_gov_id.addWidget(l_gov_id)
        g_gov_id.addWidget(new_gov_id)
        
        # Expiring Date
        g_exp_date = QVBoxLayout()
        l_exp_date = QLabel('<i>Expiring Date:</i>')
        new_exp_date = QDateEdit()
        # new_exp_date.setPlaceholderText('current')
        g_exp_date.addWidget(l_exp_date)
        g_exp_date.addWidget(new_exp_date)
        
        # gov id + expiration date
        gid_exp_cont = QHBoxLayout()
        gid_exp_cont.addLayout(g_gov_id, 1)
        gid_exp_cont.addLayout(g_exp_date, 1)
        full_name_layout.addLayout(gid_exp_cont)
        
        # gender
        g_gender_options = QHBoxLayout()
        male = QRadioButton("Male")
        female = QRadioButton("Female")    
        male.setChecked(True)    
        l_gender = QLabel('<i>Gender:</i>')
        g_gender = QVBoxLayout()
        g_gender_options.addWidget(male)
        g_gender_options.addWidget(female)
        g_gender.addWidget(l_gender)
        g_gender.addLayout(g_gender_options)
        
        # marital Status   
        g_marital_status = QVBoxLayout()
        l_marital_status = QLabel('<i>Marital Status:</i>')
        c_marital_status =QComboBox()
        c_marital_status.addItem('Single')
        c_marital_status.addItem('Married')
        c_marital_status.addItem('Divorced')
        g_marital_status.addWidget(l_marital_status)
        g_marital_status.addWidget(c_marital_status)
        
        # gender and marital status
        g_m_cont = QHBoxLayout()
        g_m_cont.addLayout(g_gender, 1)
        g_m_cont.addLayout(g_marital_status, 1)
        full_name_layout.addLayout(g_m_cont)
        
        # nationality   
        g_nationality = QVBoxLayout()
        l_nationality = QLabel('<i>Nationality:</i>')
        c_nationality =QComboBox()
        c_nationality.addItem('Nigerian')
        c_nationality.addItem('Other')
        g_nationality.addWidget(l_nationality)
        g_nationality.addWidget(c_nationality)
        
        # dob
        g_dob = QVBoxLayout()
        l_dob = QLabel('<i>Date Of Birth:</i>')
        c_dob =QDateEdit()
        g_dob.addWidget(l_dob)
        g_dob.addWidget(c_dob)
        
        # nationilty + dob
        n_dob_cont = QHBoxLayout()
        n_dob_cont.addLayout(g_nationality)
        n_dob_cont.addLayout(g_dob)
        full_name_layout.addLayout(n_dob_cont)
        
        full_name_layout.addWidget(QWidget(), 5)
        
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
        g_city = QVBoxLayout()
        l_city = QLabel('<i>City:</i>')
        new_city = QLineEdit()
        new_city.setPlaceholderText('current city')
        g_city.addWidget(l_city)
        g_city.addWidget(new_city)        
        
        # State/Province
        g_state = QVBoxLayout()
        l_state_province = QLabel('<i>State/Province:</i>')
        new_state_province = QLineEdit()
        # new_state_province.setPlaceholderText('current employee id')
        g_state.addWidget(l_state_province)
        g_state.addWidget(new_state_province)
        
        # Zip/Postal Code
        g_zip = QVBoxLayout()
        l_zip_code = QLabel('<i>Zip Code:</i>')
        new_zip_code = QLineEdit()
        # new_zip_code.setPlaceholderText('current')
        g_zip.addWidget(l_zip_code)
        g_zip.addWidget(new_zip_code)
        
        # city + state + zip
        c_s_zip_cont = QHBoxLayout()
        c_s_zip_cont.addLayout(g_city)
        c_s_zip_cont.addLayout(g_state)
        c_s_zip_cont.addLayout(g_zip)
        form_layout.addLayout(c_s_zip_cont)
        
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
        g_mobile = QVBoxLayout()
        l_mobile_tel = QLabel('<i>Mobile Telephone:</i>')
        new_mobile_tel = QLineEdit()
        g_mobile.addWidget(l_mobile_tel)
        g_mobile.addWidget(new_mobile_tel)
        
        # Work Telephone
        g_work = QVBoxLayout()
        l_work_tel = QLabel('<i>Work Telephone:</i>')
        new_work_tel = QLineEdit()
        g_work.addWidget(l_work_tel)
        g_work.addWidget(new_work_tel)
        
        # Mobile + Work Telephone
        m_m_t_cont = QHBoxLayout()
        m_m_t_cont.addLayout(g_mobile, 1)
        m_m_t_cont.addLayout(g_work, 1)
        form_layout.addLayout(m_m_t_cont)
        
        # Email Address
        l_email_address = QLabel('<i>Email Address:</i>')
        new_email_address = QLineEdit()
        # new_exp_date.setPlaceholderText('current')
        form_layout.addWidget(l_email_address)
        form_layout.addWidget(new_email_address)
        form_layout.addWidget(QWidget(), 5)
    
        submit_button = QPushButton('Submit')
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
     
    def account_details_tab(self):
        main_layout = QHBoxLayout(self.tab_account_details)
        
        # Form elements for edit
        form_layout = QVBoxLayout()   
             
        # bank name
        g_bank_name = QVBoxLayout()
        l_bank_name = QLabel('<i>Bank Name:</i>')
        new_bank_name = QComboBox()
        for country in self.bank_names:
            item = country.get('name')
            if item:
                new_bank_name.addItem(item)
        g_bank_name.addWidget(l_bank_name)
        g_bank_name.addWidget(new_bank_name)
        
        # account number
        g_account_number = QVBoxLayout()
        l_account_number = QLabel('<i>Account Number:</i>')
        new_account_number = QLineEdit()
        # new_account_name.setValidator(QIntValidator)
        g_account_number.addWidget(l_account_number)
        g_account_number.addWidget(new_account_number)
        
        # account name + account number
        acct_cont = QHBoxLayout()
        acct_cont.addLayout(g_bank_name, 1)
        acct_cont.addLayout(g_account_number, 1)
        form_layout.addLayout(acct_cont)
        
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
        g_p_bank_name = QVBoxLayout()
        l_pension_bank_name = QLabel('<i>Pension Bank Name:</i>')
        new_pension_bank_name = QComboBox()
        for country in self.bank_names:
            item = country.get('name')
            if item:
                new_pension_bank_name.addItem(item)
        g_p_bank_name.addWidget(l_pension_bank_name)
        g_p_bank_name.addWidget(new_pension_bank_name)
        
        # pension account number
        g_p_account_number = QVBoxLayout()
        l_pension_account_number = QLabel('<i>Pension Account Number:</i>')
        new_pension_account_number = QLineEdit()
        # new_account_name.setValidator(QIntValidator)
        g_p_account_number.addWidget(l_pension_account_number)
        g_p_account_number.addWidget(new_pension_account_number)
        
        # pension details cont
        p_acct_cont = QHBoxLayout()
        p_acct_cont.addLayout(g_p_bank_name,1 )
        p_acct_cont.addLayout(g_p_account_number, 1)
        form_layout.addLayout(p_acct_cont)
        form_layout.addWidget(QWidget(), 5)
        
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
        g_from_date = QVBoxLayout()
        l_from_date = QLabel('<i>From Date:</i>')
        new_from_date = QDateEdit()
        g_from_date.addWidget(l_from_date)
        g_from_date.addWidget(new_from_date)        
        
        # to date
        g_to_date = QVBoxLayout()
        l_to_date = QLabel('<i>To Date:</i>')
        new_to_date = QLineEdit()
        g_to_date.addWidget(l_to_date)
        g_to_date.addWidget(new_to_date)
        
        # from date + to date
        f_t_date_cont = QHBoxLayout()
        f_t_date_cont.addLayout(g_from_date, 1)
        f_t_date_cont.addLayout(g_to_date, 1)
        form_layout.addLayout(f_t_date_cont)
        
        # comment
        l_comment = QLabel('<i>Comment:</i>')
        new_comment = QTextEdit()
        form_layout.addWidget(l_comment)
        form_layout.addWidget(new_comment)
        
        form_layout.addWidget(QWidget(), 5)
        
    
        submit_button = QPushButton('Submit')
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
     
 
    def job_tab(self):
        main_layout = QHBoxLayout(self.tab_job)
        
        # Form elements for edit
        l_layout = QVBoxLayout()     
           
        # job title
        g_job_title = QVBoxLayout()
        l_job_title = QLabel('<i>Job Title:</i>')
        new_job_title = QComboBox()
        for country in self.job_titles:
            item = country.get('title')
            if item:
                new_job_title.addItem(item)
        g_job_title.addWidget(l_job_title)
        g_job_title.addWidget(new_job_title)
        
        # Nature of Appointment
        g_NOA = QVBoxLayout()
        l_NOA = QLabel('<i>Nature Of Appointment:</i>')
        new_NOA = QComboBox()
        for nature in self.nature_of_appointment:
            item = nature.get('title')
            if item:
                new_NOA.addItem(item)
        g_NOA.addWidget(l_NOA)
        g_NOA.addWidget(new_NOA)
        
         # job designation
        g_job_designation = QVBoxLayout()
        l_job_designation = QLabel('<i>Job Designation:</i>')
        new_job_designation = QComboBox()
        for job in self.job_designation:
            item = job.get('name')
            if item:
                new_job_designation.addItem(item)
        g_job_designation.addWidget(l_job_designation)
        g_job_designation.addWidget(new_job_designation)     
        
        # job title + nature of NOA + job designation
        jt_noa_cont = QHBoxLayout()
        jt_noa_cont.addLayout(g_job_title, 3)
        jt_noa_cont.addLayout(g_NOA, 2)
        jt_noa_cont.addLayout(g_job_designation, 2)
        l_layout.addLayout(jt_noa_cont)
        
        
        # Employment Status
        g_employment_status = QVBoxLayout()
        l_employment_status = QLabel('<i>Employment Status:</i>')
        new_employment_status = QComboBox()
        for status in self.employment_status:
            item = status.get('name')
            if item:
                new_employment_status.addItem(item)
        g_employment_status.addWidget(l_employment_status)
        g_employment_status.addWidget(new_employment_status)     
        
        # Job Category
        g_job_category = QVBoxLayout()
        l_job_category = QLabel('<i>Job Category:</i>')
        new_job_category = QComboBox()
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_job_category.addItem(item)
        g_job_category.addWidget(l_job_category)
        g_job_category.addWidget(new_job_category)     
        
        # Grade level
        g_grade_level = QVBoxLayout()
        l_grade_level = QLabel('<i>Level:</i>')
        new_grade_level = QComboBox()
        new_grade_level.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_grade_level.addItem(item)
        g_grade_level.addWidget(l_grade_level)
        g_grade_level.addWidget(new_grade_level)  
        
        # employment status + job category + grade level
        jd_es_cont = QHBoxLayout()
        jd_es_cont.addLayout(g_employment_status, 2)
        jd_es_cont.addLayout(g_job_category, 2)
        jd_es_cont.addLayout(g_grade_level, 3)
        l_layout.addLayout(jd_es_cont)
        
        # Unit
        g_unit = QVBoxLayout()
        l_unit = QLabel('<i>Unit:</i>')
        new_unit = QComboBox()
        new_unit.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_unit.addItem(item)
        g_unit.addWidget(l_unit)
        g_unit.addWidget(new_unit)  
        
        # Sub Unit
        g_sub_unit = QVBoxLayout()
        l_sub_unit = QLabel('<i>Sub Unit:</i>')
        new_sub_unit = QComboBox()
        new_sub_unit.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_sub_unit.addItem(item)
        g_sub_unit.addWidget(l_sub_unit)
        g_sub_unit.addWidget(new_sub_unit)  
        
        # Location
        g_location = QVBoxLayout()
        l_location = QLabel('<i>Location:</i>')
        new_location = QComboBox()
        new_location.setEditable(True)
        for item in self.d_values:
            item = item.get('value')
            if item:
                new_location.addItem(item)
        g_location.addWidget(l_location)
        g_location.addWidget(new_location)  
        
        # Unit + Sub Unit + Location
        gl_u_su_cont = QHBoxLayout()
        gl_u_su_cont.addLayout(g_unit)
        gl_u_su_cont.addLayout(g_sub_unit)
        gl_u_su_cont.addLayout(g_location)
        l_layout.addLayout(gl_u_su_cont)
        
        
        # joined date
        g_joined_date = QVBoxLayout()
        l_joined_date = QLabel('<i>Joined Date:</i>')
        new_joined_date = QDateEdit()
        g_joined_date.addWidget(l_joined_date)
        g_joined_date.addWidget(new_joined_date)
        
         # start date
        g_start_date = QVBoxLayout()
        l_start_date = QLabel('<i>Start Date:</i>')
        new_start_date = QDateEdit()
        g_start_date.addWidget(l_start_date)
        g_start_date.addWidget(new_start_date)
        
         # end date
        g_end_date = QVBoxLayout()
        l_end_date = QLabel('<i>End Date:</i>')
        new_end_date = QDateEdit()
        g_end_date.addWidget(l_end_date)
        g_end_date.addWidget(new_end_date)
        
        # joined date + start date + end date
        l_jd_sd_ed_cont = QHBoxLayout()
        l_jd_sd_ed_cont.addLayout(g_joined_date, 1)
        l_jd_sd_ed_cont.addLayout(g_start_date, 1)
        l_jd_sd_ed_cont.addLayout(g_end_date, 1)
        l_layout.addLayout(l_jd_sd_ed_cont)
        
         # Pay Percentage
        g_p_pay = QVBoxLayout()
        l_p_pay = QLabel('<i>Percentage Pay:</i>')
        new_p_pay = QSpinBox()
        new_p_pay.setRange(0, 100)
        g_p_pay.addWidget(l_p_pay)
        g_p_pay.addWidget(new_p_pay)
        
         # Days
        g_day = QVBoxLayout()
        l_day = QLabel('<i>Day:(Total Days in a month)</i>')
        new_day = QSpinBox()
        new_day.setRange(0, 31)
        g_day.addWidget(l_day)
        g_day.addWidget(new_day)
        
         # Year Of Service
        g_year_of_service = QVBoxLayout()
        l_year_of_service = QLabel('<i>Year Of Service:</i>')
        new_year_of_service = QSpinBox()
        new_day.setRange(2000, 3000)
        g_year_of_service.addWidget(l_year_of_service)
        g_year_of_service.addWidget(new_year_of_service)
        
        # Percentage pay + Day + Year Of Service
        pp_d_yos_cont = QHBoxLayout()
        pp_d_yos_cont.addLayout(g_p_pay, 3)
        pp_d_yos_cont.addLayout(g_day, 2)
        pp_d_yos_cont.addLayout(g_year_of_service, 2)
        l_layout.addLayout(pp_d_yos_cont)
        
         # Comment
        g_comment = QVBoxLayout()
        l_comment = QLabel('<i>Comment:</i>')
        new_comment = QTextEdit()
        g_comment.addWidget(l_comment)
        g_comment.addWidget(new_comment)
        l_layout.addLayout(g_comment)
        
        l_layout.addWidget(QWidget(), 5)
    
        submit_button = QPushButton('Submit')
        main_layout.addLayout(l_layout)
        
        # main_layout.addWidget(submit_button)
     
    def salary_tab(self):
        main_layout = QHBoxLayout(self.tab_salary)
        
        # Form elements for edit
        l_layout = QVBoxLayout()    
        # Bank Salary
        cont_b_salary = QHBoxLayout()    
        l_b_salary = QLabel('<i>Bank Salary:</i>')
        b_salary = QLabel('<b>1234567</b>')
        cont_b_salary.addWidget(l_b_salary)
        cont_b_salary.addWidget(b_salary)
        l_layout.addLayout(cont_b_salary)
        
        # total allowance
        cont_t_allowance = QHBoxLayout()    
        l_t_allowance = QLabel('<i>Total Allowance:</i>')
        t_allowance = QLabel('<b>1234567</b>')
        cont_t_allowance.addWidget(l_t_allowance)
        cont_t_allowance.addWidget(t_allowance)
        l_layout.addLayout(cont_t_allowance)
        
        # total deduction
        cont_t_deduction = QHBoxLayout()    
        l_t_deduction = QLabel('<i>Total Deduction:</i>')
        t_deduction = QLabel('<b>1234567</b>')
        cont_t_deduction.addWidget(l_t_deduction)
        cont_t_deduction.addWidget(t_deduction)
        l_layout.addLayout(cont_t_deduction)     
        
        # Gross Pay
        cont_g_pay = QHBoxLayout()    
        l_g_pay = QLabel('<i>Gross Pay:</i>')
        g_pay = QLabel('<b>1234567</b>')
        cont_g_pay.addWidget(l_g_pay)
        cont_g_pay.addWidget(g_pay)
        l_layout.addLayout(cont_g_pay)
        
        # Net Pay
        cont_n_pay = QHBoxLayout()    
        l_n_pay = QLabel('<i>Net Pay:</i>')
        n_pay = QLabel('<b>1234567</b>')
        cont_n_pay.addWidget(l_n_pay)
        cont_n_pay.addWidget(n_pay)
        l_layout.addLayout(cont_n_pay)
        
        # Allowance Table
        l_layout.addWidget(QLabel("<b>Allowance Table</b>"))
        allowance_table = QTableWidget()
        allowance_table.setColumnCount(3)
        allowance_table.setRowCount(3)
        allowance_table.setHorizontalHeaderLabels(["Name", "Amount", 'three'])
        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                allowance_table.setItem(row, col, item)

        # Set size policies for table
        allowance_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        l_layout.addWidget(allowance_table)
        
        # Pay type
        cont_p_type = QHBoxLayout()    
        l_p_type = QLabel('<i>Pay Type:</i>')
        p_type = QComboBox()
        for item in self.d_values:
            item = item.get('value')
            if item:
                p_type.addItem(item)
        p_type.setEditable(True)
        cont_p_type.addWidget(l_p_type)
        cont_p_type.addWidget(p_type)
        l_layout.addLayout(cont_p_type)
        
        # Name/Description
        cont_n_desc = QHBoxLayout()  
        l_n_desc = QLabel('<i>Name/Descrition:</i>')
        n_desc = QComboBox()
        for name in self.d_values:
            name = name.get('value')
            if name:
                n_desc.addItem(name)
        n_desc.setEditable(True)
        cont_n_desc.addWidget(l_n_desc)
        cont_n_desc.addWidget(n_desc)
        l_layout.addLayout(cont_n_desc)
        
        # Amount
        cont_amount = QHBoxLayout()  
        l_amount = QLabel('<i>Amount:</i>')
        amount = QSpinBox()
        cont_amount.addWidget(l_amount)
        cont_amount.addWidget(amount)
        l_layout.addLayout(cont_amount)
        
        submit_button = QPushButton('Add Deduction/Allowance')
        l_layout.addWidget(submit_button)
        l_layout.addWidget(QWidget(), 5)
        
        # Right Layout
        r_layout = QVBoxLayout()
        
        # Total Earnings
        cont_t_earnings = QHBoxLayout()    
        l_t_earnings = QLabel('<i>Total Earnings:</i>')
        t_earnings = QLabel('<b>1234567</b>')
        cont_t_earnings.addWidget(l_t_earnings)
        cont_t_earnings.addWidget(t_earnings)
        r_layout.addLayout(cont_t_earnings)
        
        # Rent
        cont_rent = QHBoxLayout()    
        l_rent = QLabel('<i>Rent:</i>')
        rent = QLabel('<b>1234567</b>')
        cont_rent.addWidget(l_rent)
        cont_rent.addWidget(rent)
        r_layout.addLayout(cont_rent)
        
        # Peculiar
        cont_peculiar = QHBoxLayout()    
        l_peculiar = QLabel('<i>Peculiar:</i>')
        peculiar = QLabel('<b>1234567</b>')
        cont_peculiar.addWidget(l_peculiar)
        cont_peculiar.addWidget(peculiar)
        r_layout.addLayout(cont_peculiar)
        
        # Deduction Table
        r_layout.addWidget(QLabel("<b>Deduction Table</b>"))
        deduction_table = QTableWidget()
        deduction_table.setColumnCount(3)
        deduction_table.setRowCount(3)
        deduction_table.setHorizontalHeaderLabels(["Name", "Amount", 'three'])
        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                deduction_table.setItem(row, col, item)

        # Set size policies for table
        deduction_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        r_layout.addWidget(deduction_table)
        
         # Comment
        cont_comment = QVBoxLayout()    
        l_comment = QLabel('<i>Comment:</i>')
        comment = QTextEdit()
        cont_comment.addWidget(l_comment)
        cont_comment.addWidget(comment)
        r_layout.addLayout(cont_comment)
        
        comment_button = QPushButton("Submit Comment")
        r_layout.addWidget(comment_button)
        r_layout.addWidget(QWidget(), 5)
        
        main_layout.addLayout(l_layout)
        main_layout.addLayout(r_layout)
  

    def qualifications_tab(self):
        main_layout = QVBoxLayout(self.tab_qualifications)
        
        # Experience
        exp_layout = QHBoxLayout()
        exp_layout_l = QVBoxLayout()
        exp_layout_r = QVBoxLayout()
        
        exp_layout_l.addWidget(QLabel("<b>Experience</b>"))
        
        # Experience Table
        exp_table = QTableWidget()
        exp_table.setColumnCount(4)
        exp_table.setRowCount(3)
        exp_table.setHorizontalHeaderLabels(["Company Name", "Job Definition", 'From', 'To'])
        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                exp_table.setItem(row, col, item)

        # Set size policies for table
        exp_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        exp_layout_l.addWidget(exp_table)
        
        # Editable
        exp_layout_r.addWidget(QLabel("<b>Add New Experience</b>"))
        # company name
        cont_comp_name = QVBoxLayout()
        l_comp_name = QLabel("<i>Company Name:</i>")
        comp_name = QLineEdit()
        cont_comp_name.addWidget(l_comp_name)
        cont_comp_name.addWidget(comp_name)
        exp_layout_r.addLayout(cont_comp_name)
        
        # Job Title
        cont_job_title = QVBoxLayout()
        l_job_title = QLabel("<i>Job Title:</i>")
        job_title = QLineEdit()
        cont_job_title.addWidget(l_job_title)
        cont_job_title.addWidget(job_title)
        exp_layout_r.addLayout(cont_job_title)
        
         # From
        cont_from_date_exp = QVBoxLayout()
        l_from_date_exp = QLabel("<i>From Date:</i>")
        from_date_exp = QDateEdit()
        cont_from_date_exp.addWidget(l_from_date_exp)
        cont_from_date_exp.addWidget(from_date_exp)
        
         # To
        cont_to_date_exp = QVBoxLayout()
        l_to_date_exp = QLabel("<i>To Date:</i>")
        to_date_exp = QDateEdit()
        cont_to_date_exp.addWidget(l_to_date_exp)
        cont_to_date_exp.addWidget(to_date_exp)
        
         # Exp From - To
        cont_from_to_exp = QHBoxLayout()
        cont_from_to_exp.addLayout(cont_from_date_exp, 1)
        cont_from_to_exp.addLayout(cont_to_date_exp, 1)
        exp_layout_r.addLayout(cont_from_to_exp)
       
        # Comment
        cont_comment = QVBoxLayout()
        l_comment = QLabel("<i>Comment:</i>")
        comment = QLineEdit()
        cont_comment.addWidget(l_comment)
        cont_comment.addWidget(comment)
        exp_layout_r.addLayout(cont_comment)
        
        cont_buttons = QHBoxLayout()
        edit_button = QPushButton("Edit")
        save_button = QPushButton("Save")
        cont_buttons.addWidget(edit_button)
        cont_buttons.addWidget(save_button)
        exp_layout_r.addLayout(cont_buttons)
        
        # diplay on screen
        exp_layout.addLayout(exp_layout_l)
        exp_layout.addLayout(exp_layout_r)
        
        # Education Layout
        edu_layout = QHBoxLayout()
        edu_layout_l = QVBoxLayout()
        edu_layout_r = QVBoxLayout()
        
        edu_layout_l.addWidget(QLabel("<b>Education</b>"))
        
        # Education Table
        edu_table = QTableWidget()
        edu_table.setColumnCount(5)
        edu_table.setRowCount(3)
        edu_table.setHorizontalHeaderLabels(["Institution Name", "Major/Discipline","Year Of Certificate", "From", "To"])
        # Add sample data
        for row in range(3):
            for col in range(5):
                item = QTableWidgetItem(f"Sample Data {row+1}-{col+1}")
                edu_table.setItem(row, col, item)

        # Set size policies for table
        edu_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      
        # Add table to layout
        edu_layout_l.addWidget(edu_table)
        
        # Editable
        edu_layout_r.addWidget(QLabel("<b>Add New Education Qualification</b>"))
        
        # Institute
        g_institute = QVBoxLayout()
        l_institute = QLabel("<i>Institute:</i>")
        institute = QLineEdit()
        g_institute.addWidget(l_institute)
        g_institute.addWidget(institute)
        
         # major
        g_major = QVBoxLayout()
        l_major = QLabel("<i>Major / Specialization:</i>")
        major = QLineEdit()
        g_major.addWidget(l_major)
        g_major.addWidget(major)
        
        # institute + major
        i_m_cont = QHBoxLayout()
        i_m_cont.addLayout(g_institute, 1)
        i_m_cont.addLayout(g_major, 1)
        edu_layout_r.addLayout(i_m_cont)
        
         # Year
        g_year = QVBoxLayout()
        l_year = QLabel("<i>Year:</i>")
        year = QSpinBox()
        year.setRange(1000, 4000)
        g_year.addWidget(l_year)
        g_year.addWidget(year)

         # gpa
        g_gpa = QVBoxLayout()
        l_gpa = QLabel("<i>G.P.A:</i>")
        gpa = QLineEdit()
        g_gpa.addWidget(l_gpa)
        g_gpa.addWidget(gpa)
        
        # Level
        g_level = QVBoxLayout()
        l_level = QLabel("<i>Level:</i>")
        c_level = QComboBox()
        for item in self.d_values:
            item = item.get('value')
            if item:
                c_level.addItem(item)
        c_level.setEditable(True)
        g_level.addWidget(l_level)
        g_level.addWidget(c_level)
        
        # Year + GPA + Level
        cont_year_gpa = QHBoxLayout()
        cont_year_gpa.addLayout(g_year, 1)
        cont_year_gpa.addLayout(g_gpa, 1)
        cont_year_gpa.addLayout(g_level, 1)
        edu_layout_r.addLayout(cont_year_gpa)
        
         # From
        cont_from_date_edu = QVBoxLayout()
        l_from_date_edu = QLabel("<i>From Date:</i>")
        from_date_edu = QDateEdit()
        cont_from_date_edu.addWidget(l_from_date_edu)
        cont_from_date_edu.addWidget(from_date_edu)
        
         # To
        cont_to_date_edu = QVBoxLayout()
        l_to_date_edu = QLabel("<i>To Date:</i>")
        to_date_edu = QDateEdit()
        cont_to_date_edu.addWidget(l_to_date_edu)
        cont_to_date_edu.addWidget(to_date_edu)
        
         # Edu From - To
        cont_from_to_edu = QHBoxLayout()
        cont_from_to_edu.addLayout(cont_from_date_edu, 1)
        cont_from_to_edu.addLayout(cont_to_date_edu, 1)
        edu_layout_r.addLayout(cont_from_to_edu)
        
        cont_buttons = QHBoxLayout()
        edit_button = QPushButton("Edit")
        save_button = QPushButton("Save")
        cont_buttons.addWidget(edit_button)
        cont_buttons.addWidget(save_button)
        edu_layout_r.addLayout(cont_buttons)
        
        edu_layout.setSizeConstraint
        edu_layout_l.addWidget(QWidget(), 5)
        edu_layout_r.addWidget(QWidget(), 5)
        # diplay on screen
        edu_layout.addLayout(edu_layout_l)
        edu_layout.addLayout(edu_layout_r)
        
        main_layout.addLayout(exp_layout)
        main_layout.addLayout(edu_layout)
    