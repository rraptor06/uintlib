class UInt8:
    def __init__(self, value=0):
        self.value = value & 0xFF

    def set(self, value):
        self.value = value & 0xFF

    def get(self):
        return self.value

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"UInt8({self.value})"

    def __add__(self, other):
        if isinstance(other, UInt8):
            other = other.value
        return UInt8((self.value + other) & 0xFF)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, UInt8):
            other = other.value
        return UInt8((self.value - other) & 0xFF)

    def __eq__(self, other):
        if isinstance(other, UInt8):
            return self.value == other.value
        return self.value == other
