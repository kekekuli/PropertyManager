import pymysql
import sys
import signupUI
import PyQt5.QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QDate



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
    def link_submit_parse(ui):
        ui.submit.clicked.connect(manager.parse_signup_date)

    @staticmethod
    def create_signup_ui():
        if manager.ui_lists['signup'] is None:
            manager.ui_lists['signup'] = signupUI.Ui_MainWindow()
        return manager.ui_lists['signup']

    # Call parse function when clicked submit

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
        manager.link_submit_parse(ui)

    @staticmethod
    def display_window(window):
        window.show()

    @staticmethod
    def wait_app_end():
        if manager.app is None:
            return
        sys.exit(manager.app.exec())


    @staticmethod
    def parse_signup_date():
        ui = manager.ui_lists['signup']

        datas = dict()
        datas['house_id'] = ui.house_id.text()
        datas['name'] = ui.name.text()
        datas['password'] = ui.password.text()

        # In yyyy-mm-dd
        date = ui.start_date.date()
        datas['start_time'] = "{}-{}-{}".format(str(date.year()), str(date.month()), str(date.day()))

        datas['gender'] = ui.gender.currentText()
        datas['profession'] = ui.profession.currentText()
        datas['area'] = float(ui.area.text())
        datas['population'] = int(ui.population.value())
        datas['phone'] = ui.phone.text()

        print(datas)
