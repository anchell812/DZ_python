# Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_obj = open('new_text_file.txt', 'w')

line = input('Введи данные\n')
while line:
    f_obj.writelines(line)
    line = input('Введи данные\n')
    if not line:
        break

f_obj.close()