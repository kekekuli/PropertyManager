from modules.manager import manager

if __name__ == '__main__':
    app = manager.create_app()
    window = manager.create_signup()
    window.show()
    manager.wait_app_end()
