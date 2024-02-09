

LIGHT_GREEN_MODE_STYLESHEET = """
    /* Light Mode Styles */
    QMainWindow {
        background-color: #FFFFFF; /* Window background color */
        color: #000000; /* Text color */
    }
    
    QMenuBar {
        background-color: #EAEAEA; /* Menu bar background color */
        color: #333333; /* Menu text color */ 
    }
    
    QTabWidget {
        background-color: #FFFFFF; /* Menu bar background color */
        color: #000000; /* Menu text color */ 
        margin: 20px;
    }
    
    QTabBar::tab {
        background-color: #FFFFFF;
        color: #000000;
        height: 25px;
        padding: 5px;
    }
    
    QTabBar::tab:selected {
        background-color: lightgray;
        font-weight: bold;
    }
    
    QTabBar::tab:hover {
        background-color: lightgray;
    }
    
    QDialog {
        background-color: #FFFFFF; /* Menu bar background color */
        color: #000000; /* Menu text color */ 
        margin: 20px;
    }
    
    
    QMenuBar::item:selected {
        background-color: #089811; /* Selected menu item background color */
        border-radius: 5px;
        color: white;
    }
    
    QMenu {
        background-color: #EAEAEA; /* Submenu background color */
        color: #333333; /* Submenu text color */
    }
    
    QMenu::item:selected {
        color: white;
        background-color: #089811; /* Selected submenu item background color */
    }
    
    QToolBar {
        background-color: #EAEAEA; /* Toolbar background color */
    }
    
    QPushButton {
        background-color: #089811; /* Button background color */
        color: #FFFFFF; /* Button text color */
        border: 1px solid #089811; /* Button border color */
        border-radius: 10px;
        padding: 5px 10px;
        font-size: 14px;
        font-weight: bold;
    }
    
    QIcon {
        color: white;
        background-color: white;
        border-color: white;
        
    }
    
    QLineEdit, QTextEdit, QComboBox, QSpinBox, QDateEdit {
        border: 1px solid #000; /* Button border color */
        border-radius: 5px;
        padding: 5px;
    }
    
    QComboBox:focus, QSpinBox:focus, QLineEdit:focus, QDateEdit:focus, QTextEdit:focus {
        border: 1px solid #089811; /* Button border color */
        
    }
    
    QPushButton:hover {
        background-color: #0FCC1C; /* Button background color on hover */
    }
    
    QStatusBar {
        background-color: #EAEAEA; /* Status bar background color */
        color: #333333; /* Status bar text color */
    }
    
    QLabel {
        color: #000
    }
    
    QLabel#form_label {
        # font-weight: bold;
        color: red;
    }
"""


LIGHT_BLUE_MODE_STYLESHEET = """
    /* Light Mode Styles */
    QMainWindow {
        background-color: #FFFFFF; /* Window background color */
        color: #000000; /* Text color */
    }
    
    QMenuBar {
        background-color: #EAEAEA; /* Menu bar background color */
        color: #333333; /* Menu text color */ 
    }
    
    QTabWidget {
        background-color: #FFFFFF; /* Menu bar background color */
        color: #000000; /* Menu text color */ 
        margin: 20px;
    }
    
    QTabBar::tab {
        background-color: #FFFFFF;
        color: #000000;
        height: 25px;
        padding: 5px;
    }
    
    QTabBar::tab:selected {
        background-color: lightgray;
        font-weight: bold;
    }
    
    QTabBar::tab:hover {
        background-color: lightgray;
    }
    
    QDialog {
        background-color: #FFFFFF; /* Menu bar background color */
        color: #000000; /* Menu text color */ 
        margin: 20px;
    }
    
    QMenuBar::item:selected {
        background-color: #1C08CC; /* Selected menu item background color */
        border-radius: 5px;
        color: white;
    }
    
    QMenu {
        background-color: #EAEAEA; /* Submenu background color */
        color: #333333; /* Submenu text color */
    }
    
    QMenu::item:selected {
        color: white;
        background-color: #1C08CC; /* Selected submenu item background color */
    }
    
    QToolBar {
        background-color: #EAEAEA; /* Toolbar background color */
    }
    
    QPushButton {
        background-color: #1C08CC; /* Button background color */
        color: #FFFFFF; /* Button text color */
        border: 1px solid #1C08CC; /* Button border color */
        border-radius: 10px;
        padding: 5px 10px;
        font-size: 14px;
        font-weight: bold;
    }
    
    QIcon {
        color: #FFFFFF;
    }
    
    QComboBox, QSpinBox, QDateEdit, QLineEdit, QTextEdit {
        border: 1px solid #000; /* Button border color */
        border-radius: 5px;
        padding: 5px;
    }
    
    QComboBox:focus, QSpinBox:focus, QLineEdit:focus, QDateEdit:focus, QTextEdit:focus {
        border: 1px solid #1C08CC; /* Button border color */
    }
    
    QPushButton:hover {
        background-color: #2812E8; /* Button background color on hover */
    } 
    
    QStatusBar {
        background-color: #EAEAEA; /* Status bar background color */
        color: #333333; /* Status bar text color */
    }
    
    QLabel {
        color: #000
    }
    
    QLabel#form_label {
        # font-weight: bold;
        color: red;
    }
"""


