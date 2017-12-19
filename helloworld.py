import os
import unittest
from selenium import webdriver
#get chrome path
class Login(unittest.TestCase):
    def setUp(self):
        # create new chrome session
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.get("http://goodjobs-dev.dynagility.us/login")

    def test_login_site(self):
        self.email_field = self.driver.find_element_by_name("email")
        self.password_field = self.driver.find_element_by_name("password")
        self.login_button = self.driver.find_element_by_xpath("//button[contains(text(),'LOGIN')]")
        self.email_field.clear()
        self.email_field.send_keys("admin@yopmail.com")
        self.password_field.clear()
        self.password_field.send_keys("Voyen!1412")
        self.login_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=1)