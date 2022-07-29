import pytest
from PageObject.Log import log
from Utility.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utility/input.properties")

@pytest.mark.usefixtures('setup')
class Testlog(logclass):
    def testlog(self,setup):
        lg = self.getthelogs()
        log1 = log(self.driver)
        self.driver.implicitly_wait(10)
        lg.info("TestCase 001")
        log1.click_Contact_Us()
        log1.input_name()
        log1.input_email()
        log1.input_number()
        log1.input_text()
        log1.upload_file()
        log1.click_on_submit()
    #
    #     self.driver.find_element(by=By.XPATH,
    #                              value="//body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").click()
    #     lg.info("Verify the Title")
    #     if self.driver.title == 'Datacrest':
    #         assert True
    #         lg.info("TestCase Passed")
    #     else:
    #         lg.critical("TestCase Failed")
    #         self.driver.save_screenshot('Screenshots\\testlogin-001.png')
    #         assert False
    #
    #
    # def testInvalidUsername(self,setup):
    #     lg = self.getthelogs()
    #     self.driver.implicitly_wait(10)
    #     lg.info("TestCase 002")
    #     lg.info("Entering UserID")
    #     self.driver.find_element(by=By.XPATH, value="//body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]").click()
    #     lg.info("Verifying Message after invalid credential")
    #
    # def testlogin_user_URL(self):
    #     self.driver1 = webdriver.Chrome(executable_path="Utility/chromedriver.exe")
    #     self.driver1.get("https://insights-aurora.com/dataCrest")
    #     self.driver1.maximize_window()
    #     if self.driver1.title == 'Sign In':
    #         assert True
    #     else:
    #         self.driver1.save_screenshot('Screenshots\\testlogin-005.png')
    #         assert False
    #     self.driver1.quit()
