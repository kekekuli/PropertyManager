from modules.UI.UI_resourse import queryfeeUI
from PyQt5.QtWidgets import QMainWindow

class queryfee:
    def __init__(self):
        self.ui = queryfeeUI.Ui_Form()
        self.window = QMainWindow()
        self.window.setWindowTitle("query fee")
        self.ui.setupUi(self.window)

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)

    def submit(self):
        pass
    def close(self):
        pass
    def show(self):
        pass
    def display_datas(self, datas):
        pass

