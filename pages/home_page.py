from base.base_page import basepage
import allure
class HomePage(basepage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title