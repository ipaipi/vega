# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from db.mysql_db import pool  # 引入连接池


class RoleDao(object):
    # 查询角色列表
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select id,role from t_role"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 关闭链接
