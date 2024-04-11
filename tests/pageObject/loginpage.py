#page locators
#page action
#webdriver initialization
#custom function
#no assertions here
from selenium.webdriver.common.by import By
class Loginpage():
    def __init__(self, driver):
        self.driver = driver
#pagelocators
    username= (By.ID, "login-username")
    password = (By.ID, "login-password")
    submit = (By.XPATH, "//span[@data-qa='ezazsuguuy']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")
#
#these arenormal tuple, we have to return these tuple

    def get_user(self):
        return self.driver.find_element(*Loginpage.username)

    def get_password(self):
        return self.driver.find_element(*Loginpage.password)

    def get_submitbtn(self):
        return self.driver.find_element(*Loginpage.submit)

    def get_error_message(self):
        return self.driver.find_element(*Loginpage.error_message)
    #pageactions
    def login_page(self, user, pwd):
        self.get_user().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submitbtn().click()


    def get_error_message_text(self):
        return self.get_error_message().text
