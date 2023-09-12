from PyQt5 import QtWidgets
from modules.UI.UI_resourse import alterfeeUI
from modules import global_vars
from modules.managers import manager

class alterfee(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = alterfeeUI.Ui_Form()
        self.setWindowTitle("修改物业费")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.view.clicked.connect(self.display_content)
        self.ui.change.clicked.connect(self.change_fee)
        self.ui.dele.clicked.connect(self.del_fee)
        self.ui.create.clicked.connect(self.create_fee)
    def close(self):
        print("try to close alterfee...")
        super().close()
        global_vars.window_list['alterfee'] = None
        del self
    def change_fee(self):
        datas = self.get_datas()

        if bool(datas) is False:
            return

        result = manager.manager.fees_manager.change_fee(datas)

        _error = manager.manager.ui_manager.create_error()
        self.addChild(_error)
        _error.show()

        if result == -1:
            _error.set_message("修改失败")
        else:
            _error.set_message("修改成功")
            try:
                self.read_fee_data()
            except:
                pass

    def addChild(self, child):
        self.childs.append(child)
    def read_fee_data(self):
        id = self.get_inputID()
        fee_datas = manager.manager.fees_manager.query_fee(id)
        household_datas = manager.manager.account_manager.get_household(id)

        if bool(household_datas) is False:
            self.clear_content()
            raise Exception("不存在此用户")

        if bool(fee_datas) is False:
            self.clear_content()
            self.ui.name.setText(household_datas['name'])
            raise Exception("未产生物业费")

        self.ui.name.setText(household_datas['name'])
        self.ui.property_fee.setText(str(fee_datas['property_fee']))
        self.ui.park_fee.setText(str(fee_datas['park_fee']))
        self.ui.other_fee.setText(str(fee_datas['other_fee']))
        self.ui.all_fee.setText(str(fee_datas['all_fee']))
        self.ui.charge_time.setDate(fee_datas['charge_time'])
        self.ui.paid.setText(str(fee_datas['paid']))
    def get_inputID(self):
        return self.ui.house_id.text()
    def del_fee(self):
        id = self.get_inputID()
        result = manager.manager.fees_manager.del_fee(id)

        _error = manager.manager.ui_manager.create_error()
        self.addChild(_error)
        _error.show()

        if result == -1:
            _error.set_message("删除失败")
        else:
            _error.set_message("删除成功")
            try:
                self.read_fee_data()
            except:
                pass

    def get_datas(self):
        datas = {}
        datas['house_id'] = self.ui.house_id.text()
        datas['property_fee'] = self.ui.property_fee.text()
        datas['park_fee'] = self.ui.park_fee.text()
        datas['other_fee'] = self.ui.other_fee.text()
        datas['paid'] = self.ui.paid.text()
        date = self.ui.charge_time.date()
        datas['charge_time'] = "{}-{}-{}".format(str(date.year()), str(date.month()), str(date.day()))

        if self.parse_datas(datas) == -1:
            return {}

        return datas
    def parse_datas(self, datas):
        try:
            if len(datas['house_id']) == 0 or len(datas['property_fee']) == 0 or \
                len(datas['park_fee']) == 0 or len(datas['other_fee']) == 0 or \
                len(datas['paid']) == 0 : \
                    raise ValueError()
            datas['house_id'] = int(datas['house_id'])
            datas['property_fee'] = float(datas['property_fee'])
            datas['park_fee'] = float(datas['park_fee'])
            datas['other_fee'] = float(datas['other_fee'])
            datas['paid'] = float(datas['paid'])

            return 0
        except Exception as e:
            print(e)
            _error = manager.manager.ui_manager.create_error(tip="数据有误")
            self.addChild(_error)
            _error.show()

            return -1
    def create_fee(self):
        datas = self.get_datas()
        if bool(datas) is False:
            return
        result = manager.manager.fees_manager.add_fee(datas)

        _error = manager.manager.ui_manager.create_error()
        self.addChild(_error)
        _error.show()

        if result == -1:
            _error.set_message("创建失败")
        else:
            _error.set_message("创建成功")
            self.read_fee_data()
    def clear_content(self):
        self.ui.name.setText("")
        self.ui.property_fee.setText("")
        self.ui.other_fee.setText("")
        self.ui.park_fee.setText("")
        self.ui.paid.setText("")
        self.ui.all_fee.setText("")
    def display_content(self):
        try:
            self.read_fee_data()
        except Exception as e:
            _error = manager.manager.ui_manager.create_error(tip=str(e), size=12)
            self.addChild(_error)
            _error.show()
