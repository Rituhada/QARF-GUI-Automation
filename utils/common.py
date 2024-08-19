from selenium import webdriver
class WebDriverSetup:
    def __init__(self, context):
        self.context = context

    def get_driver(self):
        driver = webdriver.Chrome()
        self.context.driver = driver
        return driver
