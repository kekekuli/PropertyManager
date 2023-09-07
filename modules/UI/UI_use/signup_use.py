from PyQt5.QtWidgets import QMainWindow
from modules import global_vars
from modules.UI.UI_resourse import signupUI
from modules.managers import manager

class signup(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = signupUI.Ui_MainWindow()
        self.setWindowTitle("singup")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.submit.clicked.connect(self.submit)
        return
    def submit(self):
        datas = self.get_datas()
        flag = self.parse_data(datas)
        if flag == -1:
            return
        manager.manager.database_manager.add_household(datas)
        return
    def add_Child(self, child):
        self.childs.append(child)
        return

    def parse_data(self, datas):
        try:
            data = datas['house_id']
            for ch in data:
                if ch < '0' or ch > '9':
                    raise ValueError('输入有非法字符')

            data = datas['phone']
            for ch in data:
                if ch < '0' or ch > '9':
                    raise ValueError('输入有非法字符')

            data = float(datas['area'])
            datas['area'] = data

            if len(datas['house_id']) == 0 or len(datas['password']) == 0 \
                    or len(datas['name']) == 0 or len(datas['phone']) == 0:
                raise ValueError('长度有误')

            return 0

        except ValueError as e:
            print("Through Value Error:" + str(e))
            _error = manager.manager.ui_manager.create_error()
            if str(e) != '长度有误':
                _error.set_message('数值有误')
            else:
                _error.set_message('长度有误')
            self.add_Child(_error)
            _error.show()
            return -1

    def get_datas(self):
        ui = self.ui

        datas = dict()
        datas['house_id'] = ui.house_id.text()
        datas['name'] = ui.name.text()
        datas['password'] = ui.password.text()

        # In yyyy-mm-dd
        date = ui.start_date.date()
        datas['start_time'] = "{}-{}-{}".format(str(date.year()), str(date.month()), str(date.day()))

        datas['gender'] = ui.gender.currentText()
        datas['profession'] = ui.profession.currentText()
        datas['area'] = ui.area.text()
        datas['population'] = ui.population.value()
        datas['phone'] = ui.phone.text()

        print(datas)
        return datas