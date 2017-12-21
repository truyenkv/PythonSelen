import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#get chrome path
class Login(unittest.TestCase):
   # @classmethod
    def setUp(self):
        # create new chrome session
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.get("http://goodjobs-dev.dynagility.us/login")
        self.email_field = self.driver.find_element_by_name("email")
        self.password_field = self.driver.find_element_by_name("password")
        self.login_button = self.driver.find_element_by_xpath("//button[contains(text(),'LOGIN')]")
        self.email_field.clear()
        self.email_field.send_keys("admin@yopmail.com")
        self.password_field.clear()
        self.password_field.send_keys("Voyen!1412")
        self.login_button.click()
    # def test_login_site(self):
    #     self.email_field = self.driver.find_element_by_name("email")
    #     self.password_field = self.driver.find_element_by_name("password")
    #     self.login_button = self.driver.find_element_by_xpath("//button[contains(text(),'LOGIN')]")
    #     self.email_field.clear()
    #     self.email_field.send_keys("admin@yopmail.com")
    #     self.password_field.clear()
    #     self.password_field.send_keys("Voyen!1412")
    #     self.login_button.click()

    def test_download_option(self):
        self.assertTrue(self.is_element_present(By.XPATH,"//a[contains(text(),'Manage')]"))

    def test_manage_company_is_show(self):
        manage_button = self.driver.find_element_by_xpath("//a[contains(text(),'Manage')]")
        manage_button.click();
        self.driver.implicitly_wait(10)
        self.assertTrue(self.is_element_present(By.XPATH,"//*[contains(text(),'Manage Administrators')]"))
    #@classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)