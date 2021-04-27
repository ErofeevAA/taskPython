class Balance:
    _difference = 0

    def add_left(self, weight):
        self._difference -= weight

    def add_right(self, weight):
        self._difference += weight

    def result(self):
        if self._difference < 0:
            return 'L'
        if self._difference > 0:
            return 'R'
        return '='


balance = Balance()
print(balance.result())
