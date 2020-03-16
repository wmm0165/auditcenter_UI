import pytest
from selenium import webdriver
from config.cfg import *
import time


# 打开浏览器
@pytest.fixture(scope='session')
def driver():
    global _driver
    print('------------open browser------------')
    # 启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # _driver = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")  # 驱动chrome浏览器
    _driver = webdriver.Chrome("D:/soft/chromedriver.exe", chrome_options=option)  # 驱动谷歌浏览器
    # _driver = webdriver.Firefox() # 驱动火狐浏览器
    _driver.maximize_window()
    yield _driver
    print('------------close browser------------')
    _driver.quit()


@pytest.fixture(scope='session', autouse=True)
def login(driver):
    """登录"""
    driver.get(url)
    driver.find_element_by_id('name').send_keys(username)
    driver.find_element_by_css_selector("div.pwd-ipt>input").send_keys(password)
    driver.find_element_by_css_selector("button.login-button").click()
    time.sleep(2)
    driver.find_element_by_css_selector("div:nth-of-type(6)").click()
    time.sleep(2)

