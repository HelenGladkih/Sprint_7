import pytest
from helpers import *
from methods.courier_methods import CourierMethods

@pytest.fixture
def courier():
    payload = generate_couriers_data()
    CourierMethods.create_courier(payload)
    response = CourierMethods.courier_login(payload)
    courier_id = response[1]["id"]
    yield courier_id
    CourierMethods.delete_courier(courier_id)
