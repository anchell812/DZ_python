# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.



with open("new_file_2.txt") as my_f:
    print(my_f.read())

def my_f():
    file = open("new_file_2.txt")
    count = 0
    for line in file:
            count+=1

    print(count)
my_f()


