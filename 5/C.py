class BaseObject:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_coordinates(self):
        return [self._x, self._y, self._z]


class Block(BaseObject):

    def shatter(self):
        super().__init__(None, None, None)


class Entity(BaseObject):

    def move(self, x, y, z):
        super().__init__(x, y, z)


class Thing(BaseObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)


entity = Entity(1, 2, 3)
print(entity.get_coordinates())
entity.move(3, 2, 1)
print(entity.get_coordinates())
block = Block(4, 3, 2)
print(block.get_coordinates())
block.shatter()
print(block.get_coordinates())
