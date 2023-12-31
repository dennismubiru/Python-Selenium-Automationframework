import pytest
import allure

from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("Home page - smoke test")
    @allure.description("Check if home page has good title")
    def test_homepage_title(self):
        homepage = HomePage(self.driver)
        homepage.open()
        assert("STORE" in homepage.get_page_title())
