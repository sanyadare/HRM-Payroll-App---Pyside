from PySide6.QtWidgets import QTabWidget, QWidget, QFormLayout, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton

class Reports(QTabWidget):
    def __init__(self):
        super().__init__()

        # Create three tabs
        self.report_1 = QWidget()
        self.report_2 = QWidget()
        self.report_3 = QWidget()
        self.report_4 = QWidget()
        self.report_5 = QWidget()
        self.report_6 = QWidget()
        self.report_7 = QWidget()

        # Add tabs to the SalarySetup widget
        self.addTab(self.report_1, "Report One")
        self.addTab(self.report_2, "Report Two")
        self.addTab(self.report_3, "Report Three")
        self.addTab(self.report_4, "Report Four")
        self.addTab(self.report_5, "Report Five")
        self.addTab(self.report_6, "Report Six")
        self.addTab(self.report_7, "Report Seven")

        # Setup tab content
        self.report_1_tab()
        self.report_2_tab()
        self.report_3_tab()
        self.report_4_tab()
        self.report_5_tab()
        self.report_6_tab()
        self.report_7_tab()
        

    def report_1_tab(self):
        layout = QVBoxLayout(self.report_1)

    def report_2_tab(self):
        # Similar setup as the allowance tab
        pass

    def report_3_tab(self):
        # Similar setup as the allowance tab
        pass
    
    def report_4_tab(self):
        # Similar setup as the allowance tab
        pass
    
    def report_5_tab(self):
        # Similar setup as the allowance tab
        pass
    
    def report_6_tab(self):
        # Similar setup as the allowance tab
        pass
    
    def report_7_tab(self):
        # Similar setup as the allowance tab
        pass
