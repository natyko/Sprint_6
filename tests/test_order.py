"""
Tests for the order process of the scooter application.
"""

import pytest
import allure

from data import TOP_BUTTON_ORDER_DATA, BOTTOM_BUTTON_ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.mark.usefixtures("driver")
@allure.feature("Order Flow")
class TestOrderFlow:

    @allure.title("Test scooter order using top button")
    @pytest.mark.parametrize("order_data", TOP_BUTTON_ORDER_DATA)
    def test_order_with_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Order scooter using top button"):
            main_page.open_main_page()
            main_page.click_top_order_button()

            order_page.fill_first_order_form(
                order_data["name"],
                order_data["surname"],
                order_data["address"],
                order_data["phone"],
            )

            order_page.fill_second_order_form(
                order_data["rent_period"], order_data["color"], order_data["comment"]
            )

            order_page.confirm_order()

            assert order_page.is_order_completed(), "Order is not completed"

            completion_text = order_page.get_order_completed_text()

            assert (
                "Номер заказа:" in completion_text
            ), f"Order completion text '{completion_text}' doesn't contain order number information"

    @allure.title("Test scooter order using bottom button")
    @pytest.mark.parametrize("order_data", BOTTOM_BUTTON_ORDER_DATA)
    def test_order_with_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Order scooter using bottom button"):
            main_page.open_main_page()
            main_page.click_bottom_order_button()

            order_page.fill_first_order_form(
                order_data["name"],
                order_data["surname"],
                order_data["address"],
                order_data["phone"],
            )

            order_page.fill_second_order_form(
                order_data["rent_period"], order_data["color"], order_data["comment"]
            )

            order_page.confirm_order()

            assert order_page.is_order_completed(), "Order is not completed"

            completion_text = order_page.get_order_completed_text()

            assert (
                "Номер заказа:" in completion_text
            ), f"Order completion text '{completion_text}' doesn't contain order number information"
