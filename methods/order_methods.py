import requests
import allure
from data import *
from helpers import *

class OrderMethods:

    @allure.step('Создать заказ')
    def create_order(payload):
        response = requests.post(ORDERS_URL, json = payload)
        return response.status_code, response.json()
        
    @allure.step('Получить список заказов')
    def get_list_orders():
        response = requests.get(ORDERS_URL)
        return response.status_code, response.text

    @allure.step('Получить отсортированный список заказов')
    def get_list_orders_sort(payload):
        response = requests.get(ORDERS_URL, params = payload)
        return response.status_code, response.json()
    