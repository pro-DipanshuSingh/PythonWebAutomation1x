from selenium import webdriver
import pytest
import allure
from tests.pageObject.loginpage import Loginpage
import tests.pageObject.Dashboardpage
from selenium import webdriver
import time
class Testlogin():

    @allure.epic("vwoLogin")
    @allure.feature("tc1: Positive testcase")
    @pytest.mark.usefixtures("setup")
    def test_vwologin(self, setup):
        driver = setup
        driver.get(self.url)
        loginpage = Loginpage(driver)
        loginpage.login_page(user=self.name, pwd=self.password)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)

    @allure.epic("VWO Login Test")
    @allure.feature('TC#0 - VWO App Negative Test')
    @pytest.mark.usefixtures("setup")
    def test_vwologin_negative(self, setup):
        driver = setup
        driver.get(self.url)
        loginPage = Loginpage(driver)
        loginPage.login_page(user="admin", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
        time.sleep(2)

