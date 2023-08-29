import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from modules.UI.UI_resourse import error
from global_vars import globals
from UI.UI_use import *

class manager:
    @staticmethod
    def get_db():
        default_host = 'localhost'
        default_user = 'root'
        default_password = '88888888'
        default_database = 'property'
        if globals.db is None:
            globals.db = pymysql.connect(host=default_host,
                                         user=default_user,
                                         password=default_password,
                                         database=default_database)
        return globals.db
