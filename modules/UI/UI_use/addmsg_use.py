# used for add new message to database
from modules.UI.UI_resourse import addmsgUI
from PyQt5.QtWidgets import QMainWindow
from modules.managers import manager
from modules import global_vars

class addmsg(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = addmsgUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("留言")
        self.childs = []

        self.ui.ensure.clicked.connect(self.submit)
        self.ui.cancel.clicked.connect(self.close)
    def close(self):
        print("try to close addmsg...")
        super().close()
        global_vars.window_list['addmsg'] = None
        del self
    def closeEvent(self, event):
        self.close()
    def submit(self):
        _msg = self.get_msg()
        _complain = self.get_complain()
        flag = self.parse_data(_msg)

        _error = manager.manager.ui_manager.create_error()

        # success in parse data
        if flag == 0:
            result = manager.manager.message_manager.add_msg(msg=_msg, complain=_complain)
            # success in add data to dabase
            if result != 0:
                _error.set_message("评论成功")
                self.close()
            else:
                _error.set_message("评论失败")
        else:
            _error.set_message("评论失败")

        self.addChild(_error)
        _error.show()

    def get_msg(self):
        return self.ui.msg.toPlainText()
    def get_complain(self):
        return self.ui.complain.isChecked()
    def parse_data(self, data):
        try:
            if len(data) == 0 or len(data) > 50:
                raise ValueError("长度非法")
            return 0
        except ValueError as ve:
            _error = manager.manager.ui_manager.create_error(tip=str(ve))
            self.addChild(_error)
            _error.show()
            return -1
    def addChild(self, child):
        self.childs.append(child)