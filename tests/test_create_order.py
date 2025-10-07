import pytest
import requests
import allure
import json
from data import *
from helps import *
from generators import *
from curl import *

class TestCreateOrder:
    @allure.title('Тест на создание заказа с авторизацией и выбором ингредиентов')
    @allure.description('Отправить POST-Запрос на создание заказа с авторизацией и корректными ингредиентами')
    def test_create_order_with_auth_and_ingredients_success(self, get_access_token):
        with allure.step('Получить access token из фикстуры'):
            access_token = get_access_token

        with allure.step('Подготовить данные заказа с ингредиентами'):
            order_data = DataForOrder.order_data_with_ingredients

        with allure.step('Отправить POST-Запрос на создание заказа с авторизацией'):
            response = OrderCreation.create_order(order_data, access_token)

        with allure.step('Проверяем статус код 200 успешного создания заказа'):
            assert response['response_status_code'] == 200

        with allure.step('Проверяем флаг success в ответе'):
            assert response['response_json'].get('success') == True

        with allure.step('Проверяем наличие номера заказа в ответе'):
            order_number = response['response_json'].get('order', {}).get('number')
            assert order_number is not None

        with allure.step('Проверяем наличие имени заказа в ответе'):
            order_name = response['response_json'].get('name')
            assert order_name is not None

    @allure.title('Тест на создание заказа без авторизации - Баг: API возвращает код статуса 200 вместо 401')
    @allure.description(
        'Отправляем POST-Запрос на создание заказа без токена авторизации. По документации API код должен приходить 401, а API возвращает код 200')
    def test_create_order_without_auth_fails(self):
        with allure.step('Подготавливаем данные заказа с ингредиентами'):
            order_data = DataForOrder.order_data_with_ingredients

        with allure.step('Отправляем POST-Запрос на создание заказа без авторизации'):
            response = OrderCreation.create_order(order_data)

        with allure.step('Найден Баг: API возвращает код 200, ожидается код 401 по документации'):
            allure.attach(
                'Баг: При создании заказа без авторизации API возвращает код 200 вместо 401\n'
                'Ожидаемый результат: по документации API код возвращается 401 Unauthorized\n'
                'Фактический результат: возвращается код 200 OK\n'
                'Выходит, что пользователи могут создавать свои заказы без авторизации\n'
                'Приоритет ошибки: Критическая',
                name='Bug Report - Authorization',
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step('Проверяем по документации: должен быть код 401'):
            assert response['response_status_code'] == 401

        with allure.step('Проверяем что заказ НЕ создается без авторизации'):
            assert response['response_json'].get('success') == False


    @allure.title('Тест на создание заказа без ингредиентов')
    @allure.description('Отправляем POST-Запрос на создание заказа с пустым списком ингредиентов')
    def test_create_order_without_ingredients_fails(self, get_access_token):
        with allure.step('Получаем access token из фикстуры'):
            access_token = get_access_token

        with allure.step('Подготавливаем данные для заказа без ингредиентов'):
            order_data = DataForOrder.order_data_without_ingredients

        with allure.step('Отправить POST-Запрос на создание заказа без ингредиентов'):
            response = OrderCreation.create_order(order_data, access_token)

        with allure.step('Проверить статус код ошибки 400'):
            assert response['response_status_code'] == 400

        with allure.step('Проверяем флаг success в ответе'):
            assert response['response_json'].get('success') == False

        with allure.step('Проверить сообщение об ошибке'):
            error_message = response['response_json'].get('message')
            assert error_message == ErrorMessage.INGREDIENTS_REQUIRED

    @allure.title('Тест на создание заказа с неверным хешем ингредиентов')
    @allure.description('Отправляем POST-Запрос на создание заказа с некорректными хешами ингредиентов')
    def test_create_order_with_invalid_ingredient_hash_fails(self, get_access_token):
        with allure.step('Получить access token из фикстуры'):
            access_token = get_access_token

        with allure.step('Подготовить данные заказа с неверными хешами ингредиентов'):
            order_data = DataForOrder.order_data_with_invalid_hash

        with allure.step('Отправить POST-запрос на создание заказа с неверными ингредиентами'):
            response = OrderCreation.create_order(order_data, access_token)

        with allure.step('Проверить статус код ответа 500'):
            assert response['response_status_code'] == 500

        with allure.step('Зафиксировать что API возвращает HTML вместо JSON при ошибке 500'):
            # API возвращает HTML страницу с ошибкой вместо JSON
            allure.attach(
                "При ошибке 500 API возвращает HTML вместо JSON:\n" + response['response_text'],
                name="500 Error Response",
                attachment_type=allure.attachment_type.TEXT
            )