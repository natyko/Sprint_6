# Scooter Service Automated Tests

Automated test suite for the Scooter Service web application using Selenium WebDriver and Python.

## Project Structure

- `pages/` - Page Object classes for application pages
- `tests/` - Test cases organized by functionality
- `conftest.py` - Test configuration and fixtures
- `requirements.txt` - Project dependencies

## Test Coverage

The test suite verifies:
- FAQ section dropdown functionality
- Complete scooter ordering flow with multiple data sets
- Navigation via Scooter and Yandex logos

## Implementation Details

- Uses Page Object pattern to separate test logic from UI interactions
- Implements parameterized tests for multiple data scenarios
- Generates detailed test reports using Allure

## Setup and Running Tests

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run tests and generate Allure results:
    ```bash
    test --alluredir=allure-results

3. View the Allure report:
    ```bash
    allure serve allure-results