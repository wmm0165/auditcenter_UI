import pytest
from Page.PageObject.PlanSettingPage import PlanSettingPage


@pytest.fixture(scope='module',autouse=True)
def choose_auditplan_setting(driver):
    driver.find_element_by_css_selector("li:nth-of-type(5) li:nth-of-type(1)>span").click()

@pytest.fixture(scope='module')
def auditplan_setting(driver):
    auditplan_setting_page = PlanSettingPage(driver)
    yield auditplan_setting_page
    # 遍历列表删除所有方案


