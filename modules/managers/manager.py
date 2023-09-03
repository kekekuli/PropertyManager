import sys

from modules.managers import ui_manager
from modules.managers import account_manager
from modules.managers import message_manager
from modules.managers import fees_manager
from modules.managers import database_manager

from modules import global_vars
from PyQt5.QtWidgets import QApplication
class manager:
    @staticmethod
    def setup():
        manager.ui_manager = ui_manager.core
        manager.account_manager = account_manager.core
        manager.fees_manager = fees_manager.core
        manager.message_manager = message_manager.core
        manager.database_manager = database_manager.core

        manager.database_manager.setup()
        manager.ui_manager.setup()
        manager.account_manager.setup()
        manager.fees_manager.setup()
        manager.message_manager.setup()

        global_vars.app = QApplication(sys.argv)

    @staticmethod
    def wait_for_end():
        sys.exit(global_vars.app.exec())