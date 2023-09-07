from modules.managers import manager

if __name__ == '__main__':
    manager.manager.setup()
    mainwin = manager.manager.ui_manager.create_mainwin()
    mainwin.show()
    manager.manager.wait_for_end()