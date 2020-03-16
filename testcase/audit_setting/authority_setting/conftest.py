# -*- coding: utf-8 -*-
# @Time : 2020/3/12 14:17
# @Author : wangmengmeng
import pytest

@pytest.fixture(scope='module',autouse=True)
def choose_authority_setting(driver):
    driver.find_element_by_css_selector("li:nth-of-type(5) li:nth-of-type(2)>span").click()
