import sys
import signupUI
from Managers.manager import manager
from signupUI import *
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = manager.create_app()
    window = manager.create_signup()
    window.show()
    manager.wait_app_end()
