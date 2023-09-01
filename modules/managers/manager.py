import sys

from modules.managers.ui_manager import ui_manager
from modules.managers.account_manager import account_manager
from modules.managers.message_manager import message_manager
from modules.managers.fees_manager import fees_manager
from modules.managers.database_manager import database_manager

from modules import global_vars
from PyQt5.QtWidgets import QApplication
class manager:
    @staticmethod
    def setup():
        manager.ui_manager = ui_manager
        manager.account_manager = account_manager
        manager.fees_manager = fees_manager
        manager.message_manager = message_manager
        manager.database_manager = database_manager

        manager.database_manager.setup()
        manager.ui_manager.setup()
        manager.account_manager.setup()
        manager.fees_manager.setup()
        manager.message_manager.setup()

        global_vars.app = QApplication(sys.argv)

    @staticmethod
    def wait_for_end():
        sys.exit(global_vars.app.exec())