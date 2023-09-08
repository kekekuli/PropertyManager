# used for change self infomatino
from modules.UI.UI_resourse import selfinfoUI
from PyQt5.QtWidgets import QMainWindow
from modules.managers import manager
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

        self.read_signin_statu()
        return
    def submit(self):
        pass
    def addChild(self, child):
        self.childs.append(child)
    # read saved signin statu to change title
    def read_signin_statu(self):
        signinStatu = manager.manager.get_log_statu()
        datas = manager.manager.database_manager.get_household(signinStatu)
        msg = "尊敬的{}号住户业主{}，选择你要更改的信息".format(datas['house_id'], datas['name'])
        self.ui.canva.setText(msg)
        self.ui.name.setText(datas['name'])
        self.ui.password.setText(datas['password'])
        self.ui.phone.setText(datas['phone'])
        self.ui.gender.setCurrentText(datas['gender'])
        self.ui.profession.setCurrentText(datas['profession'])
        self.ui.population.setValue(datas['population'])
    def close(self):
        print('try to close selfinfo')
        super().close()
        global_vars.window_list['selfinfo'] = None
        del self