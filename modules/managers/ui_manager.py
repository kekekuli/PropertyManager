import sys

import pymysql
from modules import global_vars, database
from modules.UI.UI_use import signup_use, error_use, signin_use, queryfee_use
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