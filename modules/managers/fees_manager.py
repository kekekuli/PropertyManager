# used for manage property fees info
from modules.managers import manager
class core:
    @staticmethod
    def setup():
        print('fees_manager loading...')

    # 以字典形式返回一条物业费数据，不存在返回空
    @staticmethod
    def query_fee(house_id):
        dbm = manager.manager.database_manager
        sql = dbm.get_queryFee_sql(house_id)
        result = dbm.execute_query(sql)
        return result
    @staticmethod
    def add_fee(datas):
        dbm = manager.manager.database_manager
        sql = dbm.get_addFee_sql(datas)
        result = dbm.execute_insert(sql)
        if result == 0:
            print("Add fee failed")
            return -1
        else:
            print("Add fee success")
            return 0
    @staticmethod
    def del_fee(id):
        dbm = manager.manager.database_manager
        sql = dbm.get_delFee_sql(id)
        result = dbm.execute_del(sql)
        if result == 0:
            print("Add fee failed")
            return -1
        else:
            print("Add fee success")
            return 0
    @staticmethod
    def change_fee(datas):
        dbm = manager.manager.database_manager
        sql = dbm.get_changeFee_sql(datas)
        result = dbm.execute_update(sql)
        if result == 0:
            print("Change fee failed")
            return -1
        else:
            print("Change fee success")
            return 0