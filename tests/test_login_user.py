import pytest
import requests
import allure
import json
from data import *
from helps import UserRegistration
from generators import *
from curl import *


class TestLoginUser:
    @allure.title('Тест на вход с существующими валидными данными')
    @allure.description('Отправляем POST-Запрос на авторизацию с конкретными валидными данными')
    def test_login_existing_user_with_valid_data_success(self):
        with allure.step('Использовать конкретные валидные данные из data.py'):
            valid_data = DataForRegistration.data_user_valid

        with allure.step('Отправить запрос на авторизацию с валидными данными'):
            login_response = UserRegistration.login_user(valid_data)

        with allure.step('Проверить статус код успешной авторизации'):
            assert login_response['response_status_code'] == 200

        with allure.step('Проверить наличие accessToken в ответе'):
            assert login_response.get('access_token') is not None

        with allure.step('Проверить флаг success в ответе'):
            assert login_response['response_json'].get('success') == True

    @allure.title('Тест на вход с некорректными данными')
    @allure.description('Отправляем POST-Запрос на авторизацию с корректными но несуществующими данными')
    def test_login_with_nonexistent_credentials_fails(self):
        with allure.step('Использовать данные несуществующего пользователя из data.py'):
            nonexistent_data = DataForRegistration.data_user_nonexistent_credentials

        with allure.step('Отправить запрос на авторизацию с несуществующими данными'):
            response = UserRegistration.login_user(nonexistent_data)

        with allure.step('Проверить статус код ошибки 401'):
            assert response['response_status_code'] == 401

        with allure.step('Проверить сообщение об ошибке неверных учетных данных'):
            assert ErrorMessage.INVALID_CREDENTIALS in response['response_text']

        with allure.step('Проверить флаг success в ответе'):
            assert response['response_json'].get('success') == False

    @allure.title('Тест на вход с невалидным форматом email')
    @allure.description('Отправляем POST-Запрос на авторизацию с некорректным форматом email')
    def test_login_with_invalid_email_format_fails(self):
        with allure.step('Использовать данные с невалидным форматом email из data.py'):
            invalid_data = DataForRegistration.data_user_invalid_email_format

        with allure.step('Отправить запрос на авторизацию с невалидным email'):
            response = UserRegistration.login_user(invalid_data)

        with allure.step('Проверить статус код ошибки 401'):
            assert response['response_status_code'] == 401

        with allure.step('Проверить сообщение об ошибке неверных учетных данных'):
            assert ErrorMessage.INVALID_CREDENTIALS in response['response_text']

        with allure.step('Проверить флаг success в ответе'):
            assert response['response_json'].get('success') == False

    @allure.title('Тест на вход с невалидным коротким паролем')
    @allure.description('Отправляем POST-Запрос на авторизацию с слишком коротким паролем')
    def test_login_with_invalid_short_password_fails(self):
        with allure.step('Использовать данные с невалидным коротким паролем из data.py'):
            invalid_data = DataForRegistration.data_user_invalid_short_password

        with allure.step('Отправить запрос на авторизацию с невалидным паролем'):
            response = UserRegistration.login_user(invalid_data)

        with allure.step('Проверить статус код ошибки 401'):
            assert response['response_status_code'] == 401

        with allure.step('Проверить сообщение об ошибке неверных учетных данных'):
            assert ErrorMessage.INVALID_CREDENTIALS in response['response_text']

        with allure.step('Проверить флаг success в ответе'):
            assert response['response_json'].get('success') == False