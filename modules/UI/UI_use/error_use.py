from modules.UI.UI_resourse import errorUI
from PyQt5.QtWidgets import QMainWindow

class error(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = errorUI.Ui_Form()
        self.setWindowTitle('error')
        self.ui.setupUi(self)

        self.ui.ensure.clicked.connect(self.close)
        return
    def set_message(self, str):
        self.ui.message.setText(str)
    def set_size(self, size):
        font = self.font()
        font.setPointSize(size)
        self.ui.message.setFont(font)