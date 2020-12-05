# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("text_file_part3.txt", "r") as my_file:
    salary = []
    salary_min = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            salary_min.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20000 {salary_min}, средний оклад {sum(map(int, salary)) / len(salary)}')