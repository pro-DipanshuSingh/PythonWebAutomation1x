# Assertion
import time

import pytest
import allure
from tests.pageObject.loginpage import Loginpage
import tests.pageObject.Dashboardpage
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    return driver


@allure.epic("vwoLogin")
@allure.feature("tc1: Positive testcase")
def test_vwologin(setup):
    driver = setup
    loginpage = Loginpage(driver)
    loginpage.login_page(user="contact+atb5x@thetestingacademy.com", pwd="ATBx@1234")
    time.sleep(5)
    assert "Dashboard" in driver.title
    time.sleep(2)

@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
def test_vwologin_negative(setup):
    driver = setup
    loginPage = Loginpage(driver)
    loginPage.login_page(user="admin", pwd="admin")
    time.sleep(5)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    time.sleep(2)