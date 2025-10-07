from generators import *

# Класс данных для регистрации пользователя
class DataForRegistration:


    # Конкретные валидные данные для регистрации пользователя
    data_user_valid = {
        "email": "Dmitry_Volgushev29777@yandex.ru",
        "password": "1q2w3e4r",
        "name": "DmitryVolgushev29"
    }

    # Некорректные данные
    data_user_nonexistent_credentials = {
        "email": "nonexistent@example.com",
        "password": "wrongpassword123"
    }

    # Данные с невалидным форматом email
    data_user_invalid_email_format = {
        "email": "invalid-email-format",
        "password": "1q2w3e4r"
    }

    # Данные с невалидным коротким паролем
    data_user_invalid_short_password = {
        "email": "test@example.com",
        "password": "123"
    }

    # Корректные данные для регистрации пользователя
    data_user_registration = UserGenerator.generate_data_user()


    # Некорректные данные для регистрации без поля email
    data_user_without_email = UserGenerator.generate_data_user_without_email()

    # Некорректные данные для регистрации без поля password
    data_user_without_password = UserGenerator.generate_data_user_without_password()

    # Некорректные данные для регистрации без поля name
    data_user_without_name = UserGenerator.generate_data_user_without_name()


# Класс данных для заказов
class DataForOrder:
    # Корректное тело данных для создания заказа
    order_data_with_ingredients = {
        'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']
    }

    # Тело с данными для заказа без ингредиентов
    order_data_without_ingredients = {
        'ingredients': []
    }

    # Тело с данными для заказа с некорректным хешем ингредиентов
    order_data_with_invalid_hash = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6z", "61c0c5a71d1f82001bdaaa6x"]
    }


# Класс с ошибками
class ErrorMessage:
    # Ошибки создания пользователя
    USER_ALREADY_EXISTS = "User already exists"     # Если пользователь существует, вернётся код ответа 403 Forbidden.
    REQUIRED_FIELD_MISSING = "Email, password and name are required fields"     # Если нет одного из полей, вернётся код ответа 403 Forbidden.

    # Ошибки авторизации
    INVALID_CREDENTIALS = 'email or password are incorrect'     # Если логин или пароль неверные, или нет одного из полей, вернётся код ответа 401 Unauthorized.

    # Ошибки создания заказа
    INGREDIENTS_REQUIRED = 'Ingredient ids must be provided'     # Если не передать ни один ингредиент, вернётся код ответа 400 Bad Request.

    # Выход из системы
    LOGGING_OUT = 'Successful logout'       # Тело ответа сервера при выходе из системы

    # Авторизация
    REQUEST_WITHOUT_AUTHORIZATION = 'You should be authorised'      # Если выполнить запрос без авторизации, вернётся код ответа 401 Unauthorized.
    MAIL_THAT_IS_ALREADY_IN_USE = 'User with such email already exists'     # Если передать почту, которая уже используется, вернётся код ответа 403 Forbidden.

    # Успешные сообщения
    OK_TRUE = '{"ok":true}'

