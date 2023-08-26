import sys
import signupUI
from Managers.manager import manager
from signupUI import *
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = manager.create_app()
    ui = manager.create_signup_ui()
    window = manager.create_window()
    manager.link_ui_window(ui, window)
    manager.display_window(window)
    manager.wait_app_end()
