# -*- coding: utf-8 -*-
# @Time : 2020/3/12 17:03
# @Author : wangmengmeng
import pytest


@pytest.fixture(scope='module', autouse=True)
def choose_audit_iptreview(driver):
    driver.find_element_by_css_selector("li:nth-of-type(2) li:nth-of-type(2)>span").click()
