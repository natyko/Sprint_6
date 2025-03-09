"""
Tests for the FAQ functionality of the scooter application.
"""

import pytest
import allure
from pages.main_page import MainPage


@pytest.mark.usefixtures("driver")
@allure.feature("FAQ Section")
class TestFAQSection:

    @allure.title("Test all FAQ dropdowns")
    @pytest.mark.parametrize(
        "faq_index,expected_text_contains",
        [
            (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (2, "Пока что у нас так: один заказ — один самокат"),
            (3, "Допустим, вы оформляете заказ на 8 мая"),
            (4, "Только начиная с завтрашнего дня"),
            (5, "Пока что нет"),
            (6, "Самокат приезжает к вам с полной зарядкой"),
            (7, "Да, пока самокат не привезли"),
            (8, "Да, обязательно. Всем самокатов!"),
        ],
    )
    def test_faq_dropdown_by_index(self, driver, faq_index, expected_text_contains):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_faq_item_by_index(faq_index)
        panel_text = main_page.get_faq_item_panel_text_by_index(faq_index)

        assert (
            expected_text_contains in panel_text
        ), f"Expected text '{expected_text_contains}' not found in panel text '{panel_text}'"

    @allure.title("Print all FAQ content for debugging")
    def test_print_all_faq_content(self, driver):
        """Helper test to print the actual content of all FAQ items for debugging."""
        main_page = MainPage(driver)
        main_page.open_main_page()

        for i in range(1, 9):
            try:
                main_page.open_faq_item_by_index(i)
                text = main_page.get_faq_item_panel_text_by_index(i)
                print(f"FAQ {i} text: {text}")
                allure.attach(
                    f"FAQ {i} text: {text}",
                    name=f"faq_{i}_content",
                    attachment_type=allure.attachment_type.TEXT,
                )
            except Exception as e:
                print(f"Error getting FAQ {i}: {str(e)}")
                allure.attach(
                    f"Error getting FAQ {i}: {str(e)}",
                    name=f"faq_{i}_error",
                    attachment_type=allure.attachment_type.TEXT,
                )
