import allure
import pytest
from helpers import *
from data import *
from methods.courier_methods import CourierMethods

class TestCourierCreate:

    @allure.title('Позитивный сценарий создания курьера: передаем все обязательные поля (логин, пароль).')
    @allure.description('ОР: Курьер успешно создан.')
    def test_create_courier_login_password_created_successfully(self):
        status_code, response_data = CourierMethods().create_courier()
        assert status_code == 201 and response_data['ok'] == True

    @allure.title('Негативный сценарий создания курьера: логин уже есть в системе.')
    @allure.description('ОР: Нельзя создать двух одинаковых курьеров, запрос возвращает ошибку.')
    @pytest.mark.parametrize('payload', [CourierAuthData.COURIER_AUTH_DATA_1])
    def test_create_courier_duplicate_login_error_409(self, payload):
        status_code, response_data = CourierMethods().create_courier(payload)
        assert status_code == 409 and response_data['message'] == RegErrors.DUPLICATE_LOGIN

    @allure.title('Негативный сценарий создания курьера: передаем пустой логин или пустой пароль.')
    @allure.description('ОР: Курьер не создан, запрос возвращает ошибку.')
    @pytest.mark.parametrize('payload', [CourierAuthData.COURIER_AUTH_DATA_2, CourierAuthData.COURIER_AUTH_DATA_3])
    def test_create_courier_missing_login_or_password_error_400(self, payload):
        status_code, response_data = CourierMethods().create_courier(payload)
        assert status_code == 400 and response_data['message'] == RegErrors.MISSING_DATA

class TestCourierLogin:

    @allure.title('Позитивный сценарий авторизации курьера: передаем все обязательные поля (логин, пароль).')
    @allure.description('ОР: Курьер успешно авторизирован в системе, запрос возвращает id курьера')
    @pytest.mark.parametrize("payload", [CourierLoginData.COURIER_LOGIN_DATA_1])
    def test_login_courier_valid_credentials_success_200(self, payload):
        status_code, response_data = CourierMethods().login_courier(payload)
        assert status_code == 200 and response_data['id'] is not None

    @allure.title('Негативный сценарий авторизации курьера: передаем несуществующий логин или неверный пароль')
    @allure.description('ОР: Курьер не авторизирован в системе, запрос возвращает ошибку.')
    @pytest.mark.parametrize("payload", [CourierLoginData.COURIER_LOGIN_DATA_2, CourierLoginData.COURIER_LOGIN_DATA_3])
    def test_login_courier_invalid_credentials_not_found_404(self, payload):
        status_code, response_data = CourierMethods().login_courier(payload)
        assert status_code == 404 and response_data["message"] == LoginErrors.USER_NOT_FOUND

    @allure.title('Негативный сценарий авторизации курьера: передаем пустой логин или пустой пароль.')
    @allure.description('ОР: Курьер не авторизирован в системе, запрос возвращает ошибку.')
    @pytest.mark.parametrize("payload", [CourierLoginData.COURIER_LOGIN_DATA_4, CourierLoginData.COURIER_LOGIN_DATA_5])
    def test_login_courier_empty_login_or_password_bad_request_400(self, payload):
        status_code, response_data = CourierMethods().login_courier(payload)
        assert status_code == 400 and response_data["message"] == LoginErrors.MISSING_AUTH_DATA
