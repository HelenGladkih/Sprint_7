import allure
import pytest
from methods.order_methods import OrderMethods
from data import *

class TestCreateOrder:

    @allure.title('Позитивный сценарий создания заказа: передаем все обязательные поля, цвет или один, или оба, или без цвета.')
    @allure.description('ОР: Заказ успешно создан, тело ответа содержит track.')
    @pytest.mark.parametrize("payload", [OrderData.ORDER_DATA_1, OrderData.ORDER_DATA_2, OrderData.ORDER_DATA_3])
    def test_create_order_with_various_colors_success_201(self, payload):
        status_code, response_data = OrderMethods.create_order(payload)
        assert status_code == 201 and response_data['track'] is not None

class TestGetListOrders:

    @allure.title('Позитивный сценарий получения списка заказов.')
    @allure.description('ОР: Тело ответа вернуло список заказов.')
    def test_get_list_orders_default_params_success_200(self):
        status_code, list_orders = OrderMethods.get_list_orders()
        assert status_code == 200 and list_orders != []

    @allure.title('Позитивный сценарий получения списка заказов: запрос c существующим id курьера в системе.')
    @allure.description('ОР: Тело ответа вернуло список всех активных/завершенных заказов курьера.')
    def test_get_list_orders_id_200(self):
        payload = OrdersParamsData.ORDERS_PARAMS_DATA_1
        status_code, list_orders = OrderMethods.get_list_orders_sort(payload)
        assert status_code == 200 and list_orders != []

    @allure.title('Позитивный сценарий получения списка заказов: все активные/завершенные заказы курьера на указаной станции.')
    @allure.description('ОР: Тело ответа вернуло список всех активных/завершенных заказов курьера.')
    def test_get_list_orders_id_station_200(self):
        payload = OrdersParamsData.ORDERS_PARAMS_DATA_3
        status_code, list_orders = OrderMethods.get_list_orders_sort(payload)
        assert status_code == 200 and list_orders != []      

    @allure.title('Позитивный параметризированный сценарий получения списка заказов: передаем количество заказов и № текущей страницы') 
    @allure.description('ОР: Тело ответа вернуло список заказов курьера в кол-ве не более 30 шт.')                
    @pytest.mark.parametrize("payload", [data[1] for data in OrdersParamsData.ORDERS_LIMIT_PAGE_DATA], ids=[data[0] for data in OrdersParamsData.ORDERS_LIMIT_PAGE_DATA])
    def test_get_list_orders_limit_page_200(self, payload):
        status_code, list_orders = OrderMethods.get_list_orders_sort(payload)
        assert status_code == 200 and len(list_orders["orders"]) <= 30 

    @allure.title('Позитивный параметризированный сценарий получения списка заказов: передаем количество заказов и станцию метро')
    @allure.description('ОР: Тело ответа вернуло список заказов курьера в кол-ве не более 30 шт.')                
    @pytest.mark.parametrize("payload", [data[1] for data in OrdersParamsData.ORDERS_LIMIT_STATION_DATA], ids=[data[0] for data in OrdersParamsData.ORDERS_LIMIT_STATION_DATA])
    def test_get_list_orders_limit_station_200(self, payload):
        status_code, list_orders = OrderMethods.get_list_orders_sort(payload)
        assert status_code == 200 and len(list_orders["orders"]) <= 30 

    @allure.title('Негативный сценарий получения списка заказов: запрос c несуществующим id курьера в системе.')
    @allure.description('ОР: Тело ответа содержит сообщение об ошибке с указанием несуществующего id курьера')
    def test_get_list_orders_id_invalid_404(self):
        payload = OrdersParamsData.ORDERS_PARAMS_DATA_2
        status_code, response_data = OrderMethods.get_list_orders_sort(payload)
        id = OrdersParamsData.ORDERS_PARAMS_DATA_2.get('courierId')
        assert status_code == 404 and response_data['message'] == f'Курьер с идентификатором {id} не найден'
 