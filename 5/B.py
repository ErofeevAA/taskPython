class MyVector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return MyVector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return MyVector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self._x = self._x * other
        self._y = self._y * other
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'MyVector({self.x}, {self.y})'


test = MyVector(4, 4)
test *= 2
print(test)
print(test + test)
print(test - test)
print(test == test)
print(test != test)
print(test * 2)
print(2 * test)
print(abs(test))
