import time
from behave import given, when, then
from pages.login_page import Login_page
from pages.logout_page import Logout_page
from pages.change_password import Change_Password
from utils.common import WebDriverSetup
from configuration.config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('The user navigates to login page')
def navigate_login_page(context):
    context.utils = WebDriverSetup(context)
    context.driver = context.utils.get_driver()
    context.driver.maximize_window()
    context.login_page = Login_page(context.driver)
    context.logout_page = Logout_page(context.driver)
    context.change_password = Change_Password(context.driver)
    context.login_page.open_qarf()
    time.sleep(5)
@when('The user enters a valid username and password')
def enter_credential(context):
    time.sleep(5)
    context.login_page.enter_credentials(TestData.USERNAME,TestData.PASSWORD)
@when('The user enters an invalid username and password')
def enter_invalid_credential(context):
    context.login_page.enter_credentials('abc', 'xyz')
@when('The user enters empty username and password')
def empty_credential(context):
    context.login_page.enter_credentials('', '')
@when('the user clicks on the Login button')
def the_user_click_on_login_button(context):
    time.sleep(5)
    context.login_page.click_login_button()
    time.sleep(10)
@then('the user navigates to the home page')
def verify_homepage(context):
    time.sleep(5)
    context.login_page.verify_homepage()
@then('the user should see error message')
def verify_error_message(context):
    time.sleep(5)
    error_message = context.login_page.verify_error_message()
@when('the users clicks on logout button')
def clicks_logout_button(context):
    context.logout_page.logout()
    time.sleep(2)
@then('the user should see required field validation message')
def validate_required_message(context):
    context.login_page.required_user_message()
    context.login_page.required_password_message()
@then('the user should see login panel layout')
def user_should_see_login_panel_layout(context):
    context.login_page.displayed_company_logo()
@then('the forgot password should be enabled')
def forgot_password_enabled(context):
    context.login_page.enable_forgot_password()
@then('the forgot password should be displayed')
def forgot_password_should_be_displayed(context):
    context.login_page.displayed_forgot_password()
@then('the login button should be enabled')
def login_button_should_be_enabled(context):
    context.login_page.enable_login_button()
@then('the login button should be displayed')
def login_button_should_be_displayed(context):
    context.login_page.displayed_login_button()
@then('the user textbox should be enabled')
def user_textbox_should_be_enabled(context):
    context.login_page.enable_user_textbox()
@then('the user textbox should be displayed')
def user_textbox_should_be_displayed(context):
    context.login_page.displayed_user_textbox()
@then('the password textbox should be enabled')
def password_textbox_should_be_enabled(context):
    context.login_page.enable_password_textbox()
@then('the password textbox should be displayed')
def password_textbox_should_be_displayed(context):
    context.login_page.displayed_password_textbox()
@then('the user label should be displayed')
def user_label_should_be_displayed(context):
    context.login_page.displayed_user_label()
@then('the password label should be displayed')
def password_label_should_be_displayed(context):
    context.login_page.displayed_user_password()
@when('the user clicks on the forget password')
def click_forgot_password(context):
    context.login_page.click_forgot_password()
    time.sleep(5)
@then('the user navigate to the OTP panel')
def navigate_to_otp_panel(context):
    context.login_page.verify_otp_panel()
@then('the user verify the OTP panel layout')
def verify_otp_panel_layout(context):
    context.login_page.verify_otp_panel()
@when('the user enter the username in OTP panel')
def enter_username_otp_panel(context):
    context.login_page.enter_username_in_otp_panel(TestData.USERNAME)
@then('the request OTP button should enable')
def verify_request_otp_button(context):
    context.login_page.enable_request_otp_button()
@when('the users clicks on change password button')
def users_click_on_change_password_button(context):
    context.change_password.clicks_on_change_password()
@then('the user navigates to the change password page')
def user_navigates_to_the_change_password_page (context):
    context.change_password.change_password_page_display()
@then('the user should see change password panel layout')
def the_user_should_see_change_password_panel_layout (context):
    context.change_password.change_password_layout()
@when('the user clicks on cancel button')
def user_click_on_cancel_button(context):
    context.change_password.password_cancel_page()