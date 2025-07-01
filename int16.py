class Int16:
    def __init__(self, value=0):
        self.value = self.to_int16(value)

    def to_int16(self, value):
        value &= 0xFFFF
        if value & 0x8000:
            value -= 0x10000
        return value

    def set(self, value):
        self.value = self.to_int16(value)

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"Int16({self.value})"

    def __add__(self, other):
        if isinstance(other, Int16):
            other = other.value
        return Int16(self.value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Int16):
            other = other.value
        return Int16(self.value - other)

    def __eq__(self, other):
        if isinstance(other, Int16):
            return self.value == other.value
        return self.value == other
