import random
import string

def generate_couriers_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    login = generate_random_string(10)
    password = generate_random_string(10)
       #ПО ФАКТУ 'firstName' НЕобязательное поле. В документации обязательное. Нужна корректировка документации!!
    
    payload = {
            'login': login,
            'password': password
        }
    
    return payload
