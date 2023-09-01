import sys

import pymysql
from modules import global_vars, database
from modules.UI.UI_use import signup_use,error_use
from PyQt5.QtWidgets import QApplication

class ui_manager:
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

