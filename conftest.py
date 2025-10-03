import pytest
import logging
import requests
import allure
from helps import *
from data import *
from generators import *


logger = logging.getLogger(__name__)

# Фикстура для регистрации, логина и удаления пользователя
@pytest.fixture()
def user_reg_log_del():
    with allure.step('Создаём нового пользователя'):
        user_create = UserRegistration.register_user(DataForRegistration.data_user_registration)

    with allure.step('Логинемся созданным пользователем'):
        user_login = UserRegistration.login_user(DataForRegistration.data_user_registration)

    yield {
        'user_data': DataForRegistration.data_user_registration,
        'user_create_response': user_create,
        'user_login_response': user_login,
        'access_token': user_login.get('access_token')
    }

    with allure.step('Удаляем тестового пользователя '):
        if user_login.get('access_token'):
            UserRegistration.delete_user(user_login['access_token'])


# Фикстура для получения токена ('access_token')
@pytest.fixture()
def get_access_token():
    with allure.step('Создать и залогиниться пользователем для получения токена'):
        user_create = UserRegistration.register_user(DataForRegistration.data_user_registration)
        user_login = UserRegistration.login_user(DataForRegistration.data_user_registration)

    yield user_login.get('access_token')

    with allure.step('Удалить тестового пользователя'):
        if user_login.get('access_token'):
            UserRegistration.delete_user(user_login['access_token'])

