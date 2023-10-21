# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.expected_conditions import alert_is_present

class TestHod():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_hod(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1549, 955)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("22222221")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("password")
    self.driver.find_element(By.ID, "submit").click()
    print("Login successfully")
    self.driver.find_element(By.LINK_TEXT, "Comment History").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .read-details-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".read-close-btn").click()
    print("Comment History successfully")
    self.driver.find_element(By.LINK_TEXT, "View Workload").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) a").click()
    self.driver.find_element(By.ID, "exampleFormControlTextarea1").click()
    self.driver.find_element(By.ID, "exampleFormControlTextarea1").send_keys("test comment")
    self.driver.find_element(By.CSS_SELECTOR, ".send-comment").click()
    print("Comment successfully")
    WebDriverWait(self.driver, 10).until(alert_is_present())
    alert = self.driver.switch_to.alert
    alert.accept()
    self.driver.find_element(By.LINK_TEXT, "Comment History").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .read-details-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".read-close-btn").click()
    print("Read Comment Successfully")
    self.driver.find_element(By.LINK_TEXT, "View Workload").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) a").click()
    self.driver.find_element(By.ID, "AdjustedHours").click()
    self.driver.find_element(By.ID, "AdjustedHours").send_keys("1000")
    self.driver.find_element(By.CSS_SELECTOR, ".container:nth-child(4)").click()
    self.driver.find_element(By.ID, "modify").click()
    WebDriverWait(self.driver, 10).until(alert_is_present())
    alert = self.driver.switch_to.alert
    alert.accept()
    print("Modify successfully")
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
if __name__ == "__main__":
    test = TestHod()
    test.setup_method(None)

    try:
        test.test_hod()
        print("Test passed successfully")
    except Exception as e:
        print("Test failed", e)
    finally:
        test.teardown_method(None)