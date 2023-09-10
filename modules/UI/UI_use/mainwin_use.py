# A main window used for test communicate between windows
from modules.UI.UI_resourse import mainwinUI
from PyQt5.QtWidgets import QMainWindow
from modules.managers import manager
from modules import global_vars

class mainwin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = mainwinUI.Ui_Form()
        self.setWindowTitle("Main window")
        self.ui.setupUi(self)
        self.childs = []

        self.ui.test1.clicked.connect(self.show_signin)
        self.ui.test2.clicked.connect(self.show_signup)
        self.ui.test3.clicked.connect(self.show_queryfee)
        self.ui.test4.clicked.connect(self.show_selfinfo)
        self.ui.logout.clicked.connect(self.show_logout)
        self.ui.addmsg.clicked.connect(self.show_addmsg)
        self.ui.showmsg.clicked.connect(self.show_showmsg)
    def show_signin(self):
        try:
            signin = manager.manager.ui_manager.create_signin()
            self.addChild(signin)
            signin.signinStatus.connect(self.accept_msg)
            signin.show()
        except Exception as e:
            _error = manager.manager.ui_manager.create_error(tip=str(e))
            self.addChild(_error)
            _error.show()
    def show_signup(self):
        try:
            signup = manager.manager.ui_manager.create_signup()
            self.addChild(signup)
            signup.show()
        except Exception as e:
            _error = manager.manager.ui_manager.create_error(tip=str(e))
            self.addChild(_error)
            _error.show()
    def show_queryfee(self):
        queryfee = manager.manager.ui_manager.create_queryfee()
        self.addChild(queryfee)
        queryfee.show()
    def show_selfinfo(self):
        try:
            selfinfo = manager.manager.ui_manager.create_selfinfo()
            self.addChild(selfinfo)
            selfinfo.show()
        except Exception as e:
            _error = manager.manager.ui_manager.create_error(tip=str(e))
            self.addChild(_error)
            _error.show()
    def show_logout(self):
        # Check if already logout
        if global_vars.signinID is None:
            _error = manager.manager.ui_manager.create_error(tip="你已经登出了", size=12)
            self.addChild(_error)
            _error.show()
            return

        manager.manager.logout()
        _error = manager.manager.ui_manager.create_error()
        self.addChild(_error)
        if global_vars.signinID is None:
            _error.set_message("登出成功")
        else:
            _error.set_message("登出失败")
        _error.show()
    def show_addmsg(self):
        mmu = manager.manager.ui_manager
        try:
            addmsg = mmu.create_addmsg()
            self.addChild(addmsg)
            addmsg.show()
        except Exception as e:
            _error = mmu.create_error(tip=str(e))
            self.addChild(_error)
            _error.show()
    def show_showmsg(self):
        mmu = manager.manager.ui_manager
        try:
            showmsg = mmu.create_showmsg()
            self.addChild(showmsg)
            showmsg.show()
        except Exception as e:
            _error = mmu.create_error(tip=str(e))
            self.addChild(_error)
            _error.show()
    def addChild(self, child):
        self.childs.append(child)
    def accept_msg(self, house_id):
        manager.manager.login(house_id)
    def close(self):
        print("try to close mainwin")
        super().close()
        global_vars.window_list['mainwin'] = None
        del self