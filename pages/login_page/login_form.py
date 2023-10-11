import time

import allure
from selenium.webdriver.common.keys import Keys
from locators.locators import SetLoginLocators
from base.base_page import basepage


class LogInPage(basepage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Opening opensource-demo.OrangeHRM website")
    def open_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    @allure.step("Login with username and password")
    def set_user_inputs(self, username, password):
        self.driver.find_element(*SetLoginLocators.username).click()
        time.sleep(5)
        self.driver.find_element(*SetLoginLocators.username).send_keys(username)
        self.driver.find_element(*SetLoginLocators.password).click()
        time.sleep(5)
        self.driver.find_element(
            *SetLoginLocators.password).send_keys(password, Keys.ENTER)

        self.driver.find_element(*SetLoginLocators.login_button).click()

    #@allure.step("Logout")
    #def logout(self):
        #self.driver.find_element(*SetLoginLocators.logout_link).click()
