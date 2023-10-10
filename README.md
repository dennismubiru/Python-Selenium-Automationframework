
## Test Automation project

This a  sample format  of test automation project framework based on Selenium-Webdriver with Python automated tests based on https://opensource-demo.orangehrmlive.com/ demo website.This is an HRM open source management system.
The collection of tests contains:
- user login tests (correct / incorrect login and password
- employee claims

## Project Structure
Here you can find a short description of main directories and it's content
- [locators](locators) - there are locators of web elements in locators.py grouped in classes
- [pages](pages) - there are sets of method for each test step (notice: some repeated methods were moved to [functions.py](utils/functions.py))
- [tests](tests) - there are sets of tests for main functionalities of website
- [reports](reports) - if you run tests with Allure, tests reports will be saved in this directory
- [utilities](utils) - this directory contains files responsible for configuration, e.g. driver_factory.py for webdriver management or [read_xlsx.py](utils/read_xlsx.py) for reading input data from xlsx files included in project

## Project Features
- framework follows page object pattern
- data-driven tests - in most tests the option of loading data from an xlsx file has been implemented
- logger has been implemented in each step of test cases.
```
 
```

- The Frame work has ability to easily generate legible and attractive test reports using Allure 
- tests can be run on popular browsers - Chrome and Firefox are preconfigured in DriverFactory class and both can be select in [conftest.py](tests/conftest.py), e.g.
```
@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
```


## Getting Started

To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Run Automated Tests

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow. There are 2 versions of test in each test file. In general test cases you can easily modify test inputs. Data-driven tests base on xlsx files from [utils](utils) directory. 

## Generate Test Report

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest --alluredir=<reports directory path>
```
After that you need to use command:
```
$ allure serve <reports directory path>
```


Report is generated in Chrome browser.

