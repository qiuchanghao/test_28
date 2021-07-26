# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/6 17:22
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
import pymysql
import string
import random
'''
工具类
链接数据库
ip,端口，用户名，密码，对应的库
'''
# class Test_Mysql():
#     def __init__(self,ip,user,password,db,port):
#         '''准备连接参数'''
#         # 创建对象--db_connect
#         # 实例化connect---拿到一个对象db_connect
#         try:
#             self.db_connect = pymysql.connect(host=ip, user=user, password=password, db=db, port=port)
#             self.cursor = self.db_connect.cursor()  # 创建游标---对数据库增删改
#         except Exception as e:
#             print(f'链接异常{e}')
#     def update_sql(self,sql):
#         try:
#             self.cursor.execute(sql)#传入需要执行sql语句
#             self.db_connect.commit()
#         except Exception as e:
#             print(f'修改异常{e}')
#
#     # def insert_sql(self, sql):
#     #     self.cursor.execute(sql)  # 传入需要执行sql语句
#     #     self.db_connect.commit()
#     #
#     # def delete_sql(self, sql):
#     #     self.cursor.execute(sql)  # 传入需要执行sql语句
#     #     self.db_connect.commit()
#
#         # #添加数据
#         # self.cursor.execute('insert into sys_user(id,user,login_pwd,tel)values(1000,"admin1","123456","18813913812")')
#         # self.db_connect.commit()
#         # # 修改数据
#         # self.cursor.execute('update sys_user set tel="18819919191" where id=1000')
#         # self.db_connect.commit()
#         # #删除数据
#         # self.cursor.execute('delete from sys_user where id=1000')
#         # self.db_connect.commit()
#
#     def select_sql(self,sql):
#         # 查询数据
#         try:
#             self.cursor.execute(sql)  # 游标对象操作执行方法，(查询sql)
#             print(self.cursor.fetchone())  # 游标返回所有结果---fetchall---打印
#         except Exception as e:
#             print(f'查询异常{e}')
#
#         finally:
#             self.cursor.close()#关闭游标
#             self.db_connect.close()#关闭数据库
#
# if __name__ == '__main__':
#     test_mysql=Test_Mysql('192.168.31.204','root','Aa123456.','test_class',3306)
#     test_mysql.update_sql('insert into sys_user(id,user,login_pwd,tel)values(1000,"admin1","123456","18813913812")')
#     test_mysql.select_sql('select * from sys_user where id=1000')
#     test_mysql.select_sql('select * from sys_user where id=12')




class Insert_Data():
    def __init__(self,ip,user,password,db,port):
        try:
            self.db_connect = pymysql.connect(host=ip, user=user, password=password, db=db, port=port)
            self.cursor = self.db_connect.cursor()  # 创建游标---对数据库增删改
        except Exception as e:
            print(f'链接异常{e}')
    def insert_sql(self,i,user_name,user_pwd,user_tel):
        try:
            self.cursor.execute('insert into sys_user(id,user,login_pwd,tel)values({},"{}","{}","{}")'.format(i,user_name,user_pwd,user_tel))#传入需要执行sql语句
            self.db_connect.commit()
        except Exception as e:
            print(f'修改异常{e}')
    def info(self):
        for i in range(20101,20201):
            user_name='user_'+str(i)
            user_pwd='111111'
            user_tel=''.join(random.sample(string.ascii_letters,6))
            self.insert_sql(i,user_name,user_pwd,user_tel)


if __name__ == '__main__':

    test_mysql=Insert_Data('192.168.31.204','root','Aa123456.','test_class',3306)
    test_mysql.info()