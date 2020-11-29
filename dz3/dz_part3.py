# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg1>=arg2 and arg2>=arg3:
        return arg1+arg2
    elif arg1<=arg2 and arg1<=arg3:
        return arg2+arg3
    else:
        return arg1+arg3
print(my_func(int(input('введи первое число')), int(input('введи второе число')), int(input('введи третье число'))))