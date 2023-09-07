# used for change self infomatino
from modules.UI.UI_resourse import selfinfoUI
from PyQt5.QtWidgets import QMainWindow
from modules import global_vars
class selfinfo:
    def __init__(self):
        self.ui = selfinfoUI.Ui_Form()
        self.window = QMainWindow()
        self.window.setWindowTitle("self info change")
        self.ui.setupUi(self.window)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)
        return
    def show(self):
        self.window.show()
        return
    def close(self):
        self.window.close()
        global_vars.window_list['selfinfo'] = None
        del self
        return
    def submit(self):
        pass
    def addChild(self, child):
        self.childs.append(child)