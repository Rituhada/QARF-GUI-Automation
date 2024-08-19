from selenium.webdriver.common.by import By
import time
class Logout_page:
    def __init__(self, driver):
        self.driver = driver
        self.user_icon_xpath = "//div//div[@class='rtui-button-icon']//i[@class='rtui-icon-user']"
        self.logout_button_xpath = "//div[text()='Logout']"
    def logout(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.user_icon_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()
        time.sleep(5)
        self.driver.quit()
