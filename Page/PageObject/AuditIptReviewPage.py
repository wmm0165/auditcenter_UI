# -*- coding: utf-8 -*-
# @Time : 2020/3/12 17:23
# @Author : wangmengmeng
from Page.BasePage import BasePage


# 选择科室
# 选择病区
# 药品分类
# 药品名称
# 抗菌药物
# 注射药物
# 住院号
# 患者号
# 审方药师
# 医嘱状态
# 收藏分类
# 医嘱类型


class AuditIptReview(BasePage):
    def input_eventno(self, eno):
        """输入住院号"""
        self.send_keys('css selector','')

    def input_patientid(self, pid):
        """输入患者号"""
        self.send_keys('css selector','')
