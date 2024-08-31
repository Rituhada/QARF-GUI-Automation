from utils.common import WebDriverSetup

def before_scenario(context, scenario):
    context.utils = WebDriverSetup(context)
    context.driver = context.utils.get_driver()
    context.driver.maximize_window()
def after_scenario(context, scenario):
    context.driver.quit()

