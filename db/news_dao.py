# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from db.mysql_db import pool  # 引入连接池


class NewsDao(object):
    # 查询待审批新闻列表
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id,n.title,t.type,u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                  "join t_user u on n.editor_id =u.id " \
                  "where n.state=%s " \
                  "order by n.create_time desc " \
                  "limit %s,%s"
            cursor.execute(sql, ("待审批", (page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 关闭链接

    # 查询待审批新闻列表页数
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(*)/10) from t_news n where n.state=%s"
            cursor.execute(sql, ["待审批"])
            search_page = cursor.fetchone()[0]
            return search_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()# 关闭链接

    # 审批新闻
    def update_unreview_news(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "update t_news set state=%s where id=%s"
            cursor.execute(sql, ("已审批", id))
            con.commit()#提交事务
        except Exception as e:
            if 'con' in dir():
                con.rollback()#如果发生错误，回滚事务
            print(e)
        finally:
            if 'con' in dir():
                con.close()# 关闭连接

    # 查询新闻列表
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id,n.title,t.type,u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                  "join t_user u on n.editor_id =u.id " \
                  "order by n.create_time desc " \
                  "limit %s,%s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询新闻总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(*)/10) from t_news"
            cursor.execute(sql)
            search_page = cursor.fetchone()[0]
            return search_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 删除新闻
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "delete from t_news where id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

# service = NewsDao()
# result=service.search_unreview_list(1)
# print(result)
