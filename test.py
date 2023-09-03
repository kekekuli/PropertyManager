from modules.managers.manager import manager

class test:
    @staticmethod
    def test_signup():
        manager.setup()
        signup = manager.ui_manager.create_signup()
        signup.show()
        manager.wait_for_end()
    @staticmethod
    def test_signin():
        manager.setup()
        signin = manager.ui_manager.create_signin()
        signin.show()
        manager.wait_for_end()