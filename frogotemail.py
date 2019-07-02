import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        #user = "instructor"
        #pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mavteam1.pythonanywhere.com/")
        time.sleep(2)
        # clicks on login
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/a").click()
        time.sleep(2)

        # clicks on forgot password
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div[1]/form/div[2]/button[2]/a").click()
        time.sleep(2)

        #give email
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("pkanaganti@unomaha.edu")
        time.sleep(2)

        # clicks on forgot password
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

