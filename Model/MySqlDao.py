import pymysql

# 读取文档
def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        sql = ''
        for s in f.readlines():
            sql = sql + s.strip()
    return sql

class MySqlDao:
    coonect = {}
    cursor = {}
    host_list = {
        'nkbot': {
            'host': '148.70.75.212',
            'port': 3306,
            'user': 'nkbot',
            'password': 'Dm3nafPjNBywamxM',
            'database': 'nkbot',
        }
    }

    host_dict = {}

    def __init__(self, host_name='nkbot'):
        if host_name in self.host_list:
            self.host_dict = self.host_list[host_name]
        else:
            self.host_dict = self.host_list['nkbot']

    def init(self):
        self.coonect = self.get_connect()
        self.cursor = self.coonect.cursor()

    def get_connect(self):
        return pymysql.connect(
            host=self.host_dict['host'],
            port=self.host_dict['port'],
            user=self.host_dict['user'],
            password=self.host_dict['password'],
            database=self.host_dict['database'],
            charset='utf8',
            # cursorclass=pymysql.cursors.DictCursor
        )

    def initDataBase(self):
        sql = read('nike.sql')
        self.exec(sql)


    def exec(self, sql=''):
        self.init()
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.coonect.commit()
            res = 1
        except:
            # 发生错误时回滚
            self.coonect.rollback()
            res = 0

        # 关闭数据库连接
        self.coonect.close()
        return res

    def rows(self, sql):
        self.init()
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except:
            res = []
        self.coonect.close()
        return res

    def row(self, sql):
        self.init()
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except:
            res = {}
        self.coonect.close()
        return res

    def count(self, sql):
        self.init()
        try:
            self.cursor.execute(sql)
            res = self.cursor.rowcount
        except:
            res = 0
        self.coonect.close()
        return res
