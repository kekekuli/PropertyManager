import PyQt5.QtCore
from PyQt5 import QtWidgets, QtCore
from modules.managers import manager
from modules import global_vars
import sys

class showmsg(QtWidgets.QWidget):
    delStatus = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        msgm = manager.manager.message_manager
        self.childs = []

        super().__init__(parent)
        self.lay = QtWidgets.QVBoxLayout(self)

        self.scrollArea = QtWidgets.QScrollArea()
        self.lay.addWidget(self.scrollArea)
        self.top_widget = QtWidgets.QWidget()
        self.top_layout = QtWidgets.QVBoxLayout()

        self.set_ui(msgm.read_msg())

        self.top_widget.setLayout(self.top_layout)
        self.scrollArea.setWidget(self.top_widget)
        self.resize(300, 400)

        self.delStatus.connect(self.del_msg)
    def set_ui(self, datas):
        i = 1
        for item in datas:
            name = item['name']
            time = item['time']
            msg = item['msg']
            id = int(item['id'])

            group_box = QtWidgets.QGroupBox()
            group_box.setTitle('第{}条留言'.format(i))
            i += 1

            layout = QtWidgets.QVBoxLayout(group_box)

            label = QtWidgets.QLabel()
            label.setText("{}于{}留言:".format(name, time))
            layout.addWidget(label)

            testedit = QtWidgets.QTextEdit()
            testedit.setFixedSize(200, 80)
            testedit.setText(msg)
            layout.addWidget(testedit)

            # must save id as myid in myButton function
            # because id value is vary, need a place to hold
            def myButton():
                button = QtWidgets.QPushButton()
                button.setText("删除")
                myid = id
                button.setFixedSize(50, 30)
                button.clicked.connect(lambda : self.delStatus.emit(myid))
                return button
            layout.addWidget(myButton())

            self.top_layout.addWidget(group_box)
    def del_msg(self, id):
        result = manager.manager.message_manager.del_msg(id)
        self.close()

        _error = manager.manager.ui_manager.create_error()
        self.addChild(_error)

        if result == 0:
            _error.set_message("删除失败")
        else:
            _error.set_message("删除成功，正在刷新留言信息表")
            _error.set_size(10)

            self.close()
            result = manager.manager.ui_manager.create_showmsg()
            result.show()

        _error.show()
    def close(self):
        print("try to close showmsg...")
        super().close()
        global_vars.window_list['showmsg'] = None
        del self
    def addChild(self, child):
        self.childs.append(child)
    def closeEvent(self, event):
        self.close()
if __name__ == '__main__':
    manager.manager.setup()
    app = QtWidgets.QApplication(sys.argv)
    a = showmsg()
    a.show()
    sys.exit(app.exec_())