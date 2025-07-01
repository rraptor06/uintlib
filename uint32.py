class UInt32:
    def __init__(self, value=0):
        self.value = value & 0xFFFFFFFF

    def set(self, value):
        self.value = value & 0xFFFFFFFF

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"UInt32({self.value})"

    def __add__(self, other):
        if isinstance(other, UInt32):
            other = other.value
        return UInt32((self.value + other) & 0xFFFFFFFF)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, UInt32):
            other = other.value
        return UInt32((self.value - other) & 0xFFFFFFFF)

    def __eq__(self, other):
        if isinstance(other, UInt32):
            return self.value == other.value
        return self.value == other
