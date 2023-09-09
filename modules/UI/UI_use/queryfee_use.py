from modules.UI.UI_resourse import queryfeeUI
from PyQt5.QtWidgets import QMainWindow
from modules import global_vars
from modules.managers import manager

class queryfee(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = queryfeeUI.Ui_Form()
        self.setWindowTitle("query fee")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.cancel.clicked.connect(self.close)
        self.ui.ensure.clicked.connect(self.submit)

    def submit(self):
        try:
            key = int(self.ui.house_id.text())
            datas = manager.manager.fees_manager.query_fee(key)
            self.display_datas(datas)
        except ValueError as e:
            print("Through value error: " + str(e))
            _error = manager.manager.ui_manager.create_error()
            _error.set_message("数值有误")
            self.addChild(_error)
            _error.show()
        return 0
    def display_datas(self, datas):
        textlines = self.ui.display

        if len(datas) == 0:
            msg = "未查询到信息"
            textlines.setText(msg)
            return

        msg = """
        住房编号: {}
        缴费时间: {} 
        物业费: {}
        停车费: {} 
        其他费用: {}
        所有费用: {}
        已支付: {}
        """.format(datas['house_id'], datas['charge_time'], datas['property_fee'],
                   datas['park_fee'], datas['other_fee'], datas['all_fee'], datas['paid'])

        textlines.setText(msg)
        return
    def addChild(self, child):
        self.childs.append(child)
    def close(self):
        print("try to close queryfee")
        super().close()
        global_vars.window_list['queryfee'] = None
        del self