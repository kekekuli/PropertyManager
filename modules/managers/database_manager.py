# used for manage database
from modules import global_vars
from modules.database import database


class core:
    @staticmethod
    def setup():
        print('database_manager loading...')

        if global_vars.db is None:
            core.get_db()
        core.db = global_vars.db


    @staticmethod
    def get_db():
        if global_vars.db is None:
            global_vars.db = database()
        return global_vars.db

    @staticmethod
    def add_household(datas):
        sql = """insert into `household`(
                house_id, password, name, gender,
                profession, start_time, area, population, phone) 
                values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""

        sql = sql % (datas['house_id'], datas['password'], datas['name'], datas['gender'],
                  datas['profession'], datas['start_time'], datas['area'], datas['population'], datas['phone'])
        print(sql)
        try:
            result = core.db.insert_one(sql)
        except Exception as e:
            print('error at insert data:' + str(e))
    # return 0 if house_id not existed in database
    @staticmethod
    def signin_auth(house_id, password):
        sql = 'select * from household where house_id = "{}" and password = "{}"'.format(house_id, password)
        print(sql)
        result = core.db.fetchAll(sql);
        if len(result) == 0:
            print("No user exist")
        for item in result:
            print(item)
        return len(result)
    @staticmethod
    def add_message():
        pass

    @staticmethod
    def add_fees():
        pass

    # 以字典形式返回一条物业费数据，不存在返回空
    @staticmethod
    def query_fee(house_id):
        sql = 'select * from fees where house_id = "{}"'.format(house_id)
        print(sql)
        result = core.db.fetchAll(sql);
        if len(result) == 0:
            return {}
        else:
            return result[0]

