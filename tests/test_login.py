import pytest
import allure
from locators.locators import SetLoginLocators
from pages.login_page.login_form import LogInPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_login_passed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_page()
        log_in_page.set_user_inputs("admin", "amin123")

    @allure.title("Login with invalid email test")
    @allure.description("This is test of login with invalid email")
    def test_login_failed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_page()
        log_in_page.set_user_inputs("admins", "admin1234")
        error_msg = "Invalid credentials"
        assert error_msg in self.driver.find_element(
            *SetLoginLocators.invalid_data_msg).text
