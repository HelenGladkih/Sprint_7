import pytest
from helpers import *
from methods.courier_methods import CourierMethods
   
@pytest.fixture
def courier():
    courier_data = generate_couriers_data()
    response = CourierMethods().create_courier(courier_data) 
    yield response, courier_data                            
    id_courier = CourierMethods().login_courier(courier_data)
    CourierMethods().delete_courier(id_courier[1]['id'])

@pytest.fixture
def authorization_courier(courier):
    response = CourierMethods().login_courier(courier[1])
    return response  
