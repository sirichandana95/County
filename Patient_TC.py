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

        # xpath, clicks on add patient button
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
        time.sleep(2)

        #fillig out the add patient form
        elem = driver.find_element_by_id("id_PatientID")
        elem.send_keys("14")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Status")
        elem.send_keys("Active")
        time.sleep(1)
        elem = driver.find_element_by_id("id_HospitalName")
        elem.send_keys("UNMC")
        time.sleep(1)

        elem = driver.find_element_by_id("id_FirstName")
        elem.send_keys("Jack")
        time.sleep(1)
        elem = driver.find_element_by_id("id_LastName")
        elem.send_keys("Wills")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Date_of_Birth")
        elem.send_keys("11, 11, 1994")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Gender")
        elem.send_keys("Male")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Department")
        elem.send_keys("Mental Health")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Injury_type")
        elem.send_keys("Others")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Condition_on_arrival")
        elem.send_keys("Good/Fair")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Room_No_If_Admitted")
        elem.send_keys("112")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Kin_Name")
        elem.send_keys("Kate Wills")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Relationship_To_Victim")
        elem.send_keys("Husband")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Triage_Tag_colour")
        elem.send_keys("Green")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Disposition_type")
        elem.send_keys("To home")
        time.sleep(1)


        #xpath, clicks on save button for add patient
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
        time.sleep(2)

        # xpath, clicks on patient button
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[3]/a").click()
        time.sleep(2)

        # xpath, clicks on edit  button
        elem = driver.find_element_by_xpath(
            "//*[@id='app-layout']/section/div/div/div/table/tbody/tr[1]/td[8]/a").click()
        time.sleep(2)

        # fillig out the add patient form
        elem = driver.find_element_by_id("id_FirstName")
        elem.clear()
        elem.send_keys("Mike")
        time.sleep(1)
        elem = driver.find_element_by_id("id_LastName")
        elem.clear()
        elem.send_keys("Mickles")
        time.sleep(1)

        # xpath, clicks on update button for edit patient
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/section/div/div/div/form/div[2]/button").click()
        time.sleep(2)


        # xpath, clicks on delete  button
        elem = driver.find_element_by_xpath(
            "//*[@id='app-layout']/section/div/div/div/table/tbody/tr[1]/td[9]/a").click()
        time.sleep(2)

        driver.switch_to.alert.accept()
        # xpath, clicks on update button for edit patient
        # elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div/form/div/button").click()
        # time.sleep(2)
        #
        # xpath, clicks on more option
        # elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[4]/a").click()
        # time.sleep(2)
        # xpath, clicks on logout
        # elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[4]/ul/li[1]/a").click()
        # time.sleep(2)

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

