class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self._size = size

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Can't fit that many cookies")
        else:
            self._size = self.size + n
            return self._size

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("There's not that many cookies in the Jar")
        else:
            self._size = self.size - n
            return self._size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Jar is empty")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        size = self.deposit('') - self.withdraw('')
        if size < 0:
            raise ValueError("There are not enough cookies for you to eat")
        else:
            self._size = size
