#URL
BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
COURIERS_URL = f'{BASE_URL}/courier'
COURIERS_LOGIN_URL = f'{COURIERS_URL}/login'
ORDERS_URL = f'{BASE_URL}/orders'

class OrderData:
    # Цвет черный
    ORDER_DATA_1 = {
        "firstName": "ТестИван",
        "lastName": "ТестИванов",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 22 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "comment_Black scooter",
        "color": ["BLACK"]
    }
    # Цвет и черный и белый
    ORDER_DATA_2 = {
        "firstName": "ТестИван",
        "lastName": "ТестИванов",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 22 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "comment_Black and Grey scooter",
        "color": ["BLACK", "GREY"]
    }
    # Без указания цвета
    ORDER_DATA_3 = {
        "firstName": "ТестИван",
        "lastName": "ТестИванов",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 22 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "comment_No color scooter",
        "color": []
    }

class CourierAuthData:
    #Пустой логин
    COURIER_AUTH_DATA_1 = {
        "login": "",
        "password": "1234",
        "firstName": "test_firstName"
    }
    #Пустой пароль, такого логина еще нет в системе
    COURIER_AUTH_DATA_2 = {
        "login": "test_NOT_authorized_user",
        "password": "",
        "firstName": "test_firstName"
    }

class CourierLoginData:
    #Неверный пароль, такой логин уже есть в системе
    COURIER_LOGIN_DATA_1 = {
        "login": "test_authorized_user",
        "password": "invalid_password"
    }
    #Неверный логин
    COURIER_LOGIN_DATA_2 = {
        "login": "invalid__login",
        "password": "1234"
    }
    #Пустой логин
    COURIER_LOGIN_DATA_3 = {
        "login": "",
        "password": "1234"
    }
    #Пустой пароль, такой логин уже есть в системе
    COURIER_LOGIN_DATA_4 = {
        "login": "test_authorized_user",
        "password": ""
    }
    
class OrdersParamsData:
    #Неверный id курьера
    ORDERS_PARAMS_DATA_1 = {"courierId":"00001"}
    #Сущ-ый id курьера в системе, станция метро "Бульвар Рокоссовского"(1)
    ORDERS_PARAMS_DATA_2 = {"courierId":"572854", "nearestStation":["1"]} 
    
    #limit: max=30 заказов, 'page' по умолчанию =0 
    ORDERS_LIMIT_PAGE_DATA = [
        ("min_limit_1", {"limit": "1", "page": "1"}),
        ("under_max_limit_29", {"limit": "29", "page": "5"}),
        ("exact_max_limit_30", {"limit": "30", "page": "5"}),
        ("over_max_limit_31", {"limit": "31", "page": "5"}),
        ("large_limit_50", {"limit": "50", "page": "50"}),
        ("zero_limit", {"limit": "0", "page": "0"}),
        ("none_limit", {"limit": "", "page": ""})
    ]
    ORDERS_LIMIT_STATION_DATA = [
        ("min_station_1", {"limit": "1", "nearestStation": "1"}),
        ("under_max_limit_29", {"limit": "29", "nearestStation": "110"}),
        ("exact_max_limit_30", {"limit": "30", "nearestStation": "110"}),
        ("over_max_limit_31", {"limit": "31", "nearestStation": "5"}),
        ("large_limit_50", {"limit": "50", "nearestStation": "50"}),
        ("zero_limit", {"limit": "0", "nearestStation": "0"}),
        ("none_limit", {"limit": "", "nearestStation": ""})
    ]

class RegErrors:
    MISSING_DATA = 'Недостаточно данных для создания учетной записи'
    DUPLICATE_LOGIN = 'Этот логин уже используется. Попробуйте другой.' #!!В документации указано неактуальное сообщение. Нужна корректировка документации!!

class LoginErrors:
    MISSING_AUTH_DATA = 'Недостаточно данных для входа'
    USER_NOT_FOUND = 'Учетная запись не найдена'
 