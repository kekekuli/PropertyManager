from modules.UI.UI_resourse import errorUI
from PyQt5.QtWidgets import QMainWindow

class error:
    def __init__(self):
        self.ui = errorUI.Ui_Form()
        self.window = QMainWindow()
        self.ui.setupUi(self.window)

        self.ui.ensure.clicked.connect(self.close)
        return
    def show(self):
        self.window.show()
        return
    def set_message(self, str):
        self.ui.message.setText(str)

    def close(self):
        self.window.close()
        del self
        return