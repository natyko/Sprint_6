from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Logo locators
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # First order form
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']/ul/li[1]")
    PHONE_FIELD = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Second order form
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_OPTION = (By.XPATH, "//div[@class='react-datepicker__month']/div[3]/div[1]")
    RENT_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-control']")
    RENT_PERIOD_OPTION_TEMPLATE = (
        By.XPATH,
        "//div[@class='Dropdown-menu']/div[text()='{}']",
    )

    # Scooter colors
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")

    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle') and text()='Заказать']",
    )

    # Confirmation modal
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_COMPLETED_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    ORDER_COMPLETED_TEXT = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader')]/div[contains(@class, 'Order_Text')]",
    )
