from modules.managers import manager

if __name__ == '__main__':
    manager.manager.setup()
    #mainwin = manager.manager.ui_manager.create_mainwin()
    #mainwin.show()
    menu = manager.manager.ui_manager.create_menu()
    menu.show()
    manager.manager.wait_for_end()