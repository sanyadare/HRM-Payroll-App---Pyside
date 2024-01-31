from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Dashboard(QWidget):
    def __init__(self, username='admin', date=None):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.setGeometry(300, 300, 400, 200)

        self.all_labels = []
        self.username = QLabel(username)
        self.date = QLabel(date)
        # self.date.name
        self.all_labels.append({'label':'self.username', 
                                'text':self.username})
        self.all_labels.append({'label':'self.date', 
                                'text':self.date})
        self.init_ui(username, date)

    def init_ui(self, username, date):
        layout = QVBoxLayout()

        welcome_label = QLabel(f"Hello, {username}!")
        date_label = QLabel(f"Date, {date}")
        layout.addWidget(date_label)
        layout.addWidget(welcome_label)

        self.setLayout(layout)
    
    def change_labels(self, label, new_text):
        # for _label in self.all_labels:
        #     print(_label.get('label'))
            
        for _label in self.all_labels:
            if label ==_label.get(label):
                _label['text'].setText(new_text)
                
    def change_date_label(self, new_text):
        self.date.setText(new_text)
        self.update()
        return self.date