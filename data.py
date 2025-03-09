# Test data
TEST_ORDER_DATA = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Пушкина, д. 10",
        "phone": "+79001234567",
        "rent_period": "сутки",
        "color": "black",
        "comment": "Позвоните за час до доставки",
    },
    {
        "name": "Мария",
        "surname": "Петрова",
        "address": "ул. Ленина, д. 15",
        "phone": "+79009876543",
        "rent_period": "двое суток",
        "color": "grey",
        "comment": "Оставьте у консьержа",
    },
    {
        "name": "Александр",
        "surname": "Сидоров",
        "address": "ул. Гагарина, д. 5",
        "phone": "+79123456789",
        "rent_period": "трое суток",
        "color": "black",
        "comment": "Домофон не работает, позвоните",
    },
]

TOP_BUTTON_ORDER_DATA = TEST_ORDER_DATA[0:2]  # First two data sets for top button test
BOTTOM_BUTTON_ORDER_DATA = [TEST_ORDER_DATA[2]]  # Last data set for bottom button test
