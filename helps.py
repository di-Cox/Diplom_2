import requests
from data import *
from curl import *
from generators import *
import json

# Класс для пользователя (Создаём, логинемся, удаляем)
class UserRegistration:
    # Регистрация пользователя
    @staticmethod
    def register_user(data):
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(data)
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', headers=headers, data=data_json)

        # Безопасное получение JSON (если ответ в JSON формате)
        try:
            response_json = response.json() if response.text else {}
        except:
            response_json = {}

        return {
            'response_text': response.text,
            'response_status_code': response.status_code,
            'response_json': response_json
        }

    # Логин пользователя
    @staticmethod
    def login_user(data):
        headers = {'Content-Type': 'application/json'}
        data_json = json.dumps(data)
        response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', headers=headers, data=data_json)

        # Безопасное получение JSON
        try:
            response_json = response.json() if response.text else {}
        except:
            response_json = {}

        return {
            'id': str(response_json.get('id', '')) if response_json else '',
            'response_text': response.text,
            'response_status_code': response.status_code,
            'response_json': response_json,
            'access_token': response_json.get('accessToken') if response_json else None
        }

    # Удаление пользователя
    @staticmethod
    def delete_user(access_token):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': access_token
        }
        response = requests.delete(f'{Url.MAIN_URL}{Url.GET_USER_INFO}', headers=headers)
        return {
            'response_text': response.text,
            'response_status_code': response.status_code
        }


class OrderCreation:
    # Создание заказа
    @staticmethod
    def create_order(data, access_token=None):
        headers = {'Content-Type': 'application/json'}
        if access_token:
            headers['Authorization'] = access_token

        data_json = json.dumps(data)
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', headers=headers, data=data_json)

        # Безопасное получение JSON (обрабатываем случаи когда API возвращает HTML вместо JSON)
        response_json = {}
        if response.text:
            try:
                response_json = response.json()
            except:
                # Если не JSON (например HTML), оставляем пустой словарь
                response_json = {}

        return {
            'response_text': response.text,
            'response_status_code': response.status_code,
            'response_json': response_json
        }

