from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
class Change_Password:
    def __init__(self, driver):
        self.driver = driver
        self.user_icon = "//div//div[@class='rtui-button-icon']//i[@class='rtui-icon-user']"
        self.change_password_button= "//div[text()='Change Password']"
        self.change_password_page="//div[ @class ='rtui-section changepassword-modal-section']"
        self.change_password_layout_panel="//h5[@class='title' and text()='Change Password']"
        self.cancel_page="(//div[@class='rtui-section changepassword-modal-section']//button[2])[1]"
    def clicks_on_change_password(self):
        self.driver.find_element(By.XPATH, self.user_icon).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.change_password_button).click()
    def change_password_page_display(self):
        time.sleep(2)
        change_password_page=self.driver.find_element(By.XPATH,self.change_password_page)
        unittest.TestCase().assertTrue(change_password_page.is_displayed(), "Change password page is not displayed")
        time.sleep(5)
    def change_password_layout(self):
        time.sleep(5)
        layout_panel=self.driver.find_element(By.XPATH,self.change_password_layout_panel)
        unittest.TestCase().assertTrue(layout_panel.is_displayed(), "Layout panel not displayed")
    def password_cancel_page(self):
        time.sleep(2)
        cancel_button = self.driver.find_element(By.XPATH, self.cancel_page)
        self.driver.execute_script("arguments[0].click();", cancel_button)
        time.sleep(2)