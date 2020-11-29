# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_data(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])
print(my_data(name ='Ivan', surname ='Ivanov', year = '1986', city = 'SPb', email = '1@1.ru', phone = '123456'))
