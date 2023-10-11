import pytest
import allure

from locators.locators import SearchClaimsLocators, SearchResultsLocators
from pages.claims_pages.search_claims_form import SearchClaims
from utilities.data_reader import XlsxReader


@pytest.mark.usefixtures("setup")
class TestClaimSearch:
    @allure.title("Search flight test: one way")
    @allure.description("This is test of searching one way flight")
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_search_claims_data())
    def test_search_claim(self,data):
        search_claim = SearchClaims(self.driver)
        search_claim.open_page()
        search_claim.set_employee(data.employee_name)
        search_claim.set_reference_ID(data.reference_ID)
        search_claim.set_event(data.event)
        search_claim.set_from_date(data.status)
        search_claim.set_to_date(data.from_date)
        search_claim.set_status(data.to_date)
        search_claim.set_include(data.include)
        search_claim.search_perform()
        #assert results_title in self.driver.find_element(
            #*SearchResultsLocators.search_title).text
