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