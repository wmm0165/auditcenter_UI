import pytest

@pytest.fixture(scope='module',autouse=True)
def choose_static(driver):
    driver.find_element_by_css_selector("li:nth-of-type(4) span.menu-text").click()
