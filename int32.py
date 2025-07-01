class Int32:
    def __init__(self, value=0):
        self.value = self.to_int32(value)

    def to_int32(self, value):
        value &= 0xFFFFFFFF
        if value & 0x80000000:
            value -= 0x100000000
        return value

    def set(self, value):
        self.value = self.to_int32(value)

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"Int32({self.value})"

    def __add__(self, other):
        if isinstance(other, Int32):
            other = other.value
        return Int32(self.value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Int32):
            other = other.value
        return Int32(self.value - other)

    def __eq__(self, other):
        if isinstance(other, Int32):
            return self.value == other.value
        return self.value == other
