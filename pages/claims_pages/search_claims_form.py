import time
import allure
from allure_commons.types import AttachmentType
from locators.locators import SearchClaimsLocators
from utilities.functions import set_claims_values


class SearchClaims:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening opensource-demo.OrangeHRM website")
    def open_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    @allure.step("Setting destination to '{1}'")
    def claim_link(self):
        self.driver.find_element(*SearchClaimsLocators.Claim_text).click()

    @allure.step("entering new search values")
    def set_employee(self, employee_name):
        self.driver.find_element(*SearchClaimsLocators.employee_name).click()
        time.sleep(5)
        self.driver.find_element(*SearchClaimsLocators.employee_name).send_keys(employee_name)

    def set_reference_ID(self, reference_ID):
        self.driver.find_element(*SearchClaimsLocators.reference_ID).click()
        time.sleep(5)
        self.driver.find_element(*SearchClaimsLocators.reference_ID).send_keys(reference_ID)

    def set_event(self, event_name):
        self.driver.find_element(*SearchClaimsLocators.event_name).click()
        time.sleep(5)
        self.driver.find_element(*SearchClaimsLocators.event_name).send_keys(event_name)

    def set_status(self, status):
        self.driver.find_element(*SearchClaimsLocators.status).click()
        time.sleep(5)
        self.driver.find_element(*SearchClaimsLocators.status).send_keys(status)

    def set_from_date(self, from_date):
        self.driver.find_element(*SearchClaimsLocators.from_date).click()
        time.sleep(5)
        self.driver.find_element(*SearchClaimsLocators.from_date).send_keys(from_date)

    def set_to_date(self, to_date):
        self.driver.find_element(*SearchClaimsLocators.to_date).click()
        time.sleep(5)
        self.driver.find_element(*SearchClaimsLocators.to_date).send_keys(to_date)

    def set_include(self, include):
        self.driver.find_element(*SearchClaimsLocators.include).click()
        time.sleep(5)
        self.driver.find_element(*SearchClaimsLocators.include).send_keys(include)

    @allure.step("Performing search")
    def search_perform(self):
        self.driver.find_element(*SearchClaimsLocators.search_button).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)
