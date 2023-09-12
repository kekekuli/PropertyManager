from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from modules.managers import manager
from modules import global_vars

class menu(QWidget):
    def __init__(self, parent=None):
        self.default_win = manager.manager.ui_manager.create_mainwin()
        self.current_win = self.default_win
        super().__init__(parent)
        self.mainLayout = QVBoxLayout(self)
        self.setFixedSize(850, 650)

        self.set_layout()

    def close(self):
        pass

    def set_layout(self):
        self.top_widget = QWidget()
        self.top_widget.setFixedSize(800, 80)
        self.top_widget.setStyleSheet("background-color: #73cbdf")
        self.top_layout = QVBoxLayout(self.top_widget)
        self.top_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        self.top_layout.title = QLabel()
        self.top_layout.title.setText("物业管理系统---V1.1")
        # self.top_layout.title.setStyleSheet("background-color: #e0e6e2")
        self.top_layout.title.setFixedSize(300, 30)
        self.top_layout.addWidget(self.top_layout.title)
        self.top_layout.title.setAlignment(Qt.AlignCenter)
        manager.manager.set_font_size(self.top_layout.title, 20)

        self.top_layout.sec_title = QLabel()
        self.set_title("主界面")
        # self.top_layout.sec_title.setStyleSheet("background-color: #e0e6e2")
        self.top_layout.sec_title.setFixedSize(280, 15)
        self.top_layout.addWidget(self.top_layout.sec_title)
        self.top_layout.sec_title.setAlignment(Qt.AlignCenter)
        manager.manager.set_font_size(self.top_layout.sec_title, 12)


        self.container = QWidget()
        self.container_layout = QHBoxLayout(self.container)

        self.left_widget = QWidget()
        self.left_widget.setFixedSize(180, 500)
        self.left_widget.setStyleSheet("background-color: #e3b86a")
        self.left_layout = QVBoxLayout(self.left_widget)
        #self.left_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.container_layout.addWidget(self.left_widget)

        self.exe_widget = QWidget()
        self.exe_layout = QHBoxLayout(self.exe_widget)
        self.exe_widget.setStyleSheet("background-color: #e0e6e2")
        self.set_exe_win(self.default_win)
        self.refresh_left()
        self.container_layout.addWidget(self.exe_widget)

        self.mainLayout.addWidget(self.top_widget)
        self.mainLayout.addWidget(self.container)
    # Refresh the information of the left bar
    def refresh_left(self):
        # Delete old widgets
        for i in reversed(range(self.left_layout.count())):
            self.left_layout.itemAt(i).widget().setParent(None)

        datas = self.get_leftBar_datas()

        user_widget = QWidget()
        user_layout = QVBoxLayout(user_widget)
        user_layout.setAlignment(Qt.AlignTop)

        label1 = QLabel()
        label1.setFixedSize(100, 20)
        label1.setText("用户名: {}".format(datas['name']))

        label2 = QLabel()
        label2.setFixedSize(100, 20)
        label2.setText("用户身份: {}".format(datas['type']))

        label3 = QLabel()
        label3.setFixedSize(100, 20)
        label3.setText("用户id: {}".format(datas['id']))

        user_layout.addWidget(label1)
        user_layout.addWidget(label2)
        user_layout.addWidget(label3)

        copyright_widget = QWidget()
        copyright_layout = QVBoxLayout(copyright_widget)
        copyright_layout.setAlignment(Qt.AlignBottom)


        label4 = QLabel()
        label4.setFixedSize(150, 20)
        label4.setText("版权所有: @kekekuli")
        label4.setAlignment(Qt.AlignCenter)

        copyright_layout.addWidget(label4)
        label4.setStyleSheet("background-color: #e3b88a")

        self.left_layout.addWidget(user_widget)
        self.left_layout.addWidget(copyright_widget)

    # Goback the default win
    def set_exe_win(self, win):
        # check https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
        for i in reversed(range(self.exe_layout.count())):
            self.exe_layout.itemAt(i).widget().setParent(None)
        self.exe_layout.addWidget(win)

        self.current_win = win
    def get_leftBar_datas(self):
        datas = {}
        if global_vars.signinID is None:
            datas['name'] = "未登陆"
            datas['id'] = "未登陆"
            datas['type'] = "未登陆"
        else:
            datas['id'] = global_vars.signinID
            datas['type'] = global_vars.signinType

            if global_vars.signinType == global_vars.user:
                household = manager.manager.account_manager.get_household(datas['id'])
                datas['name'] = household['name']
            elif global_vars.signinType == global_vars.admin:
                admin = manager.manager.account_manager.query_admin(datas['id'])
                datas['name'] = admin['name']
            else:
                datas['name'] = '未知'

        return datas
    # The sec title
    def set_title(self, msg):
        self.top_layout.sec_title.setText(msg)