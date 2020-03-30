# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from db.mysql_db import pool  # 引入连接池


class UserDao(object):
    # 验证用户登陆
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username=%s AND " \
                  "AES_DECRYPT(UNHEX(password),'HelloWorld')=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            if count == 1:
                return True
            else:
                return False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()  # 关闭链接

    # 查询用户角色
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select r.role from t_user u join t_role r on u.role_id = r.id and " \
                  " u.username=%s"
            cursor.execute(sql, [username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 添加记录
    def insert(self, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_user(username,password,email,role_id) " \
                  "VALUES(%s,HEX(AES_ENCRYPT(%s,'HelloWorld')),%s,%s)"
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()  # 如果发生错误，回滚事务
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询单个用户信息
    def search_username(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username=%s"
            cursor.execute(sql, [username])
            count = cursor.fetchone()[0]
            if count == 1:
                return True
            else:
                return False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_user"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户分页记录
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT u.id,u.username,r.role " \
                  "FROM t_user u JOIN t_role r " \
                  "ON u.role_id=r.id " \
                  "ORDER BY u.id " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 修改用户信息
    def update(self, id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_user SET username=%s," \
                  "password=HEX(AES_ENCRYPT(%s,'HelloWorld'))," \
                  "email=%s,role_id=%s " \
                  "WHERE id=%s"
            cursor.execute(sql, (username, password, email, role_id, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除用户
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_user WHERE id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
