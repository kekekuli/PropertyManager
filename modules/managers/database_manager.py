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
    def get_addHousehold_sql(datas):
        sql = """insert into `household`(
                        house_id, password, name, gender,
                        profession, start_time, area, population, phone) 
                        values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""
        sql = sql % (datas['house_id'], datas['password'], datas['name'], datas['gender'],
                     datas['profession'], datas['start_time'], datas['area'], datas['population'], datas['phone'])
        return sql
    @staticmethod
    def get_getHousehold_sql(house_id):
        sql = 'select * from household where house_id="{}"'.format(house_id)
        return sql
    @staticmethod
    def get_signinAuth_sql(house_id, password):
        sql = 'select * from household where house_id = "{}" and password = "{}"'.format(house_id, password)
        return sql

    @staticmethod
    def get_queryFee_sql(house_id):
        sql = 'select * from fees where house_id = "{}"'.format(house_id)
        return sql
    @staticmethod
    def get_selfinfo_sql(datas):
        sql = 'update household set name="{}", password="{}", phone="{}", gender="{}", profession="{}", population="{}"'
        sql = sql.format(datas['name'], datas['password'], datas['phone'],
                   datas['gender'], datas['profession'], datas['population'])
        return sql
    # return 0 if failed, other any value possible
    @staticmethod
    def execute_insert(sql):
        try:
            result = core.db.insert_one(sql)
            return result
        except Exception as e:
            print("Can not insert : " + str(e))
            return 0
    # return {} if failed
    @staticmethod
    def execute_query(sql):
        try:
            result = core.db.fetchAll(sql)
            if len(result) == 0:
                return {}
            else:
                return result[0]
        except Exception as e:
            print("Can not query : " + str(e))
            return {}
    # return 0 if failed, other any value possible
    @staticmethod
    def execute_update(sql):
        try:
            result = core.db.update(sql)
            return result
        except Exception as e:
            print("Can not update : " + str(e))
            return 0