class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return str(f'Количество ячеек: {self.number}')

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if (self.number - other.number) > 0:
            return self.number - other.number
        else:
            return 'Разность меньше нуля'

    def __mul__(self, other):
        return Cell(self.number * other.number)

#В разных частях задания разные указания относительно деления.
#Вначале: обычное (не целочисленное) деление клеток
#Далее при описании метода truediv: целочисленное деление количества ячеек
#Здесь реализовано целочисленное деление
    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, number_in_row):
        x = 1
        row = ''
        while x < self.number:
            for i in range(1, int(number_in_row)):
                row += '*'
                if x % number_in_row == 0:
                    row += "\n"
                x += 1
        return row

a = Cell(8)
b = Cell(18)
c = Cell(9)
d = Cell(3)

print(a + b)
print(a - b)
print(c - d)
print(a * b)
print(c / d)
print()
print(a.make_order(5))
print()
print(b.make_order(4))