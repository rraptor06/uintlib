class Int8:
    def __init__(self, value=0):
        self.value = self.to_int8(value)

    def to_int8(self, value):
        value &= 0xFF
        if value & 0x80:
            value -= 0x100
        return value

    def set(self, value):
        self.value = self.to_int8(value)

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"Int8({self.value})"

    def __add__(self, other):
        if isinstance(other, Int8):
            other = other.value
        return Int8(self.value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Int8):
            other = other.value
        return Int8(self.value - other)

    def __eq__(self, other):
        if isinstance(other, Int8):
            return self.value == other.value
        return self.value == other
