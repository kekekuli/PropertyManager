# TODO--All the call of global_vals in ***_use should be deleted
# ***_use should not know the exist of global_vals

import sys

import pymysql
from modules import global_vars, database
from modules.UI.UI_use import signup_use, error_use, signin_use,\
    queryfee_use, mainwin_use, selfinfo_use
from PyQt5.QtWidgets import QApplication

class core:
    @staticmethod
    def setup():
        pass
    @staticmethod
    def create_signup():
        if global_vars.window_list['signup'] is None:
            global_vars.window_list['signup'] = signup_use.signup()
        return global_vars.window_list['signup']

    @staticmethod
    def create_error():
        _error = error_use.error()
        return _error
    @staticmethod
    def create_signin():
        if global_vars.window_list['signin'] is None:
            global_vars.window_list['signin'] = signin_use.signin()
        return global_vars.window_list['signin']
    @staticmethod
    def create_queryfee():
        if global_vars.window_list['queryfee'] is None:
            global_vars.window_list['queryfee'] = queryfee_use.queryfee()
        return global_vars.window_list['queryfee']
    @staticmethod
    def create_selfinfo():
        if global_vars.window_list['selfinfo'] is None:
            global_vars.window_list['selfinfo'] = selfinfo_use.selfinfo()
        return global_vars.window_list['selfinfo']
    @staticmethod
    def create_mainwin():
        if global_vars.window_list['mainwin'] is None:
            global_vars.window_list['mainwin'] = mainwin_use.mainwin()
        return global_vars.window_list['mainwin']