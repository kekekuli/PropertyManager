import pymysql
import sys
import signupUI
from PyQt5.QtWidgets import QApplication, QMainWindow


class manager:
    db = None
    app = None
    ui_lists = {'signin': None, 'signup': None}
    @staticmethod
    def link_to_db():
        default_host = 'localhost'
        default_user = 'root'
        default_password = '88888888'
        default_database = 'property'
        if manager.db is None:
            manager.db = pymysql.connect(host=default_host,
                                         user=default_user,
                                         password=default_password,
                                         database=default_database)
        return manager.db

    @staticmethod
    def owner_signup():
        return

    @staticmethod
    def owner_signin():
        return

    @staticmethod
    def self_info_manage():
        return

    @staticmethod
    def post_message():
        return

    @staticmethod
    def admin_info_manage():
        return

    @staticmethod
    def property_fee_manage():
        return

    @staticmethod
    def message_manage():
        return


    @staticmethod
    def create_signup_ui():
        if manager.ui_lists['signup'] is None:
            manager.ui_lists['signup'] = signupUI.Ui_MainWindow()
        return manager.ui_lists['signup']

    @staticmethod
    def create_window():
        return QMainWindow()

    @staticmethod
    def create_app():
        if manager.app is None:
            manager.app = QApplication(sys.argv)
        return manager.app


    @staticmethod
    def link_ui_window(ui, window):
        ui.setupUi(window)

    @staticmethod
    def display_window(window):
        window.show()

    @staticmethod
    def wait_app_end():
        if manager.app is None:
            return
        sys.exit(manager.app.exec())