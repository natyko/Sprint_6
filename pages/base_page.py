from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from config import BASE_URL, DEFAULT_TIMEOUT


class BasePage:
    BASE_URL = None

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL
        self.default_timeout = DEFAULT_TIMEOUT

    def get_url(self, url):
        """Navigate to the specified URL using the driver."""
        self.driver.get(url)

    def open(self):
        """Open the base URL of the page."""
        self.get_url(self.base_url)

    def get_current_url(self):
        """Get the current URL of the browser."""
        return self.driver.current_url

    def wait_for_element_visible(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} not visible after {timeout} seconds",
        )

    def wait_for_element_clickable(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} not clickable after {timeout} seconds",
        )

    def wait_for_element_present(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Element {locator} not present after {timeout} seconds",
        )

    def wait_for_elements_present(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Elements {locator} not present after {timeout} seconds",
        )

    def wait_for_url_contains(self, url_part, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part),
            message=f"URL did not contain {url_part} after {timeout} seconds",
        )

    def wait_for_new_window(self, current_handles, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len(current_handles),
            message=f"New window did not open after {timeout} seconds",
        )

    def find_element(self, locator, timeout=None):
        return self.wait_for_element_present(locator, timeout)

    def find_elements(self, locator, timeout=None):
        return self.wait_for_elements_present(locator, timeout)

    def click_element(self, locator, timeout=None):
        element = self.wait_for_element_clickable(locator, timeout)
        WebDriverWait(self.driver, 0.5).until(lambda d: True, message="")
        element.click()

    def scroll_to_element(self, locator, timeout=None):
        element = self.wait_for_element_present(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        WebDriverWait(self.driver, 0.5).until(lambda d: True, message="")
        return element

    def switch_to_new_window(self, original_handles=None):
        if original_handles is None:
            original_handles = [self.driver.current_window_handle]

        self.wait_for_new_window(original_handles)

        for handle in self.driver.window_handles:
            if handle not in original_handles:
                self.driver.switch_to.window(handle)
                break

        WebDriverWait(self.driver, self.default_timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete",
            message="New page did not load completely",
        )

    def switch_to_window(self, handle):
        """Switch to a specific window handle."""
        self.driver.switch_to.window(handle)
        self.wait_for_page_loaded()

    def get_window_handles(self):
        """Get all current window handles."""
        return self.driver.window_handles

    def wait_for_page_loaded(self, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete",
            message=f"Page did not load completely after {timeout} seconds",
        )

    def wait_for_animation_complete(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_timeout

        element = self.wait_for_element_present(locator, timeout)
        last_location = None

        def location_unchanged(driver):
            nonlocal last_location, element
            try:
                current_location = element.location
                if last_location == current_location:
                    return True
                last_location = current_location
                return False
            except StaleElementReferenceException:
                element = driver.find_element(*locator)
                last_location = element.location
                return False

        WebDriverWait(self.driver, timeout).until(
            location_unchanged,
            message=f"Element {locator} animation did not complete after {timeout} seconds",
        )
        return element
