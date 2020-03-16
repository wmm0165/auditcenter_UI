# -*- coding: utf-8 -*-
# @Time : 2019/9/2 22:25
# @Author : wangmengmeng
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile
from common.connect_db import ConnectDB
import pymysql
from common.compare import *


class PlanSettingPage(BasePage):
    do_conf = ParseConFile()
    addplan_btn = do_conf.get_locators_or_account('PlanSettingPageElements', 'addplan_btn')
    save_btn = do_conf.get_locators_or_account('PlanSettingPageElements', 'save_btn')
    planname = do_conf.get_locators_or_account('PlanSettingPageElements', 'planname')

    def add_plan(self, planname):
        """新增审方方案流程"""
        self.click_addplan_btn()
        self.input_planname(planname)
        self.click_save_btn()

    def query_flow(self, planname):
        """查询审方方案流程"""
        self.search_plan(planname)
        display = self.get_display_data()
        database = self.get_database_data(planname)
        return listdict_compare(display, database)

    def search_plan(self, planname):
        # 输入方案名称
        self.send_keys('css selector', 'input.audit-setting-search-input', planname)
        # 点击搜索
        self.click('css selector', '.ip-btn>span:nth-of-type(2)')

    def get_display_data(self):
        """获取页面的查询出的审方方案数据"""
        size = (self.find_element('css selector', 'span.v-middle')).text[2:-1]  # 获取总页数
        data_list = []
        data_dict = {}
        for i in range(int(size)):
            rows = len(self.find_elements('css selector', 'tbody>tr')) - 1
            for j in range(rows):
                j += 1
                ss = self.find_elements('css selector', 'tbody>tr:nth-of-type({}) td'.format(j+1))
                data_dict['name'] = ss[0].text
                data_dict['category'] = ss[1].text
                data_dict['user_name'] = ss[2].text
                # data_dict['created_time'] = ss[3].text
                # data_dict['modified_time'] = ss[4].text
                data_list.append(data_dict)
                if j < int(size):
                    self.click('css selector', 'span.-next-page')  # 点击下一页
        return data_list

    def get_database_data(self, planname):
        db = ConnectDB()
        cur = db.connect().cursor(pymysql.cursors.DictCursor)
        plan_name = 'where name = %s'  # SELECT name, category,user_name,created_time,modified_time
        cur.execute('SELECT name, category,user_name FROM `sf_audit_plan`' + plan_name,
                    planname)
        database_data = cur.fetchall()
        return database_data

    def plannames(self):
        """获取创建后的审方方案名称"""
        names = self.find_elements("css selector", "tbody>tr>td:nth-of-type(1)")
        return [ele.text for ele in names]

    def result(self, planname):
        plannames = self.plannames()
        if planname in plannames:
            return True
        else:
            return False

    def delete_plans(self):
        plans = self.find_elements("css selector", "tbody>tr button:nth-of-type(3)>span")
        for plan in plans:
            self.click('css selector', plan)

    def input_planname(self, planname):
        return self.send_keys(*PlanSettingPage.planname, planname)

    def click_addplan_btn(self):
        return self.click(*PlanSettingPage.addplan_btn)

    def click_save_btn(self):
        return self.click(*PlanSettingPage.save_btn)
