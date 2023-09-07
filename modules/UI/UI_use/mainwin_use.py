# A main window used for test communicate between windows
from modules.UI.UI_resourse import mainwinUI
from PyQt5.QtWidgets import QMainWindow
from modules.managers import manager
from modules import global_vars

class mainwin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = mainwinUI.Ui_Form()
        self.setWindowTitle("Main window")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.test1.clicked.connect(self.show_signin)
        self.ui.test2.clicked.connect(self.show_signup)
        self.ui.test3.clicked.connect(self.show_queryfee)
        self.ui.test4.clicked.connect(self.show_selfinfo)

    def show_signin(self):
        signin = manager.manager.ui_manager.create_signin()
        self.addChild(signin)
        signin.signinStatus.connect(self.accept_msg)
        signin.show()
    def show_signup(self):
        signup = manager.manager.ui_manager.create_signup()
        self.addChild(signup)
        signup.show()
    def show_queryfee(self):
        queryfee = manager.manager.ui_manager.create_queryfee()
        self.addChild(queryfee)
        queryfee.show()
    def show_selfinfo(self):
        selfinfo = manager.manager.ui_manager.create_selfinfo()
        self.addChild(selfinfo)
        selfinfo.show()
    def addChild(self, child):
        self.childs.append(child)
    def close(self):
        self.close()
        global_vars.window_list['mainwin'] = None
        del self
    def accept_msg(self, house_id):
        print(house_id)