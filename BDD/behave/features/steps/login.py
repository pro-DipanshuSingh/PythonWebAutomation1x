from selenium import webdriver
from behave import Given, When, Then
from selenium.webdriver.common.by import By
@Given('i am on "loginpage"')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://qa.criticalmention.com")
@When('valid {"username"} and {"password"}')
def step_impl(context, password, username):
    username = context.browser.find_element(by=By.XPATH, value="//input[@id='username']")
    username.send_keys("dsingh@criticalmention.com")
    continue_btn = context.browser.find_element(by=By.XPATH, value="//button[normalize-space()='Continue']")
    continue_btn.click()
    password = context.browser.find_element(by=By.XPATH, value="//input[@id='password']")
    password.send_keys("welcome123")
    submit_btn = context.browser.find_element(by=By.XPATH, value="//button[@name = 'action']")
    submit_btn.click()

@Then('Verify the User gets successfully logged into the platform and the Dashboard page is displayed')
def step_impl(context ):
    headline = context.browser.find_element(by=By.XPATH,
                                   value="//div[@class='nav-bar__links']//span[@class='nav-link__text font--semi-bold'][normalize-space()='Dashboard']")
    assert headline.text == "Dashboard"
    context.browser.quit()


