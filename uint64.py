class UInt64:
    def __init__(self, value=0):
        self.value = value & 0xFFFFFFFFFFFFFFFF

    def set(self, value):
        self.value = value & 0xFFFFFFFFFFFFFFFF

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"UInt64({self.value})"

    def __add__(self, other):
        if isinstance(other, UInt64):
            other = other.value
        return UInt64((self.value + other) & 0xFFFFFFFFFFFFFFFF)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, UInt64):
            other = other.value
        return UInt64((self.value - other) & 0xFFFFFFFFFFFFFFFF)

    def __eq__(self, other):
        if isinstance(other, UInt64):
            return self.value == other.value
        return self.value == other
