from modules.UI.UI_resourse import signinUI
from PyQt5.QtWidgets import QWidget
from modules import global_vars
from modules.managers import manager
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
class signin(QWidget):
    # if signin success, emit house_id, other emit -1
    signStatus = QtCore.pyqtSignal(int, str)

    # default signin as common user
    def __init__(self, parent=None):
        super().__init__(parent)

        self.signType = global_vars.user

        self.ui = signinUI.Ui_Form()
        self.setWindowTitle("signin")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)

        self.ui.userCheck.setChecked(True)

        self.ui.userCheck.clicked.connect(self.user_trigger)
        self.ui.adminCheck.clicked.connect(self.admin_trigger)

    def get_datas(self):
        datas = {}
        datas['house_id'] = self.ui.house_id.text()
        datas['password'] = self.ui.password.text()
        try:
            int(datas['house_id'])
        except ValueError as e:
            _error = manager.manager.ui_manager.create_error(tip="数值有误")
            self.addChild(_error)
            _error.show()
        return datas
    def submit(self):
        datas = self.get_datas()
        result = manager.manager.account_manager.signin_auth(datas['house_id'], datas['password'], self.signType);
        if result == 0:
            _error = manager.manager.ui_manager.create_error(tip="登陆失败")
            self.addChild(_error)
            _error.show()
        else:
            self.signStatus.emit(int(datas['house_id']), self.signType)
            _error = manager.manager.ui_manager.create_error(tip="登陆成功")
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

        manager.manager.ui_manager.require_set_default()

    def closeEvent(self, event):
        self.close()

    def user_trigger(self):
        self.ui.userCheck.setChecked(True)
        self.ui.adminCheck.setChecked(False)

        self.signType = global_vars.user
    def admin_trigger(self):
        self.ui.userCheck.setChecked(False)
        self.ui.adminCheck.setChecked(True)

        self.signType = global_vars.admin
    def show(self):
        manager.manager.ui_manager.require_set_self(self, "登陆")
