# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
# 实现新闻管理系统

__author__ = 'LaoTan'

from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserSercicr
from service.news_service import NewsService
from service.role_service import RoleService
import os
import sys
import time

__user_service = UserSercicr()
__news_service = NewsService()
__role_service = RoleService()

try:
    while True:
        os.system("cls")  # 清理屏幕
        print(Fore.LIGHTBLUE_EX, "\n\t====================")
        print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
        print(Fore.LIGHTBLUE_EX, "\n\t====================")
        print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
        print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
        print(Style.RESET_ALL)
        opt = input("\n\t输入操作编号：")
        if opt == "1":
            username = input("\n\t用户名：")
            password = getpass("\n\t密码：")  # 用getpass()隐藏输入的密码
            result = __user_service.login(username, password)
            if result == True:
                # 查询角色
                role = __user_service.search_user_role(username)
                while True:
                    os.system("cls")
                    if role == "新闻编辑":
                        # print("新闻编辑功能还没开放——————-")
                        pass
                    elif role == "管理员":
                        print(Fore.LIGHTBLUE_EX, "\n\t1.新闻管理")
                        print(Fore.LIGHTBLUE_EX, "\n\t2.用户管理")
                        print(Fore.LIGHTGREEN_EX, "\n\tback.退出登录")
                        print(Fore.LIGHTGREEN_EX, "\n\texit.退出系统")
                        print(Style.RESET_ALL)
                        opt = input("\n\t输入操作编号：")
                        if opt == '1':
                            while True:
                                os.system("cls")
                                print(Fore.LIGHTBLUE_EX, "\n\t1.审批新闻")
                                print(Fore.LIGHTBLUE_EX, "\n\t2.删除新闻")
                                print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一步")
                                print(Style.RESET_ALL)
                                opt = input("\n\t输入操作编号：")
                                if opt == '1':
                                    page = 1
                                    while True:
                                        os.system("cls")
                                        count_page = __news_service.search_unreview_count_page()
                                        # 调用新闻事务查询没审批新闻的总数
                                        result = __news_service.seaech_unteview_list(page)
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLACK_EX,
                                                  "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                            # 列出没审批的新闻
                                        print(Fore.LIGHTWHITE_EX, "\n\t------------------")
                                        print(Fore.LIGHTBLACK_EX, "\n\t%d/%d" % (page, count_page))
                                        print(Fore.LIGHTWHITE_EX, "\n\t------------------")
                                        print(Fore.LIGHTBLUE_EX, "\n\tback.返回上一层")
                                        print(Fore.LIGHTBLUE_EX, "\n\tprev.上一页")
                                        print(Fore.LIGHTBLUE_EX, "\n\tnext.下一页")
                                        print(Fore.LIGHTBLUE_EX, "\n\t0.退出系统")
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t输入操作编号：")
                                        if opt == "back":
                                            break
                                        elif opt == "prev" and page >= 1:
                                            page -= 1
                                        elif opt == "next" and page <= count_page:
                                            page += 1
                                        elif int(opt) >= 1 and int(opt) <= 10:
                                            news_id = result[int(opt) - 1][0]
                                            __news_service.update_unreview_news(news_id)
                                        elif int(opt) == 0:
                                            sys.exit(0)
                                        else:
                                            print(Fore.LIGHTBLACK_EX, "\n\t输入有误，请重新输入")
                                elif opt == '2':
                                    page = 1
                                    while True:
                                        os.system("cls")
                                        count_page = __news_service.search_count_page()
                                        result = __news_service.search_list(page)
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLACK_EX,
                                                  "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                        print(Fore.LIGHTWHITE_EX, "\n\t------------------")
                                        print(Fore.LIGHTBLACK_EX, "\n\t%d/%d" % (page, count_page))
                                        print(Fore.LIGHTWHITE_EX, "\n\t------------------")
                                        print(Fore.LIGHTBLUE_EX, "\n\tback.返回上一层")
                                        print(Fore.LIGHTBLUE_EX, "\n\tprev.上一页")
                                        print(Fore.LIGHTBLUE_EX, "\n\tnext.下一页")
                                        print(Fore.LIGHTBLUE_EX, "\n\t0.退出系统")
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t输入操作编号：")
                                        if opt == "back":
                                            break
                                        elif opt == "prev" and page >= 1:
                                            page -= 1
                                        elif opt == "next" and page <= count_page:
                                            page += 1
                                        elif int(opt) >= 1 and int(opt) <= 10:
                                            news_id = result[int(opt) - 1][0]
                                            __news_service.delete_by_id(news_id)
                                        elif int(opt) == 0:
                                            sys.exit(0)
                                elif opt == "back":
                                    break
                                else:
                                    print(Fore.LIGHTBLACK_EX, "\n\t输入有误，请重新输入")
                        elif opt == "2":
                            while True:
                                os.system("cls")
                                print(Fore.LIGHTBLUE_EX, "\n\t1.添加用户")
                                print(Fore.LIGHTBLUE_EX, "\n\t2.修改用户")
                                print(Fore.LIGHTBLUE_EX, "\n\t3.删除用户")
                                print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                print(Fore.LIGHTGREEN_EX, "\n\t0.退出系统")
                                print(Style.RESET_ALL)
                                opt = input("\n\t输入操作编号：")
                                if opt == "1":
                                    os.system("cls")
                                    username = input("\n\t用户名：")
                                    count = __user_service.search_username(username)
                                    if count == True:
                                        print(Fore.LIGHTBLUE_EX, "\n\t该用户名已存在，请不要重复添加(3秒自动返回)")
                                        time.sleep(3)
                                        continue
                                    password = getpass("\n\t密码：")
                                    repassword = getpass("\n\t重新输入密码：")
                                    if password != repassword:
                                        print("\n\t两次密码不一致(3秒自动返回)")
                                        time.sleep(3)
                                        continue
                                    email = input("\n\t邮箱：")
                                    result = __role_service.search_list()
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入角色编号:")
                                    role_id = result[int(opt) - 1][0]
                                    __user_service.insert(username, password, email, role_id)
                                    print(Fore.LIGHTGREEN_EX, "\n\t添加成功(3秒自动返回)")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                    print(Style.RESET_ALL)
                                    time.sleep(3)
                                elif opt == "2":
                                    page = 1
                                    while True:
                                        os.system("cls")
                                        count_page = __user_service.search_count_page()
                                        result = __user_service.search_list(page)
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLUE_EX,
                                                  "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                        print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                                        print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                        print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                                        print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                        print(Fore.LIGHTGREEN_EX, "\n\tprev.上一页")
                                        print(Fore.LIGHTGREEN_EX, "\n\tnext.下一页")
                                        print(Fore.LIGHTGREEN_EX, "\n\t0.退出系统")
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t输入操作编号:")
                                        if opt == "back":
                                            break
                                        elif opt == "prev" and page > 1:
                                            page -= 1
                                        elif opt == "next" and page < count_page:
                                            page += 1
                                        elif int(opt) >= 1 and int(opt) <= 10:
                                            os.system("cls")
                                            user_id = result[int(opt) - 1][0]
                                            username = input("\n\t新用户名:")
                                            password = getpass("\n\t新密码:")
                                            repassword = getpass("\n\t再次输入密码:")
                                            if password != repassword:
                                                print(Fore.LIGHTRED_EX, "\n\t两次密码不一致(3秒自动返回)")
                                                print(Style.RESET_ALL)
                                                time.sleep(3)
                                                break
                                            email = input("\n\t新邮箱:")
                                            result = __role_service.search_list()
                                            for index in range(len(result)):
                                                one = result[index]
                                                print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                            print(Style.RESET_ALL)
                                            opt = input("\n\t角色编号:")
                                            role_id = result[int(opt) - 1][0]
                                            opt = input("\n\t是否保存(Y/N):")
                                            if opt == "Y" or opt == "y":
                                                __user_service.update(user_id, username, password, email, role_id)
                                                print(Fore.LIGHTBLACK_EX, "\n\t保存成功(3秒自动返回)")
                                                time.sleep(3)
                                        elif opt == "0":
                                            sys.exit(0)
                                elif opt == "3":
                                    page = 1
                                    while True:
                                        os.system("cls")
                                        count_page = __user_service.search_count_page()
                                        result = __user_service.search_list(page)
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLUE_EX,
                                                  "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                        print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                                        print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                        print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                                        print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                        print(Fore.LIGHTGREEN_EX, "\n\tprev.上一页")
                                        print(Fore.LIGHTGREEN_EX, "\n\tnext.下一页")
                                        print(Fore.LIGHTGREEN_EX, "\n\t0.退出系统")
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t输入操作编号:")
                                        if opt == "back":
                                            break
                                        elif opt == "prev" and page > 0:
                                            page -= 1
                                        elif opt == "next" and page < count_page:
                                            page += 1
                                        elif opt == "0":
                                            sys.exit(0)
                                        else:
                                            try:
                                                if int(opt) >= 1 and int(opt) <= 10:
                                                    os.system("cls")
                                                    user_id = result[int(opt) - 1][0]
                                                    __user_service.delete_by_id(user_id)
                                                    print(Fore.LIGHTBLACK_EX, "\n\t删除成功(3秒自动返回)")
                                                    time.sleep(3)
                                            except Exception as e:
                                                print(e)
                                                print(Fore.LIGHTBLACK_EX, "\n\t删除失败(3秒自动返回)")
                                                time.sleep(3)
                                elif opt == "0":
                                    sys.exit(0)
                                else:
                                    print(Fore.LIGHTBLACK_EX, "\n\t输入有误，请重新输入")
                                    break
                        elif opt == "back":
                            break
                        elif opt == "exit":
                            print(Style.RESET_ALL)
                            sys.exit(0)
                        else:
                            print(Fore.LIGHTBLACK_EX, "\n\t输入有误，请重新输入")
                            time.sleep(1)
                            break
            else:
                print(Fore.LIGHTBLACK_EX, "\n\t登录失败(2秒自动返回)")
                time.sleep(2)
                print(Style.RESET_ALL)

        elif opt == "2":
            print("\n\t--已退出，欢迎下次使用--")
            sys.exit(0)
        else:
            print(Fore.LIGHTBLACK_EX, "\n\t输入有误，请重新输入")
            time.sleep(1)
except Exception as e:
    print(e)
