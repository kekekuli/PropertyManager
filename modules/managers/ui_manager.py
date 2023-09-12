# TODO--All the call of global_vals in ***_use should be deleted
# ***_use should not know the exist of global_vals

import sys

import pymysql
from modules import global_vars, database
from modules.UI.UI_use import signup_use, error_use, signin_use,\
    queryfee_use, mainwin_use, selfinfo_use, addmsg_use, showmsg_use,\
    alterfee_use, menu_use, showman_use
from modules.UI.UI_resourse import imageUI
from PyQt5.QtWidgets import QApplication, QWidget

class core:
    @staticmethod
    def setup():
        pass
    @staticmethod
    def create_signup():
        if global_vars.signinID is not None:
            raise Exception("请先登出")

        if global_vars.window_list['signup'] is None:
            print('Create new signup')
            global_vars.window_list['signup'] = signup_use.signup()
        return global_vars.window_list['signup']

    @staticmethod
    def create_error(tip="Default", size=16):
        print('Create new error')
        _error = error_use.error(msg=tip, fontSize=size)
        return _error
    @staticmethod
    def create_signin():
        if global_vars.signinID is not None:
            raise Exception("你已经登陆了")

        if global_vars.window_list['signin'] is None:
            print("Create new signin")
            global_vars.window_list['signin'] = signin_use.signin()
        return global_vars.window_list['signin']
    @staticmethod
    def create_queryfee():
        if global_vars.window_list['queryfee'] is None:
            print("Create new queryfee")
            global_vars.window_list['queryfee'] = queryfee_use.queryfee()
        return global_vars.window_list['queryfee']
    @staticmethod
    def create_selfinfo():
        if global_vars.signinID is None or global_vars.signinType != global_vars.user:
            raise Exception("非普通用户")
        if global_vars.window_list['selfinfo'] is None:
            print("Create new selfinfo")
            global_vars.window_list['selfinfo'] = selfinfo_use.selfinfo()
        return global_vars.window_list['selfinfo']
    @staticmethod
    def create_mainwin():
        if global_vars.window_list['mainwin'] is None:
            print("Create new mainwin")
            global_vars.window_list['mainwin'] = mainwin_use.mainwin()
        return global_vars.window_list['mainwin']
    @staticmethod
    def create_addmsg():
        if global_vars.signinID is None:
            raise Exception("请先登陆")
        if global_vars.window_list['addmsg'] is None:
            print("Create new addmsg")
            global_vars.window_list['addmsg'] = addmsg_use.addmsg()
        return global_vars.window_list['addmsg']
    @staticmethod
    def create_showmsg():
        if global_vars.window_list['showmsg'] is None:
            print("Create new showmsg")
            global_vars.window_list['showmsg'] = showmsg_use.showmsg()
        return global_vars.window_list['showmsg']
    @staticmethod
    def create_alterfee():
        if global_vars.window_list['alterfee'] is None:
            print("Create new alterfee")
            global_vars.window_list['alterfee'] = alterfee_use.alterfee()
        return global_vars.window_list['alterfee']
    @staticmethod
    def create_menu():
        if global_vars.window_list['menu'] is None:
            print("Create new menu")
            global_vars.window_list['menu'] = menu_use.menu()
        return global_vars.window_list['menu']

    @staticmethod
    def create_showman():
        if global_vars.window_list['showman'] is None:
            print("Create new showman")
            global_vars.window_list['showman'] = showman_use.showman()
        return global_vars.window_list['showman']
    # This is special, not like others have image_use.py, because I'm lazy
    @staticmethod
    def create_image():
        widget = QWidget()
        ui = imageUI.Ui_Form()
        ui.setupUi(widget)
        return widget
    # require set self to be current win
    @staticmethod
    def require_set_self(win, win_name):
        if global_vars.window_list['menu'] is None:
            print("menu not have created")
            return
        menu = global_vars.window_list['menu']
        menu.set_exe_win(win)
        menu.set_title(win_name)
    @staticmethod
    def require_set_default():
        if global_vars.window_list['menu'] is None:
            print("menu not have created")
            return
        menu = global_vars.window_list['menu']
        menu.set_exe_win(menu.default_win)
        menu.set_title("主界面")
