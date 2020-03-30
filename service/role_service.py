# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from db.role_dao import RoleDao


class RoleService(object):
    __role_dao = RoleDao()

    # 查询角色列表
    def search_list(self):
        result = self.__role_dao.search_list()
        return result
