

LIGHT_MODE_STYLESHEET = """
    /* Light Mode Styles */
    QMainWindow {
        background-color: #FFFFFF; /* Window background color */
        color: #000000; /* Text color */
        font-size: 20px;
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
    
    
    QMenuBar::item:selected {
        background-color: #BDBDBD; /* Selected menu item background color */
        border-radius: 5px;
    }
    
    QMenu {
        background-color: #EAEAEA; /* Submenu background color */
        color: #333333; /* Submenu text color */
    }
    
    QMenu::item:selected {
        background-color: #BDBDBD; /* Selected submenu item background color */
    }
    
    QToolBar {
        background-color: #EAEAEA; /* Toolbar background color */
    }
    
    QPushButton {
        background-color: #4CAF50; /* Button background color */
        color: #FFFFFF; /* Button text color */
        border: 1px solid #45A049; /* Button border color */
        border-radius: 10px;
        padding: 5px 10px;
        font-size: 14px;
    }
    
    QIcon {
        background-color: #FFFFFF;
        
    }
    
    QLineEdit {
        border: 1px solid #000; /* Button border color */
        border-radius: 10px;
        padding: 5px;
    }
    
    QLineEdit:focus {
        border: 1px solid #45A049; /* Button border color */
    }
    
    QPushButton:hover {
        background-color: #45A049; /* Button background color on hover */
        
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
    
    QTabWidget::item:selected {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
    }
    
    QDialog {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
    }
    
    QWidget {
        background-color: #333333; /* Window background color */
        color: #FFFFFF; /* Text color */
    }
    
    QMenuBar {
        background-color: #333333; /* Menu bar background color */
        color: #CCCCCC; /* Menu text color */
    }
    
    QMenuBar::item:selected {
        background-color: #555555; /* Selected menu item background color */
    }
    
    QMenu {
        background-color: #333333; /* Submenu background color */
        color: #CCCCCC; /* Submenu text color */
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
        padding: 5px 10px;
    }
    
    QPushButton:hover {
        background-color: #444444; /* Button background color on hover */
    }
    
    QStatusBar {
        background-color: #333333; /* Status bar background color */
        color: #CCCCCC; /* Status bar text color */
    }
"""

