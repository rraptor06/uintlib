class UInt16:
    def __init__(self, value=0):
        self.value = value & 0xFFFF

    def set(self, value):
        self.value = value & 0xFFFF

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"UInt16({self.value})"

    def __add__(self, other):
        if isinstance(other, UInt16):
            other = other.value
        return UInt16((self.value + other) & 0xFFFF)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, UInt16):
            other = other.value
        return UInt16((self.value - other) & 0xFFFF)

    def __eq__(self, other):
        if isinstance(other, UInt16):
            return self.value == other.value
        return self.value == other
