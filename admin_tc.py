import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "mavteam1"
        pwd = "8210mavteam1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mavteam1.pythonanywhere.com/")
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
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

        #xpath, clicks on admin button on the top of the page
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
        time.sleep(2)

        # xpath, clicks on manage user  button
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div[3]/div/p/a").click()
        time.sleep(2)

        # xpath, clicks on all users  button
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div[3]/div/p/a").click()
        time.sleep(2)

        # xpath, clicks on add users  button
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div[2]/div/a/span").click()
        time.sleep(2)

        #fillig out the add patient form
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Iconic")
        time.sleep(1)
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Crew")
        time.sleep(1)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("Icrew@gmail.com")
        time.sleep(1)

        elem = driver.find_element_by_id("id_username")
        elem.send_keys("icrew")
        time.sleep(1)

        # xpath, clicks on save button for add user
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
        time.sleep(5)

        #user edit
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div[2]/table/tbody/tr[6]/td[6]/a").click()
        time.sleep(2)

        elem = driver.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys("JulieS")

        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
        time.sleep(8)

        # xpath, clicks on save button for delete user
        elem = driver.find_element_by_xpath(
            "//*[@id='app-layout']/section/div/div/div[2]/table/tbody/tr[6]/td[7]/a").click()
        time.sleep(2)

        driver.switch_to.alert.accept()
        time.sleep(3)

        # xpath, clicks on patient button on the top of the page
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[4]/a").click()
        time.sleep(2)

        # xpath, clicks on events button on the top of the page
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[3]/a").click()
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

