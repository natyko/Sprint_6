"""
Tests for the navigation functionality of the scooter application.
"""

import allure

from config import BASE_URL, ORDER_URL
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestNavigation:

    @allure.description("Test navigation to main page via Scooter logo")
    def test_navigation_via_scooter_logo(self, driver):
        driver.get(ORDER_URL)
        order_page = OrderPage(driver)

        order_page.click_scooter_logo()

        expected_url = BASE_URL

        order_page.wait_for_url_contains(expected_url)

        actual_url = driver.current_url
        assert (
            actual_url == expected_url
        ), f"Expected URL {expected_url}, got {actual_url}"

    @allure.description("Test navigation to Yandex via Yandex logo")
    def test_navigation_via_yandex_logo(self, driver):
        driver.get(BASE_URL)
        main_page = MainPage(driver)

        main_page.click_yandex_logo()

        expected_url_part = "dzen.ru"
        actual_url = driver.current_url

        assert (
            expected_url_part in actual_url
        ), f"Expected URL containing '{expected_url_part}', got '{actual_url}'"

        original_window = driver.window_handles[0]
        driver.switch_to.window(original_window)
