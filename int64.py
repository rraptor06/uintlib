class Int64:
    def __init__(self, value=0):
        self.value = self.to_int64(value)

    def to_int64(self, value):
        value &= 0xFFFFFFFFFFFFFFFF
        if value & 0x8000000000000000:
            value -= 0x10000000000000000
        return value

    def set(self, value):
        self.value = self.to_int64(value)

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"Int64({self.value})"

    def __add__(self, other):
        if isinstance(other, Int64):
            other = other.value
        return Int64(self.value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Int64):
            other = other.value
        return Int64(self.value - other)

    def __eq__(self, other):
        if isinstance(other, Int64):
            return self.value == other.value
        return self.value == other
