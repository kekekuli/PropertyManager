from modules.manager import manager
from modules import global_vars

if __name__ == '__main__':
    manager.setup()
    signup = manager.create_signup()
    signup.show()
    manager.wait_for_end()