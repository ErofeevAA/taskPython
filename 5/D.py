class Polynomial:

    def __init__(self, coefficients: list):
        self._coefficients = coefficients

    @property
    def coefficients(self):
        return self._coefficients

    def __call__(self, x):
        res = 0
        for i in range(len(self._coefficients)):
            res += (self._coefficients[i] * x ** i)
        return res

    def __add__(self, other):
        res = [x + y for x, y in zip(self._coefficients, other.coefficients)]
        l_self = len(self._coefficients)
        l_other = len(other.coefficients)
        if l_self > l_other:
            res += self._coefficients[l_other:]
        else:
            res += other.coefficients[l_self:]
        return Polynomial(res)


poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = Polynomial([10, 1])
print(poly1(2))
print(poly3(-2))
print(poly4(-2))
