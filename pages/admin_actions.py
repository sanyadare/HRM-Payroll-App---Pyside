from PySide6.QtWidgets import QTabWidget, QWidget, QFormLayout, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton

class AdminActions(QTabWidget):
    def __init__(self):
        super().__init__()

        # Create three tabs
        self.tab_send_slips = QWidget()
        self.tab_bulk_transaction = QWidget()
        self.tab_new_user = QWidget()

        # Add tabs to the SalarySetup widget
        self.addTab(self.tab_send_slips, "Send Slips To All Staff")
        self.addTab(self.tab_bulk_transaction, "Input Bulk Transactions")
        
   
        # Setup tab content
        self.send_slips_tab()
        self.bulk_transaction_tab()
       
      

    def send_slips_tab(self):
        layout = QVBoxLayout()

    def bulk_transaction_tab(self):
        # Similar setup as the allowance tab
        pass

  
    