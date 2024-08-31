from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from configuration.config import TestData

class Login_page():
    def __init__(self, driver):
        self.driver = driver
        self.username_xpath = "//input[@name='loginId']"
        self.password_xpath = "//input[@id='lnPassword']"
        self.login_button_xpath = "//button[@id='lnLoginSubmit']"
        self.homepage="//button[text()='Dashboard']"
        self.error_message_xpath="//span[@class='prompt-title']"
        self.user_required_area1="//span[contains(@class,'label-error')][1]"
        self.password_required_area2="//label[contains(text(),'Password')]/following-sibling::span"
        self.company_logo="//img[@src='img/axioma_logo.png']"
        self.label_forgot_password="//button[@type='button']//span"
        self.forgot_password = "//button[@type='button']"
        self.title_login_panel="//h5[@class='title']"
        self.label_user="//div[@class='login-username']//label"
        self.label_password="//div[@class='login-password']//label"
        self.otp_panel="//div[@class='content']"
        self.enter_name_in_otp_panel="//input[@type='text']"
        self.request_otp_button="//button[@type='submit']"

    def open_qarf(self):
        time.sleep(5)
        self.driver.get(TestData.URL)
        time.sleep(2)

    def enter_credentials(self, username, password):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
    def click_login_button(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
    def verify_homepage(self):
        time.sleep(10)
        homepage_verify = self.driver.find_element(By.XPATH, self.homepage)
        assert homepage_verify.is_displayed()==True , "Dashboard button is not displayed"
        homepage=homepage_verify.text
    def verify_error_message(self):
        time.sleep(2)
        error_message = self.driver.find_element(By.XPATH, self.error_message_xpath)
        unittest.TestCase().assertTrue(error_message.is_displayed(), "Error message element is not displayed")
        error_message_text = error_message.text
    def required_user_message(self):
        required_user_element_text = self.driver.find_element(By.XPATH, self.user_required_area1).text
        unittest.TestCase().assertTrue(required_user_element_text == "Required", "Required user message does not match")
    def required_password_message(self):
        required_password_element_text = self.driver.find_element(By.XPATH, self.password_required_area2).text
        unittest.TestCase().assertTrue(required_password_element_text == "Required","Required password message does not match")
    def displayed_company_logo(self):
        comp_logo = self.driver.find_element(By.XPATH, self.company_logo)
        unittest.TestCase().assertTrue(comp_logo.is_displayed(), "Company logo is not displayed")
    def enable_forgot_password(self):
        enable_forgot = self.driver.find_element(By.XPATH, self.forgot_password)
        unittest.TestCase().assertTrue(enable_forgot.is_enabled(), "Forgot password is not enabled")
    def displayed_forgot_password(self):
        display_forgot = self.driver.find_element(By.XPATH, self.forgot_password)
        unittest.TestCase().assertTrue(display_forgot.is_displayed(), "Forgot password is not displayed")
    def enable_login_button(self):
        enable_lgn_btn=self.driver.find_element(By.XPATH, self.login_button_xpath)
        unittest.TestCase().assertTrue(enable_lgn_btn.is_enabled(), "Login button is not enabled")
    def displayed_login_button(self):
        display_lgn_btn=self.driver.find_element(By.XPATH, self.login_button_xpath)
        unittest.TestCase().assertTrue(display_lgn_btn.is_displayed(), "Login button is not displayed")
    def enable_user_textbox(self):
        user_enable_box=self.driver.find_element(By.XPATH, self.username_xpath)
        unittest.TestCase().assertTrue(user_enable_box.is_enabled(), "User textbox is not enabled")
    def displayed_user_textbox(self):
        user_txtbox=self.driver.find_element(By.XPATH, self.username_xpath).is_displayed()
        unittest.TestCase().assertTrue(user_txtbox.is_displayed(), "User textbox is not displayed")
    def enable_password_textbox(self):
        password_enable_box=self.driver.find_element(By.XPATH, self.password_xpath)
        unittest.TestCase().assertTrue(password_enable_box.is_enabled(), "Password textbox is not enabled")
    def displayed_password_textbox(self):
        password_txtbox=self.driver.find_element(By.XPATH, self.password_xpath)
        unittest.TestCase().assertTrue(password_txtbox.is_displayed(), "Password textbox is not displayed")
    def displayed_login_panel(self):
        login_panel=self.driver.find_element(By.XPATH, self.title_login_panel)
        unittest.TestCase().assertTrue(login_panel.is_displayed(), "Login panel is not displayed")
    def displayed_user_label(self):
        user_labl=self.driver.find_element(By.XPATH, self.label_user)
        unittest.TestCase().assertTrue(user_labl.is_displayed(), "User label is not displayed")
    def displayed_user_password(self):
        user_pass=self.driver.find_element(By.XPATH, self.label_password)
        unittest.TestCase().assertTrue(user_pass.is_displayed(), "User password label is not displayed")
    def click_forgot_password(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.forgot_password).click()
    def verify_otp_panel(self):
        displayed_otp_panel=self.driver.find_element(By.XPATH, self.otp_panel)
        unittest.TestCase().assertTrue(displayed_otp_panel.is_displayed(), "OTP panel is not displayed")
    def enter_username_in_otp_panel(self, username):
        self.driver.find_element(By.XPATH, self.enter_name_in_otp_panel).send_keys(username)
        time.sleep(5)
    def enable_request_otp_button(self):
        request_otp_button=self.driver.find_element(By.XPATH, self.request_otp_button)
        unittest.TestCase().assertTrue(request_otp_button.is_enabled(), "Request OTP button is not enabled")