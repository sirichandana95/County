import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class admin_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       driver = self.driver

       driver.get("https://urldefense.proofpoint.com/v2/url?u=http-3A__mavteam1.pythonanywhere.com_password-2Dreset_confirm_Mw_51l-2Dedf628a89744f7294e58_&d=DwICaQ&c=Cu5g146wZdoqVuKpTNsYHeFX_rg6kWhlkLF8Eft-wwo&r=e1ETXSw2aymaQuS5yJr5rkZ0fLYsLVSNUsJDiW-u9nY&m=ZIxSgqWZMIGsHJR1iru8fK4ydyTae4upgi2P4jVFe5w&s=glonN4RqMlZySjlE1INGTmcwcfyIDCdPdPb8-mOgJWU&e=")
       time.sleep(30)

       elem = driver.find_element_by_id("id_new_password1")
       elem.send_keys("teamISQA")
       time.sleep(30)
       elem = driver.find_element_by_id("id_new_password2")
       elem.send_keys("teamISQA")
       time.sleep(30)
       #Clicks on reset password button
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/div/button").click()
       time.sleep(30)





   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

