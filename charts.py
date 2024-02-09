
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class BarChart(QWidget):
    def __init__(self, title='My Bar Chart', x_values=[], y_values=[], x_label='', y_label=''):
        super().__init__()
        layout = QVBoxLayout()

        # Create Matplotlib figure and axes
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Plot the data
        ax.bar(x_values, y_values)

        # Add labels and title
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        fig.patch.set_facecolor((0.8, 0.8, 0.8, 0.5))
        # Embed the chart in the page
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

        self.setLayout(layout)


class LineGraph(QWidget):
    def __init__(self, title='My Line Graph', x_values=[], y_values=[], x_label='', y_label=''):
        super().__init__()
        layout = QVBoxLayout()

        # Create Matplotlib figure and axes
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Plot the data
        ax.plot(x_values, y_values)

        # Add labels and title
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        fig.patch.set_facecolor((0.8, 0.8, 0.8, 0.5))
        # fig.patch.set_edgecolor('black')
        # fig.patch.set_linewidth(2)
        # Embed the chart in the page
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

        self.setLayout(layout)


class PieChart(QWidget):
    def __init__(self, title='My Pie Cahrt', x_values=[], y_values=[], x_label='', y_label=''):
        super().__init__()
        
        layout = QVBoxLayout()

        # Create Matplotlib figure and axes
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Plot the data
        ax.pie(x_values, y_values)

        # Add labels and title
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        fig.patch.set_facecolor((0.8, 0.8, 0.8, 0.3))
        # fig.patch.set_edgecolor('black')
        # fig.patch.set_linewidth(2)
        # Embed the chart in the page
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

        self.setLayout(layout)