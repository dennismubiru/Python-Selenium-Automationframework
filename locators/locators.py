from selenium.webdriver.common.by import By


class SetLoginLocators:
    username = (By.XPATH, "//input[@placeholder='Username']")
    password = (By.XPATH, "//input[@placeholder='Password']")
    login = (By.XPATH, "//button[normalize-space()='Login']")
    invalid_data_msg = (By.XPATH, "//div[@class='oxd-alert-content oxd-alert-content--error']")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")


class SearchClaimsLocators:
    Claim_text = (By.XPATH, "//span[normalize-space()='Claim']")
    employee_name = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    reference_ID = (By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
    event_name = (By.XPATH, "(//div[contains(text(),'-- Select --')])[1]")
    status = (By.XPATH, "(//div[contains(text(),'-- Select --')])[2]")
    from_date = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
    to_date = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
    include = (By.XPATH, "(//div)[79]")
    reset_button = (By.XPATH, "//button[normalize-space()='Reset']")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")


class AddClaimsLocators:
    assign_claim = (By.XPATH, "//button[normalize-space()='Assign Claim']")
    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    event = (By.XPATH, "//input[@placeholder='Type for hints...']")
    currency = (By.XPATH, "(//div[contains(text(),'-- Select --')])[2]")
    remarks = (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
    create_button = (By.XPATH, "//button[normalize-space()='Cancel']")
    cancel_button = (By.XPATH, "//button[normalize-space()='Create']")


class SearchResultsLocators:
    search_title = (By.XPATH, "//span[@class='text-primary']")
