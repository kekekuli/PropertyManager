from modules.UI.UI_resourse import signinUI
from PyQt5.QtWidgets import QMainWindow
from modules import global_vars
from modules.managers import manager
class signin:
    def __init__(self):
        self.ui = signinUI.Ui_Form()
        self.window = QMainWindow()
        self.window.setWindowTitle("signin")
        self.ui.setupUi(self.window)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)


    def show(self):
        self.window.show()
        return
    def close(self):
        self.window.close()
        del self
        global_vars.window_list['signin'] = None
        return
    def get_datas(self):
        datas = {}
        datas['house_id'] = self.ui.house_id.text()
        datas['password'] = self.ui.password.text()

        return datas
    def submit(self):
        datas = self.get_datas()
        result = manager.manager.database_manager.signin_auth(datas['house_id'], datas['password']);
        return (datas['house_id'], result)

    def addChild(self, child):
        self.childs.append(child)
        return