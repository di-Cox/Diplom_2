# Класс для хранения Url-Главной страницы и Ручек запросов Stellar Burgers

class Url:


    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'         # Главная страница Stellar Burgers

    GETTING_INGREDIENT_DATA = 'api/ingredients'            # GET-Запрос, Получение данных об ингредиентах

    CREATE_ORDER = 'api/orders'           # POST-Запрос, Создание заказа

    PASSWORD_RECOVERY_AND_RESET = '/api/password-reset'             # POST-Запрос, Восстановление и сброс пароля

    CREATE_USER = 'api/auth/register'           # POST-Запрос, Создание пользователя

    LOGIN_USER = 'api/auth/login'               # POST-Запрос, Авторизация и регистрация пользователя

    GET_USER_INFO = 'api/auth/user'             # GET-Запрос, Получение и обновление информации о пользователе

    DELETING_USER = 'api/auth/user'             # DELETE-Запрос, Удаление пользователя

    GET_ALL_ORDERS = 'api/orders/all'           # GET-Запрос, получить все заказы

    GET_USER_ORDERS = 'api/orders'              # GET-Запрос, получить заказы конкретного пользователя

    LOGOUT_USER = 'api/auth/logout'             # POST-Запрос на Выход пользователя

    REFRESH_TOKEN = 'api/auth/token'            # POST-Запрос на Обновление токена

    UPDATE_USER_INFO = 'api/auth/user'          # PATCH-Запрос на Обновление информации о пользователе







