# used for change self infomatino
from modules.UI.UI_resourse import selfinfoUI
from PyQt5.QtWidgets import QMainWindow
from modules import global_vars
class selfinfo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = selfinfoUI.Ui_Form()
        self.setWindowTitle("self info change")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)
        return
    def close(self):
        self.close()
        global_vars.window_list['selfinfo'] = None
        del self
        return
    def submit(self):
        pass
    def addChild(self, child):
        self.childs.append(child)