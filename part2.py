
mas = []
while True:
    a = input('введите данные\n')
    if a == 'stop':
        break
    else:
        mas.append(a)
print(mas)
for i in range(0, len(mas)):
    if i % 2 == 1:
        memory = mas[i]
        mas[i] = mas[i-1]
        mas[i-1] = memory
        print(mas)
