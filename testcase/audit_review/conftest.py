import pytest


@pytest.fixture(scope='module', autouse=True)
def choose_audit_optreview(driver):
    driver.find_element_by_css_selector("li:nth-of-type(2) li:nth-of-type(1)>span").click()
