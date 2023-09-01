#引入pymysql模块
import pymysql

class database:
    #初始化
    def __init__(self):
        #创建连接
        self.conn = pymysql.Connect(
          host = 'localhost',
          port = 3306,
          user = 'root',
          password = '88888888',
          db = 'property',
          charset = 'utf8',
          cursorclass = pymysql.cursors.DictCursor  #以字典的形式返回数据
        )
        #获取游标
        self.cursor = self.conn.cursor()

    #返回多条数据
    def fetchAll(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #插入一条数据
    def insert_one(self,sql):
        result = self.cursor.execute(sql)
        self.conn.commit()
        return result

    #插入多条数据
    def insert_many(self,sql,datas):
        result = self.cursor.executemany(sql,datas)
        self.conn.commit()
        return result

    #更新数据
    def update(self,sql):
        result = self.cursor.execute(sql)
        self.conn.commit()
        return result

    #关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()