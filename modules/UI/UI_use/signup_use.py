from PyQt5.QtWidgets import QMainWindow
from modules import global_vars
from modules.UI.UI_resourse import signupUI
from modules.managers import manager


class signup:
    def __init__(self):
        self.ui = signupUI.Ui_MainWindow()
        self.window = QMainWindow()
        self.window.setWindowTitle("singup")
        self.ui.setupUi(self.window)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.submit.clicked.connect(self.submit)
        return
    def show(self):
        self.window.show()
        return
    def submit(self):
        datas = self.get_datas()
        flag = self.parse_data(datas)
        if flag == -1:
            return
        #manager.send_signup_data(datas)
        return
    def close(self):
        self.window.close()
        global_vars.window_list['signup'] = None
        del self
        return
    def addChild(self, child):
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
                    or len(datas['name']) == 0:
                raise ValueError('长度不符合要求')

            return 0

        except ValueError as e:
            print("Through Value Error")
            _error = manager.ui_manager.create_error()
            self.addChild(_error)
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