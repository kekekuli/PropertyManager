import PyQt5.QtCore
from PyQt5 import QtWidgets, QtCore
from modules.managers import manager
from modules import global_vars
import sys

class showmsg(QtWidgets.QWidget):
    delStatus = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)

        self.childs = []
        self.complainChecked = False

        self.lay = QtWidgets.QVBoxLayout(self)
        self.refresh()

        self.delStatus.connect(self.del_msg)

    def refresh(self):
        msgm = manager.manager.message_manager

        # check https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
        for i in reversed(range(self.lay.count())):
            self.lay.itemAt(i).widget().setParent(None)

        # Chechbox for is only show complain message
        self.complain = QtWidgets.QCheckBox()
        self.complain.setText("只显示投诉")
        self.complain.setChecked(self.complainChecked)
        self.complain.clicked.connect(self.change_complain_checked)

        self.lay.addWidget(self.complain)

        self.scrollArea = QtWidgets.QScrollArea()
        self.lay.addWidget(self.scrollArea)
        self.top_widget = QtWidgets.QWidget()
        self.top_layout = QtWidgets.QVBoxLayout()

        datas = msgm.read_msg(self.complainChecked)
        self.set_ui(datas)

        self.cancel = QtWidgets.QPushButton()
        self.cancel.setFixedSize(45, 30)
        self.cancel.setText("返回")
        self.cancel.clicked.connect(self.close)

        self.lay.addWidget(self.cancel)
        self.top_widget.setLayout(self.top_layout)
        self.scrollArea.setWidget(self.top_widget)
        self.resize(300, 400)

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
            if global_vars.signinType == global_vars.admin:
                layout.addWidget(myButton())

            self.top_layout.addWidget(group_box)
    def del_msg(self, id):
        result = manager.manager.message_manager.del_msg(id)

        _error = manager.manager.ui_manager.create_error()
        self.addChild(_error)

        if result == 0:
            _error.set_message("删除失败")
        else:
            _error.set_message("删除成功，正在刷新留言信息表")
            _error.set_size(10)

            result = manager.manager.ui_manager.create_showmsg()
            result.show()

            self.refresh()

        _error.show()

        self.refresh()

    def close(self):
        print("try to close showmsg...")
        super().close()
        global_vars.window_list['showmsg'] = None
        del self

        manager.manager.ui_manager.require_set_default()

    def addChild(self, child):
        self.childs.append(child)
    def closeEvent(self, event):
        self.close()
    def change_complain_checked(self):
        if self.complainChecked is False:
            self.complainChecked = True
        else:
            self.complainChecked = False
        self.refresh()

    def show(self):
        manager.manager.ui_manager.require_set_self(self, "查看留言")