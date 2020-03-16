import pytest
import time

@pytest.fixture(scope='module',autouse=True)
def choose_mission_list(driver):
    driver.find_element_by_css_selector("li:nth-of-type(1) span.menu-text").click()
    time.sleep(2)
