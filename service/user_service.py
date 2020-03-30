# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from db.user_dao import UserDao


class UserSercicr(object):
    __user_dao = UserDao()

    # 验证用户登录
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    # 查询用户角色
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    # 查询单个用户信息
    def search_username(self, username):
        count = self.__user_dao.search_username(username)
        return count

    # 添加用户
    def insert(self, username, password, email, rold_id):
        self.__user_dao.insert(username, password, email, rold_id)

    # 查询用户总页数
    def search_count_page(self):
        count_page = self.__user_dao.search_count_page()
        return count_page

    # 查询用户分页记录
    def search_list(self, page):
        result = self.__user_dao.search_list(page)
        return result

    # 修改用户信息
    def update(self, id, username, password, email, role_id):
        self.__user_dao.update(id, username, password, email, role_id)

    # 删除用户
    def delete_by_id(self, id):
        self.__user_dao.delete_by_id(id)
