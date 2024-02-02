from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from charts import BarChart, PieChart, LineGraph
class Dashboard(QWidget):
    def __init__(self, username='admin', date=None):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.setGeometry(300, 300, 400, 200)

        # self.show_greeting()
        self.all_labels = []
        self.username = username
        self.date = date
        self.init_ui()

    def show_charts(self):
        chart_layout = QHBoxLayout()
        categories = [2,3,4,6,7]
        values = [10, 20, 15, 25, 30]
        bar_chart = BarChart(title='My Bar Chart',y_label='values', y_values=values, x_label='categories', x_values=categories )
        line_chart = LineGraph(y_label='values', y_values=values, x_label='categories', x_values=categories )
        line_chart_2 = LineGraph(y_label='values', y_values=values, x_label='categories', x_values=categories )
        
        chart_layout.addWidget(line_chart)
        chart_layout.addWidget(bar_chart)
        chart_layout.addWidget(line_chart_2)
        
        return chart_layout
    
    def show_greeting(self, username, date):
        main_layout = QHBoxLayout()
        
        main_layout.addWidget(QLabel("<b style='font-size:25px;'>DASHBOARD</b>"))
        main_layout.addWidget(QWidget(), 4)
        
        layout = QVBoxLayout()
        welcome_label = QLabel(f"<b style='font-size:20px;'>Hello, {username.upper()}!</b>")
        layout.addWidget(welcome_label)
        date_label = QLabel(f"Date, {date}")
        # layout.addWidget(date_label)
        main_layout.addLayout(layout, 1)
        return main_layout
        
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.show_greeting(username=self.username, date=self.date),1)
        main_layout.addLayout(self.show_charts())
        
        main_layout.addWidget(QWidget(), 3)

        self.setLayout(main_layout)
    
