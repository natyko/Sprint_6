import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Open main page")
    def open_main_page(self):
        self.open()
        self.wait_for_page_loaded()
        self.wait_for_element_visible(self.locators.ORDER_BUTTON_TOP)
        return self

    @allure.step("Click on top order button")
    def click_top_order_button(self):
        self.click_element(self.locators.ORDER_BUTTON_TOP)
        self.wait_for_page_loaded()
        return self

    @allure.step("Click on bottom order button")
    def click_bottom_order_button(self):
        button = self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.wait_for_element_clickable(self.locators.ORDER_BUTTON_BOTTOM)
        button.click()
        self.wait_for_page_loaded()
        return self

    def verify_scooter_logo_present(self):
        element = self.wait_for_element_visible(self.locators.SCOOTER_LOGO)
        assert element.is_displayed(), "Scooter logo is not visible on the page"
        return self

    @allure.step("Click on Yandex logo")
    def click_yandex_logo(self):
        original_handles = self.driver.window_handles

        self.click_element(self.locators.YANDEX_LOGO)

        self.switch_to_new_window(original_handles)

        self.wait_for_url_contains("dzen.ru")
        return self

    @allure.step("Click on Scooter logo")
    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)
        # Wait for the main page URL to load
        self.wait_for_url_contains(BasePage.BASE_URL)
        return self

    @allure.step("Open FAQ item '{faq_text}'")
    def open_faq_item(self, faq_text):
        locator = (
            self.locators.FAQ_ITEM_TEMPLATE[0],
            self.locators.FAQ_ITEM_TEMPLATE[1].format(faq_text),
        )
        self.scroll_to_element(self.locators.FAQ_SECTION)
        self.click_element(locator)

        panel_locator = (
            self.locators.FAQ_ITEM_PANEL_TEMPLATE[0],
            self.locators.FAQ_ITEM_PANEL_TEMPLATE[1].format(faq_text),
        )
        self.wait_for_element_visible(panel_locator)

        self.wait_for_animation_complete(panel_locator)
        return self

    @allure.step("Get FAQ item text for '{faq_text}'")
    def get_faq_item_panel_text(self, faq_text):
        locator = (
            self.locators.FAQ_ITEM_PANEL_TEMPLATE[0],
            self.locators.FAQ_ITEM_PANEL_TEMPLATE[1].format(faq_text),
        )
        panel = self.wait_for_element_visible(locator)
        return panel.text

    @allure.step("Get all FAQ questions")
    def get_all_faq_questions(self):
        self.scroll_to_element(self.locators.FAQ_SECTION)
        items = self.wait_for_elements_present(
            (By.CSS_SELECTOR, ".accordion__item .accordion__heading")
        )
        return [item.text for item in items]

    @allure.step("Open FAQ item at index {index}")
    def open_faq_item_by_index(self, index):
        faq_section = self.find_element(self.locators.FAQ_SECTION)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", faq_section
        )

        self.wait_for_element_visible(self.locators.FAQ_SECTION)

        locator = (
            self.locators.FAQ_ITEM_INDEX_TEMPLATE[0],
            self.locators.FAQ_ITEM_INDEX_TEMPLATE[1].format(index),
        )

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        self.wait(0.5)

        self.driver.execute_script("arguments[0].click();", element)

        panel_locator = (
            self.locators.FAQ_ITEM_PANEL_INDEX_TEMPLATE[0],
            self.locators.FAQ_ITEM_PANEL_INDEX_TEMPLATE[1].format(index),
        )
        self.wait_for_element_visible(panel_locator)

        self.wait_for_animation_complete(panel_locator)
        return self

    @allure.step("Get FAQ item panel text at index {index}")
    def get_faq_item_panel_text_by_index(self, index):
        locator = (
            self.locators.FAQ_ITEM_PANEL_INDEX_TEMPLATE[0],
            self.locators.FAQ_ITEM_PANEL_INDEX_TEMPLATE[1].format(index),
        )
        panel = self.wait_for_element_visible(locator)
        return panel.text

    @allure.step("Wait for {seconds} seconds")
    def wait(self, seconds):
        import time

        time.sleep(seconds)
