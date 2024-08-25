from selenium import webdriver
class WebDriverSetup:
    def __init__(self, context):
        self.context = context
        self.driver= None
    def get_driver(self):
        if not self.driver:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.context.driver =self.driver
        return self.driver

