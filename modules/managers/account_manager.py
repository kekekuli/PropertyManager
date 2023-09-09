# used for manage accounts of household
from modules.managers import manager
class core:
    @staticmethod
    def setup():
        print('account_manager loading...')

    @staticmethod
    def add_household(datas):
        dbm = manager.manager.database_manager
        sql = dbm.get_addHousehold_sql(datas)
        result = dbm.execute_insert(sql)
        if result == 0:
            print("Add household failed")
            return -1
        else:
            print("Add household succeed")
            return 0
    @staticmethod
    def get_household(house_id):
        dbm = manager.manager.database_manager
        sql = dbm.get_getHousehold_sql(house_id)
        result = dbm.execute_query(sql)
        return result
    @staticmethod
    def signin_auth(house_id, password):
        dbm = manager.manager.database_manager
        sql = dbm.get_signinAuth_sql(house_id, password)
        result = dbm.execute_query(sql)
        return bool(result)

    @staticmethod
    def update_selfinfo(datas):
        dbm = manager.manager.database_manager
        sql = dbm.get_selfinfo_sql(datas)
        result = dbm.execute_update(sql)
        return result