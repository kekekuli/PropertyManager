# used for manage database
from modules import global_vars
from modules.database import database
from datetime import datetime

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
    def get_signinAuth_sql(house_id, password, signType):
        sql = ""
        if signType == global_vars.user:
            sql = 'select * from household where house_id = "{}" and password = "{}"'.format(house_id, password)
        elif signType == global_vars.admin:
            sql = 'select * from admins where id = "{}" and password = "{}"'.format(house_id, password)
        else:
            raise Exception("不能正确处理登陆角色")
        return sql

    @staticmethod
    def get_queryFee_sql(house_id):
        sql = 'select * from fees where house_id = "{}"'.format(house_id)
        return sql
    @staticmethod
    def get_selfinfo_sql(datas):
        sql = """update household 
                set name='{}', password='{}', phone='{}', 
                gender='{}', profession='{}', population='{}' 
                where house_id='{}'
        """
        sql = sql.format(datas['name'], datas['password'], datas['phone'],
                   datas['gender'], datas['profession'], datas['population'], global_vars.signinID)
        return sql
    @staticmethod
    def get_addmsg_sql(msg, complain):
        full_date = datetime.now()
        time = "{}-{}-{}".format(full_date.year, full_date.month, full_date.day)

        name_sql = ""
        if global_vars.signinType == global_vars.user:
            name_sql = core.get_getHousehold_sql(global_vars.signinID)
        elif global_vars.signinType == global_vars.admin:
            name_sql = core.get_queryAdmin_sql(global_vars.signinID)

        datas = core.execute_query(name_sql)
        name = datas['name']

        sql = 'insert into message(name, msg, time, complain) values ("{}", "{}", "{}", {})'
        sql = sql.format(name, msg, time, complain)

        return sql
    @staticmethod
    def get_readMsg_sql(complain):
        sql = ""
        if complain is True:
            sql = 'select * from message where complain={}'.format(complain)
        else:
            sql = 'select * from message'
        return sql
    @staticmethod
    def get_delMsg_sql(id):
        sql = 'delete from message where id="{}"'.format(id)
        return sql
    @staticmethod
    def get_addFee_sql(datas):
        sql = """ insert into fees(house_id, property_fee, park_fee, other_fee, paid, charge_time)
                values ('%s', '%s', '%s', '%s', '%s', '%s')"""
        sql = sql % (datas['house_id'], datas['property_fee'], datas['park_fee'],
                         datas['other_fee'], datas['paid'], str(datas['charge_time']))
        print("debug")
        print(sql)
        return sql
    @staticmethod
    def get_delFee_sql(id):
        sql = 'delete from fees where house_id="{}"'.format(id)
        return sql
    @staticmethod
    def get_changeFee_sql(datas):
        sql = """ update fees
                set charge_time='{}', paid='{}', property_fee='{}',
                park_fee='{}', other_fee='{}'    
                where house_id='{}'
        """

        sql = sql.format(datas['charge_time'], datas['paid'], datas['property_fee'],
                         datas['park_fee'], datas['other_fee'], datas['house_id'])
        return sql
    @staticmethod
    def get_allHouseholds_sql():
        sql = 'select * from household'
        return sql
    @staticmethod
    def get_delMan_sql(id):
        sql = 'delete from household where house_id="{}"'.format(id);
        return sql
    @staticmethod
    def get_queryAdmin_sql(id):
        sql = 'select * from admins where id="{}"'.format(id)
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
    # return {} if failed, statu decide return one or more
    @staticmethod
    def execute_query(sql, statu="one"):
        try:
            result = core.db.fetchAll(sql)
            if len(result) == 0:
                return {}
            else:
                if statu == "mul":
                    return result
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
            print("Can not update/delete : " + str(e))
            return 0
    @staticmethod
    def execute_del(sql):
        return core.execute_update(sql)