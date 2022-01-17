from array import array



class Vector(object):

    def __init__(self, components):...

    def __add__(self, other: "Vector") -> "Vector":
        ...

    def __sub__(self, other: "Vector") -> "Vector":...

    def __mul__(self, other: "Vector") -> "Vector":...

    def __div__(self, other: "Vector"):
        raise NotImplementedError

    def __abs__(self) -> float :...

    def __str__(self) -> str:...

    def __repr__(self) -> str:...

