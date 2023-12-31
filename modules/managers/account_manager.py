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
    def signin_auth(house_id, password, signType):
        dbm = manager.manager.database_manager
        sql = dbm.get_signinAuth_sql(house_id, password, signType)
        result = dbm.execute_query(sql)
        return bool(result)

    @staticmethod
    def update_selfinfo(datas):
        dbm = manager.manager.database_manager
        sql = dbm.get_selfinfo_sql(datas)
        result = dbm.execute_update(sql)
        return result
    @staticmethod
    def all_households():
        dbm = manager.manager.database_manager
        sql = dbm.get_allHouseholds_sql()
        result = dbm.execute_query(sql, statu='mul')
        return result
    # Before del a man, must del fee
    @staticmethod
    def del_man(id):
        dbm = manager.manager.database_manager

        manager.manager.fees_manager.del_fee(id)

        sql = dbm.get_delMan_sql(id)
        result = dbm.execute_del(sql)
        return result
    @staticmethod
    def query_admin(id):
        dbm = manager.manager.database_manager
        sql = dbm.get_queryAdmin_sql(id)
        result = dbm.execute_query(sql)
        print(result)
        return result

