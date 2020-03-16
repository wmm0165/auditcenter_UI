import pytest

# 其实也可以通过url直接访问页面，不定位菜单也行
@pytest.fixture(scope='module', autouse=True)
def choose_audit_setting(driver):
    driver.find_element_by_css_selector("li:nth-of-type(5) span.menu-text").click()
