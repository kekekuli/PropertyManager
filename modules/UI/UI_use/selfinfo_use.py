# used for change self infomatino
from modules.UI.UI_resourse import selfinfoUI
from PyQt5.QtWidgets import QWidget
from modules.managers import manager
from modules import global_vars
class selfinfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = selfinfoUI.Ui_Form()
        self.setWindowTitle("self info change")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)

        self.read_signin_statu()
        return
    def submit(self):
        datas = self.get_datas()
        flag = self.parse_datas(datas)
        if flag != -1:
            result = manager.manager.account_manager.update_selfinfo(datas)
            # Success
            if result != 0:
                _error = manager.manager.ui_manager.create_error(tip="修改成功，请重新登陆", size=10)
                self.addChild(_error)
                _error.show()

                manager.manager.logout()
                self.close()
            # Failed
            else:
                _error = manager.manager.ui_manager.create_error(tip="修改失败")
                self.addChild(_error)
                _error.show()
        else:
            _error = manager.manager.ui_manager.create_error(tip="修改失败")
            self.addChild(_error)
            _error.show()
    def addChild(self, child):
        self.childs.append(child)
    # read saved signin statu to change title
    def read_signin_statu(self):
        signinID = manager.manager.get_signinID()
        datas = manager.manager.account_manager.get_household(signinID)
        msg = "尊敬的{}号住户业主{}，选择你要更改的信息".format(datas['house_id'], datas['name'])
        self.ui.canva.setText(msg)
        self.ui.name.setText(datas['name'])
        self.ui.password.setText(datas['password'])
        self.ui.phone.setText(datas['phone'])
        self.ui.gender.setCurrentText(datas['gender'])
        self.ui.profession.setCurrentText(datas['profession'])
        self.ui.population.setValue(datas['population'])
    def get_datas(self):
        datas = {}
        datas['name'] = self.ui.name.text()
        datas['password'] = self.ui.password.text()
        datas['phone'] = self.ui.phone.text()
        datas['gender'] = self.ui.gender.currentText()
        datas['profession'] = self.ui.profession.currentText()
        datas['population'] = self.ui.population.value()
        print(datas)
        return datas
    def parse_datas(self, datas):
        try:
            data = datas['phone']
            for ch in data:
                if ch < '0' or ch > '9':
                    raise ValueError('非法字符')
            datas['population'] = int(datas['population'])
            if len(datas['name']) == 0 or len(datas['password']) == 0 or \
                len(datas['gender']) == 0 or len(datas['profession']) == 0:
                    raise ValueError("长度有误")
            return 0
        except ValueError as ve:
            _error = manager.manager.ui_manager.create_error(tip=str(ve))
            self.addChild(_error)
            _error.show()
            return -1

    def close(self):
        print('try to close selfinfo')
        super().close()
        global_vars.window_list['selfinfo'] = None
        del self
    def closeEvent(self, event):
        self.close()