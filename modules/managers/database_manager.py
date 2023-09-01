# used for manage database
from modules import global_vars
from modules.database import database


class database_manager:
    @staticmethod
    def setup():
        print('database_manager loading...')

        if global_vars.db is None:
            database_manager.get_db()
        database_manager.db = global_vars.db


    @staticmethod
    def get_db():
        if global_vars.db is None:
            global_vars.db = database()
        return global_vars.db

    @staticmethod
    def add_household(datas):
        sql = """insert into `household`(
                house_id, password, owner_name, gender,
                profession, start_time, area, population, phone) 
                values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""

        sql = sql % (datas['house_id'], datas['password'], datas['owner_name'], datas['gender'],
                  datas['profession'], datas['start_time'], datas['area'], datas['population'], datas['phone'])
        print(sql)
        try:
            result = database_manager.db.insert_one(sql)
        except Exception as e:
            print('error at insert data:' + str(e))
    @staticmethod
    def add_message():
        pass

    @staticmethod
    def add_fees():
        pass
