# pyright: reportShadowedImports=false
from math import sqrt, cos, sin

class Vector2:
    def __init__(self, *args: int | float | tuple[int | float, int | float]):
        if len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self.x, self.y = args[0], args[1]
        elif len(args) == 1 and isinstance(args[0], tuple):
            self.x, self.y = args[0]
        else:
            self.x, self.y = 0, 0
    
    def __add__(self, other: "Vector2"):
        return Vector2(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other: "Vector2"):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float):
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other: int | float):
        return self.__mul__(other)
    
    def __truediv__(self, other: int | float):
        return Vector2(self.x / other, self.y / other)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __len__(self):
        return 2

    def __getitem__(self, index: int):
        return (self.x, self.y)[index]
    
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def lenght_squared(self):
        return self.x**2 + self.y**2

    def lenght(self):
        return sqrt(self.lenght_squared())

    def normalize(self):
        return self / self.lenght()
    
    def rotate(self, angle: int | float):
        return Vector2(self.x * cos(angle) - self.y * sin(angle), self.x * sin(angle) + self.y * cos(angle))

    def dot(self, other: "Vector2"):
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2"):
        return self.x * other.y - self.y * other.x


class Vector3:
    def __init__(self, *args: int | float | tuple[int | float, int | float, int | float]):
        if len(args) == 3 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
            self.x, self.y, self.z = args[0], args[1], args[2]
        elif len(args) == 1 and isinstance(args[0], tuple):
            self.x, self.y, self.z = args[0]
        else:
            self.x, self.y, self.z = 0, 0, 0

    def __add__(self, other: "Vector3"):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: "Vector3"):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: int | float):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: int | float):
        return self.__mul__(other)
    
    def __truediv__(self, other: int | float):
        return Vector3(self.x / other, self.y / other, self.z / other)
    
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __len__(self):
        return 3
    
    def __getitem__(self, index: int):
        return (self.x, self.y, self.z)[index]

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
    
    def lenght_squared(self):
        return self.x**2 + self.y**2 + self.z**2
    
    def lenght(self):
        return sqrt(self.lenght_squared())
    
    def normalize(self):
        return self / self.lenght()

    def dot(self, other: "Vector3"):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: "Vector3"):
        return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)