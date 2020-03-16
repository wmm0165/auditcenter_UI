import pytest

@pytest.fixture(scope='module',autouse=True)
def choose_alert_message(driver):
    driver.find_element_by_css_selector("li:nth-of-type(3) span.menu-text").click()
