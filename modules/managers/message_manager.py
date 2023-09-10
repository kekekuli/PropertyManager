# used for manage messages
from modules.managers import manager
class core:
    @staticmethod
    def setup():
        print('message_manager loading...')
    # success return 0, failed return -1
    @staticmethod
    def add_msg(msg):
        mmd = manager.manager.database_manager
        sql = mmd.get_addmsg_sql(msg)
        result = mmd.execute_insert(sql)
        return result
