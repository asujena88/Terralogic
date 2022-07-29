from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import configparser
config = configparser.ConfigParser()
config.read("Utility/input.properties")


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome(executable_path="Utility/chromedriver.exe")
    driver.get(config.get("url","url"))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


class utility:
    @staticmethod
    def wait_for_element(driver, element):
        try:
            WebDriverWait(driver,20).until(ec.visibility_of(element))
            return True
        except:
            return False
