import allure
from selenium.webdriver.common.keys import Keys
from locators.locators import SetLoginLocators
from base.base_page import basepage


class LogInPage(basepage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Expanding account menu")
    def expand_account_menu(self):
        self.driver.find_element(*SetLoginLocators.user_account_menu).click()

    @allure.step("Opening login page")
    def open_login_page(self):
        self.driver.find_element(*SetLoginLocators.login_link).click()

    @allure.step("Login with email: '1'")
    def set_user_inputs(self, email, password):
        self.driver.find_element(*SetLoginLocators.email_input).click()
        self.driver.find_element(*SetLoginLocators.email_input).send_keys(email)
        self.driver.find_element(*SetLoginLocators.password_input).click()
        self.driver.find_element(
            *SetLoginLocators.password_input).send_keys(password, Keys.ENTER)

    @allure.step("Logout")
    def logout(self):
        self.driver.find_element(*SetLoginLocators.logout_link).click()