DARK_MODE_STYLESHEET = """
    /* Dark Mode Styles */
    QMainWindow {
        background-color: #121212; /* Window background color */
        color: #FFFFFF; /* Text color */
    }
  
    QMenuBar {
        background-color: #333333; /* Menu bar background color */
        color: #CCCCCC; /* Menu text color */
    }
    
    QTabWidget {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
        margin: 20px;
    }
    
    QTabBar::tab {
        background-color: #333333;
        color: #FFFFFF;
        height: 25px;
        padding: 5px;
    }
      
    QTabBar::tab:selected {
        background-color: gray; /* Window background color */
        color: #FFFFFF; /* Text color */
        font-weight: bold;
    }
    
    QTabBar::tab:hover {
        background-color: lightgray
    }
    
    QDialog {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
        margin: 20px;
    }
    
    QWidget {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
       
    }
    
    QMenu {
        background-color: #333333; /* Submenu background color */
        color: #CCCCCC; /* Submenu text color */
    }
    
    QMenuBar::item:selected {
        background-color: #555555; /* Selected menu item background color */
    }
    
    QMenu::item:selected {
        background-color: #555555; /* Selected submenu item background color */
    }
    
    QToolBar {
        background-color: #333333; /* Toolbar background color */
    }
    
    QPushButton {
        background-color: #555555; /* Button background color */
        color: #FFFFFF; /* Button text color */
        border: 1px solid #444444; /* Button border color */
        border-radius: 5px;
        padding: 5px 10px;
        font-size: 14px;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #444444; /* Button background color on hover */
    }
    
    QIcon {
        background-color: #444444;
    }
    
    QLineEdit, QComboBox, QSpinBox, QTextEdit, QDateEdit {
        border: 1px solid #444444; /* Button border color */
        border-radius: 5px;
        padding: 5px;
    }
    
    QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus, QDateEdit:focus {
        border: 1px solid #fff; /* Button border color */
        
    }
    
    QLabel {
        color: #fff;
    }
    
    QStatusBar {
        background-color: #333333; /* Status bar background color */
        color: #CCCCCC; /* Status bar text color */
    }
    
    QHeaderView::section {
        background-color: #333333; /* Status bar background color */
        color: #CCCCCC; /* Status bar text color */
        font-weight: bold;
    }
"""


