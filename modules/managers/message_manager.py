# used for manage messages
from modules.managers import manager
class core:
    @staticmethod
    def setup():
        print('message_manager loading...')
    # success return 0, failed return -1
    @staticmethod
    def add_msg(msg, complain=False):
        mmd = manager.manager.database_manager
        sql = mmd.get_addmsg_sql(msg, complain)
        result = mmd.execute_insert(sql)
        return result

    @staticmethod
    def read_msg(complain=False):
        mmd = manager.manager.database_manager
        sql = mmd.get_readMsg_sql(complain)
        result = mmd.execute_query(sql, statu="mul")
        return result
    @staticmethod
    def del_msg(id):
        mmd = manager.manager.database_manager
        sql = mmd.get_delMsg_sql(id)
        result = mmd.execute_del(sql)
        return result