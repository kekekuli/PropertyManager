from modules.UI.UI_resourse import errorUI
from PyQt5.QtWidgets import QWidget

class error(QWidget):
    def __init__(self, parent=None, msg="Default", fontSize=16):
        super().__init__(parent)
        self.ui = errorUI.Ui_Form()
        self.setWindowTitle('error')
        self.ui.setupUi(self)

        self.ui.ensure.clicked.connect(self.close)

        self.set_message(msg)
        self.set_size(fontSize)
        return
    def set_message(self, str):
        self.ui.message.setText(str)
    def set_size(self, size):
        font = self.ui.message.font()
        font.setPointSize(size)
        self.ui.message.setFont(font)
    def close(self):
        super().close()
        del self
    def closeEvent(self, event):
        self.close()