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

       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/a").click()
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
       # find element by xpath, click on co-ordinator
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
       time.sleep(2)
       # find element by xpath, click on create event
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/section/div/div/div[3]/div/p/a').click()
       time.sleep(3)

       elem = driver.find_element_by_id("id_EventID")
       elem.send_keys("16")
       time.sleep(2)
       elem = driver.find_element_by_id("id_EventName")
       elem.send_keys("Fire")
       time.sleep(2)
       elem = driver.find_element_by_id("id_EventDescription")
       elem.send_keys("Fire at a clothing factory")
       time.sleep(2)
       elem = driver.find_element_by_id("id_EventLocation")
       elem.send_keys("Omaha")
       time.sleep(2)
       elem = driver.find_element_by_id("id_InjuryLevel")
       elem.send_keys("serious")
       time.sleep(2)
       elem = driver.find_element_by_id("id_NumberofPatients")
       elem.send_keys("8")
       time.sleep(2)
       elem = driver.find_element_by_id("id_user")
       elem.send_keys("pooja")
       time.sleep(2)

       elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
       time.sleep(3)
       # find element by xpath, click on event summary
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul/li[3]/a").click()
       time.sleep(3)

# edits the event
       # xpath, clicks on edit  button
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/table/tbody/tr[1]/td[9]/a").click()
       time.sleep(2)

       # fillig out the add patient form
       elem = driver.find_element_by_id("id_EventLocation")
       elem.clear()
       elem.send_keys("West Omaha")
       time.sleep(1)
       elem = driver.find_element_by_id("id_NumberofPatients")
       elem.clear()
       elem.send_keys("10")
       time.sleep(1)

       # xpath, clicks on update button for edit event
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
       time.sleep(2)
       # xpath, clicks on more option
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul/li[4]/a").click()
       time.sleep(2)
       # xpath, clicks on logout
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul/li[4]/ul/li[1]/a").click()
       time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

