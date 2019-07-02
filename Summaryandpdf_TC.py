import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "kalpana"
        pwd = "team8210"
        driver = self.driver

        driver.get("http://mavteam1.pythonanywhere.com/")
        time.sleep(2)

        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Logged In"
        time.sleep(2)
        #xpath, clicks on nurse button on the top of the page
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
        time.sleep(2)
        # xpath, clicks on patient button
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[3]/a").click()
        time.sleep(2)
        # xpath, clicks on summary button
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/table/tbody/tr/td[10]/a").click()
        time.sleep(2)
        # xpath, clicks on Generatepdf button
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/div[18]/a").click()
        time.sleep(2)

        # xpath, clicks on more option
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/a").click()
        time.sleep(2)
        # xpath, clicks on logout
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/ul/li[1]/a").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