DARK_GREEN_MODE_STYLESHEET = """
    /* Dark Mode Styles */
    QMainWindow {
        background-color: #121212; /* Window background color */
        color: #FFFFFF; /* Text color */
    }
  
    QMenuBar {
        background-color: #333333; /* Menu bar background color */
        color: #CCCCCC; /* Menu text color */
    }
    
    QTabWidget {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
        margin: 20px;
    }
    
    QTabBar::tab {
        background-color: #333333;
        color: #FFFFFF;
        height: 25px;
        padding: 5px;
    }
      
    QTabBar::tab:selected {
        background-color: lightgray; /* Window background color */
        color: #333333; /* Text color */
        font-weight: bold;
    }
    
    QTabBar::tab:hover {
        background-color: gray;
    }
    
    QDialog {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
        margin: 20px;
    }
    
    QWidget {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
    }
    
    QMenu {
        background-color: #333333; /* Submenu background color */
        color: #CCCCCC; /* Submenu text color */
    }
    
    QMenuBar::item:selected {
        background-color: #089811; /* Selected menu item background color */
    }
    
    QMenu::item:selected {
        background-color: #089811; /* Selected submenu item background color */
    }
    
    QToolBar {
        background-color: #333333; /* Toolbar background color */
    }
    
    QPushButton {
        background-color: #089811; /* Button background color */
        color: #FFFFFF; /* Button text color */
        border: 1px solid #089811; /* Button border color */
        border-radius: 10px;
        padding: 5px 10px;
        font-size: 14px;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #0FCC1C; /* Button background color on hover */
    }
    
    QIcon {
        background-color: #089811;
    }
    
    QLineEdit, QComboBox, QSpinBox, QTextEdit, QDateEdit {
        border: 1px solid gray; /* Button border color */
        border-radius: 5px;
        padding: 5px;
    }
    
    QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus, QDateEdit:focus {
        border: 1px solid #089811; /* Button border color */
        
    }
    
    QLabel {
        color: #fff;
    }
    
    QStatusBar {
        background-color: #333333; /* Status bar background color */
        color: #CCCCCC; /* Status bar text color */
    }
    
    QHeaderView::section {
        background-color: #333333; /* Status bar background color */
        color: #CCCCCC; /* Status bar text color */
        font-weight: bold;
    }
"""



DARK_BLUE_MODE_STYLESHEET = """
    /* Dark Mode Styles */
    QMainWindow {
        background-color: #121212; /* Window background color */
        color: #FFFFFF; /* Text color */
        font-size: 20px;
    }
  
    QMenuBar {
        background-color: #333333; /* Menu bar background color */
        color: #CCCCCC; /* Menu text color */
    }
    
    QTabWidget {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
        margin: 20px;
    }
    
    QTabBar::tab {
        background-color: #333333;
        color: #FFFFFF;
        height: 25px;
        padding: 5px;
    }
      
    QTabBar::tab:selected {
        background-color: lightgray; /* Window background color */
        color: #333333; /* Text color */
        font-weight: bold;
    }
    
    QTabBar::tab:hover {
        background-color: gray
    }
    
    QDialog {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
        margin: 20px;
    }
    
    QWidget {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
    }
    
    QMenu {
        background-color: #333333; /* Submenu background color */
        color: #CCCCCC; /* Submenu text color */
    }
    
    QMenuBar::item:selected {
        background-color: #0E0468; /* Selected menu item background color */
    }
    
    QMenu::item:selected {
        background-color: #0E0468; /* Selected submenu item background color */
    }
    
    QToolBar {
        background-color: #333333; /* Toolbar background color */
    }
    
    QPushButton {
        background-color: #0E0468; /* Button background color */
        color: #FFFFFF; /* Button text color */
        border: 1px solid #0E0468; /* Button border color */
        border-radius: 10px;
        padding: 5px 10px;
        font-size: 14px;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #06022B; /* Button background color on hover */
    }
    
    QIcon {
        background-color: #0E0468;
    }
    
    QLineEdit, QComboBox, QSpinBox, QTextEdit, QDateEdit {
        border: 1px solid #444444; /* Button border color */
        border-radius: 5px;
        padding: 5px;
    }
    
    QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus, QDateEdit:focus {
        border: 1px solid #0E0468; /* Button border color */
        
    }
    
    QLabel {
        color: #fff;
    }
    
    QStatusBar {
        background-color: #333333; /* Status bar background color */
        color: #CCCCCC; /* Status bar text color */
    }
    
    QHeaderView::section {
        background-color: #333333; /* Status bar background color */
        color: #CCCCCC; /* Status bar text color */
        font-weight: bold;
    }
"""


