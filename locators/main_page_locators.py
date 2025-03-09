from selenium.webdriver.common.by import By


class MainPageLocators:
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//button[text()='Заказать' and contains(@class, 'Button_Middle')]",
    )
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_ITEM_TEMPLATE = (By.XPATH, "//div[@class='accordion__item']/div[text()='{}']")
    FAQ_ITEM_PANEL_TEMPLATE = (
        By.XPATH,
        "//div[@class='accordion__item']/div[text()='{}']/parent::div/div[contains(@class, 'accordion__panel')]",
    )
    FAQ_ITEM_INDEX_TEMPLATE = (By.XPATH, "(//*[@class='accordion__button'])[{}]")
    FAQ_ITEM_PANEL_INDEX_TEMPLATE = (By.XPATH, "(//*[@class='accordion__panel'])[{}]")
