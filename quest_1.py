# #План проекта по Работе с пользователями и их профилями
# Создание класса User
#
# Атрибуты: имя, фамилия, email, пароль, дата регистрации.
# Методы: конструктор, строковое представление, метод для изменения пароля.
# Создание класса Profile
#
# Атрибуты: пользователь, возраст, пол, адрес, телефон.
# Методы: конструктор, строковое представление, метод для обновления информации профиля.
# Создание класса UserManager
#
# Атрибуты: список пользователей.
# Методы: добавление пользователя, удаление пользователя, поиск пользователя по email, вывод списка всех пользователей, обновление профиля пользователя.
# Создание основного скрипта
#
# Создание экземпляров классов.
# Демонстрация работы системы управления пользователями (добавление пользователей, обновление профилей, поиск пользователей, удаление пользователей).

import time
import os

reg_date = time.ctime()


class User:
    """
    Данный класс содержит имя, фамилию, емаил и пароль.

    методы: строковое представление и метод для изменения пароля.
    """

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        if '@' not in email or not email.endswith(('.com', '.ru', '.net')):
            raise ValueError('Вы ввели не коректную электронную почту')
        else:
            self.email = email
        self.password = str(password)
        self.data_reg = reg_date

    def __str__(self):
        return (f'Имя пользователя: {self.name}, фамилия: {self.surname},\n '
                f'email: {self.email}, ваш пороль: {self.password}\n'
                f'ваша дата регистрации: {self.data_reg}')

    def new_password(self, password, new_password, conf_new_password):
        if str(password) == self.password:
            if str(new_password) == str(conf_new_password):
                self.password = str(new_password)


class Profile:

    def __init__(self, login, age, gender, home, phone):
        self.login = login
        self.age = age
        self.gender = gender
        self.home = home
        self.phone = phone

    def redact_profile(self, age, gender, home, phone):
        self.age = age
        self.gender = gender
        self.home = home
        self.phone = phone

    def __str__(self):
        return (f'Ваш логин: {self.login}, возраст: {self.age}, пол:{self.gender}, \n'
                f'ваш адрес: {self.home}, ваш телефон: {self.phone}')


class UserManager(User, Profile):
    data = 'data.txt'

    def __init__(self, name, surname, email, password, login, age, gender, home, phone):
        super().__init__(name, surname, email, password)
        super(User, self).__init__(login, age, gender, home, phone)

    def __check_user(self, line):
        count = 0
        name, surname, email, password, login, age, gender, home, phone = line.split(' ')
        if self.email == email:
            count += 1
            print(f'Пользователь: {self.email} уже зарегестрирован')
            return count

    def add_user(self):
        with open(self.data, 'r+', encoding='utf-8') as file:
            if os.stat("data.txt").st_size == 0:
                file.write(f'{self.name} {self.surname} {self.email} {self.password} {self.login} {self.age} '
                           f'{self.gender} {self.home} {self.phone}\n')
            count = 0
            for line in file:
                if self.__check_user(line) == 1:
                    count += 1
            if count == 0:
                file.write(f'{self.name} {self.surname} {self.email} {self.password} {self.login} {self.age} '
                           f'{self.gender} {self.home} {self.phone}\n')

    def del_user(self):


den = UserManager('1234', '12342', 'qwe3@mail.ru', 123, 1113, 13,
                  3, 1113, 123123)
den.add_user()
