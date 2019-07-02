import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class admin_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "pooja"
       pwd = "8210mavteam1"
       driver = self.driver

       driver.get("http://mavteam1.pythonanywhere.com/")
       time.sleep(3)
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div[3]/div/p/a").click()
       time.sleep(8)

       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       assert "Logged In"
       time.sleep(2)
       # find element by xpath, click on more options
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/a").click()
       time.sleep(2)
       # find element by xpath, click on change password
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/ul/li[2]/a").click()
       time.sleep(3)

       elem = driver.find_element_by_id("id_old_password")
       elem.send_keys("8210mavteam1")
       time.sleep(2)
       elem = driver.find_element_by_id("id_new_password1")
       elem.send_keys("8210team1")
       time.sleep(2)
       elem = driver.find_element_by_id("id_new_password2")
       elem.send_keys("8210team1")
       time.sleep(2)

       # find element by xpath, click on change password
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
       time.sleep(3)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

