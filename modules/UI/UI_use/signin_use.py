from modules.UI.UI_resourse import signinUI
from PyQt5.QtWidgets import QMainWindow
from modules import global_vars
from modules.managers import manager
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
class signin(QMainWindow):
    # if signin success, emit house_id, other emit -1
    signinStatus = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = signinUI.Ui_Form()
        self.setWindowTitle("signin")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)

    def get_datas(self):
        datas = {}
        datas['house_id'] = self.ui.house_id.text()
        datas['password'] = self.ui.password.text()
        try:
            int(datas['house_id'])
        except ValueError as e:
            _error = manager.manager.ui_manager.create_error()
            _error.set_message("数值有误")
            self.addChild(_error)
            _error.show()
        return datas
    def submit(self):
        datas = self.get_datas()
        result = manager.manager.account_manager.signin_auth(datas['house_id'], datas['password']);
        if result == 0:
            self.signinStatus.emit(-1)
            _error = manager.manager.ui_manager.create_error()
            _error.set_message("登陆失败")
            self.addChild(_error)
            _error.show()
        else:
            self.signinStatus.emit(int(datas['house_id']))
            _error = manager.manager.ui_manager.create_error()
            _error.set_message("登陆成功")
            self.addChild(_error)
            _error.show()
            self.close()
        return
    def addChild(self, child):
        self.childs.append(child)
        return
    def close(self):
        print("try to close signin")
        super().close()
        global_vars.window_list['signin'] = None
        del self