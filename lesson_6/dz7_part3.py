# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' *(self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'sum of cell is ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'вычитание невозможно'

    def __mul__(self, other):
        return 'multiply of cell is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'truediv of cells is ' + str(self.nums / other.nums)

cell_1 = Cell(10)
cell_2 = Cell(36)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))

