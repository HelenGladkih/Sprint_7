import requests
import allure
from data import *
from helpers import *


class CourierMethods:

    @allure.step('Создать курьера')
    def create_courier(self, params = None):
        if params is None:
            params = generate_couriers_data()
        response = requests.post(COURIERS_URL, data = params)
        return response.status_code, response.json()

    @allure.step('Авторизовать курьера в системе')
    def login_courier(self, params):
        response = requests.post(COURIERS_LOGIN_URL, data = params)
        return response.status_code, response.json()

    @allure.step('Удалить курьера')
    def delete_courier(self, id):
        response = requests.delete(f'{COURIERS_URL}{id}')
        return response.status_code, response.json()
         