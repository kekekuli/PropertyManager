import sys

from modules.managers.ui_manager import ui_manager
from modules import global_vars
from PyQt5.QtWidgets import QApplication
class manager:
    @staticmethod
    def setup():
        manager.ui_manager = ui_manager
        global_vars.app = QApplication(sys.argv)

    @staticmethod
    def wait_for_end():
        sys.exit(global_vars.app.exec())