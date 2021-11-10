class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.list_of_lists])

    def __add__(self, other):
        return Matrix(list(map(
            lambda x, y: list(map(lambda z, w: z + w, x, y)),
            self.list_of_lists, other.list_of_lists)))

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
b = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
m1 = Matrix(a)
m2 = Matrix(b)
print(m1.__str__())
print()
print(m2.__str__())
print()
print(m1.__add__(m2))