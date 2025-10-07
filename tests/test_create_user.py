import pytest
import requests
import allure
import json
from data import *
from helps import *
from generators import *
from curl import *

class TestCreateUser:
    @allure.title('Тест на создание уникального пользователя')
    @allure.description('Отправляем POST-Запрос на создание нового пользователя, проверяем успешную регистрацию')
    def test_create_unique_user_success(self):
        with allure.step('Генерируем данные для нового пользователя'):
            user_data = UserGenerator.generate_data_user()

        with allure.step('Отправляем POST-запрос на создание пользователя'):
            create_response = UserRegistration.register_user(user_data)

        with allure.step('Проверить статус код ответа при создании пользователя'):
            assert create_response['response_status_code'] == 200

        with allure.step('Проверить успешное создания пользователя в ответе'):
            assert create_response['response_json'].get('success') == True

        with allure.step('Проверить, что пользователь может авторизоваться'):
            login_response = UserRegistration.login_user(user_data)
            assert login_response['response_status_code'] == 200
            assert login_response.get('access_token') is not None

        with allure.step('Удаляем созданного пользователя'):
            if login_response.get('access_token'):
                UserRegistration.delete_user(login_response['access_token'])

    @allure.title('Тест на создание пользователя который уже зарегистрирован')
    @allure.description('Отправляем два POST-Запроса на регистрацию с одинаковыми данными')
    def test_create_duplicate_user_fails(self):
        with allure.step('Создаем первого пользователя'):
            first_user_data = UserGenerator.generate_data_user()
            first_response = UserRegistration.register_user(first_user_data)
            assert first_response['response_status_code'] == 200

        with allure.step('Отправляем повторный запрос на создание пользователя с теми же данными'):
            duplicate_response = UserRegistration.register_user(first_user_data)

        with allure.step('Проверяем статус код ошибки 403'):
            assert duplicate_response['response_status_code'] == 403

        with allure.step('Проверить сообщение об ошибке существующего пользователя'):
            assert ErrorMessage.USER_ALREADY_EXISTS in duplicate_response['response_text']

        with allure.step('Удаляем созданного пользователя'):
            login_response = UserRegistration.login_user(first_user_data)
            if login_response.get('access_token'):
                UserRegistration.delete_user(login_response['access_token'])


    @allure.title('Тест на создание пользователя без заполнения обязательных полей')
    @allure.description('Отправляем POST-Запрос на регистрацию без заполнения обязательных полей')
    @pytest.mark.parametrize('user_data, missing_field', [
        (DataForRegistration.data_user_without_email, 'email'),
        (DataForRegistration.data_user_without_password, 'password'),
        (DataForRegistration.data_user_without_name, 'name'),
    ])
    def test_create_user_missing_required_field(self, user_data, missing_field):
        with allure.step('Отправляем запрос на создание пользователя без поля {missing_field}'):
            response = UserRegistration.register_user(user_data)

        with allure.step('Проверить статус код ошибки 403'):
            assert response['response_status_code'] == 403

        with allure.step('Проверить сообщение об ошибки обязательных полей'):
            assert ErrorMessage.REQUIRED_FIELD_MISSING in response['response_text']