from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class log:
    def __init__(self, driver):
        self.driver = driver

    def click_Contact_Us(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Contact Us')]").click()

    def input_name(self):
        self.driver.find_element_by_xpath("//input[@id='full_name']").send_keys("abcde")

    def input_email(self):
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("abcde@gmail.com")

    def input_number(self):
        self.driver.find_element_by_xpath("//input[@id='phone_number']").send_keys("123456789")

    def input_text(self):
        self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys("abcde123456789")

    def upload_file(self):
        self.driver.find_element_by_xpath("//input[@id='attachment']").send_keys(
            "C:/Users/asutosh.jena/Downloads/701XXXXX3795.pdf")

    def click_on_submit(self):
        self.driver.find_element_by_tag_name("button").click()
