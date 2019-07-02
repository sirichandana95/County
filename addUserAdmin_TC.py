import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class admin_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver

       driver.get("http://mavteam1.pythonanywhere.com/")
       time.sleep(3)

       driver.get("http://mavteam1.pythonanywhere.com/admin/")
       time.sleep(3)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       assert "Logged In"
       time.sleep(2)
       # find element by xpath, click on user
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/th/a").click()
       time.sleep(2)
       # find element by xpath, click on add user
       elem = driver.find_element_by_xpath("//html/body/div/div[3]/div/ul/li/a").click()
       time.sleep(3)

       elem = driver.find_element_by_id("id_username")
       elem.send_keys("Selenium")
       time.sleep(2)
       elem = driver.find_element_by_id("id_password1")
       elem.send_keys("s1u2j3u4")
       time.sleep(2)
       elem = driver.find_element_by_id("id_password2")
       elem.send_keys("s1u2j3u4")
       time.sleep(2)

       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
       time.sleep(3)


       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("Selenium")
       time.sleep(2)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Test")
       time.sleep(2)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("suv@gmail.com")
       time.sleep(2)

       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       time.sleep(3)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

