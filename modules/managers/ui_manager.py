# TODO--All the call of global_vals in ***_use should be deleted
# ***_use should not know the exist of global_vals

import sys

import pymysql
from modules import global_vars, database
from modules.UI.UI_use import signup_use, error_use, signin_use,\
    queryfee_use, mainwin_use, selfinfo_use, addmsg_use, showmsg_use
from PyQt5.QtWidgets import QApplication

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
        if global_vars.signinID is None:
            raise Exception("请先登陆")
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