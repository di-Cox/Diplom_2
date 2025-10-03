from faker import Faker

fake = Faker()

class UserGenerator():

    # Генерируем рандомные валидные данные для регистрации пользователя
    @staticmethod
    def generate_data_user():
        email = fake.email()
        password = fake.password()
        name = fake.first_name()

        data = {
            'email': email,
            'password': password,
            'name': name
        }

        return data

    # Генерация данных без поля email
    @staticmethod
    def generate_data_user_without_email():
        password = fake.password()
        name = fake.first_name()

        data = {
            'email': '',
            'password': password,
            'name': name

        }

        return data

    # Генерация данных без поля password
    @staticmethod
    def generate_data_user_without_password():
        email = fake.email()
        name = fake.first_name()

        data = {
            'email': email,
            'password': '',
            'name': name

        }

        return data

    # Генерация данных без поля name
    @staticmethod
    def generate_data_user_without_name():
        email = fake.email()
        password = fake.password()

        data = {
            'email': email,
            'password': password,
            'name': ''

        }

        return data


