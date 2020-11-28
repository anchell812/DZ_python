d = {'первый элемент':'зима',
     2:'весна',
     3:'лето',
     4:'осень'}
a = int(input('введите месяц\n'))
if a == 1 or a == 2 or a == 12:
    print(d['первый элемент'])
elif a == 3 or a == 4 or a == 5:
    print(d[2])
elif a == 6 or a == 7 or a == 8:
    print(d[3])
elif a == 9 or a == 10 or a == 11:
    print(d[4])