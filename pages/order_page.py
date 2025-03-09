import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Click on Scooter logo to navigate to main page")
    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)
        self.wait_for_url_contains(self.base_url)
        return self

    @allure.step("Click on Yandex logo to navigate to Yandex")
    def click_yandex_logo(self):
        original_handles = self.get_window_handles()

        self.click_element(self.locators.YANDEX_LOGO)

        self.switch_to_new_window(original_handles)

        self.wait_for_url_contains("dzen.ru")
        return self

    @allure.step("Fill first order form")
    def fill_first_order_form(self, name, surname, address, phone):
        self.find_element(self.locators.NAME_FIELD).send_keys(name)
        self.find_element(self.locators.SURNAME_FIELD).send_keys(surname)
        self.find_element(self.locators.ADDRESS_FIELD).send_keys(address)
        self.click_element(self.locators.METRO_STATION_FIELD)
        self.click_element(self.locators.METRO_STATION_OPTION)
        self.find_element(self.locators.PHONE_FIELD).send_keys(phone)
        self.click_element(self.locators.NEXT_BUTTON)
        return self

    @allure.step("Fill second order form")
    def fill_second_order_form(self, rent_period, color, comment):
        self.click_element(self.locators.DATE_FIELD)
        self.click_element(self.locators.DATE_OPTION)

        self.click_element(self.locators.RENT_PERIOD_FIELD)
        period_option = (
            self.locators.RENT_PERIOD_OPTION_TEMPLATE[0],
            self.locators.RENT_PERIOD_OPTION_TEMPLATE[1].format(rent_period),
        )
        self.click_element(period_option)

        if color.lower() == "black":
            self.click_element(self.locators.BLACK_COLOR)
        elif color.lower() == "grey":
            self.click_element(self.locators.GREY_COLOR)

        self.find_element(self.locators.COMMENT_FIELD).send_keys(comment)

        self.click_element(self.locators.ORDER_BUTTON)
        return self

    @allure.step("Confirm order")
    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_BUTTON)
        return self

    @allure.step("Get order completed text")
    def get_order_completed_text(self):
        return self.find_element(self.locators.ORDER_COMPLETED_TEXT).text

    @allure.step("Check if order is completed")
    def is_order_completed(self):
        return self.find_element(self.locators.ORDER_COMPLETED_MODAL) is not None

    @allure.step("Wait for page to load")
    def wait_for_page_loaded(self):
        super().wait_for_page_loaded()
        return self
