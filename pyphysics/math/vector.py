from math import sqrt, cos, sin

class Vector2:
    def __init__(self, *args: int | float | tuple[int | float, int | float])-> None:
        if len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self.x, self.y = args[0], args[1]
        elif len(args) == 1 and isinstance(args[0], tuple):
            self.x, self.y = args[0]
        else:
            self.x, self.y = 0, 0
    
    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> "Vector2":
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other: int | float) -> "Vector2":
        return self.__mul__(other)
    
    def __truediv__(self, other: int | float) -> "Vector2":
        return Vector2(self.x / other, self.y / other)
    
    def __neg__(self) -> "Vector2":
        return Vector2(-self.x, -self.y)

    def __len__(self) -> int:
        return 2

    def __getitem__(self, index: int) -> int | float:
        return (self.x, self.y)[index]
    
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    def lenght_squared(self) -> int | float:
        return self.x**2 + self.y**2

    def lenght(self) -> int | float:
        return sqrt(self.lenght_squared())

    def normalize(self) -> "Vector2":
        return self / self.lenght()
    
    def rotate(self, angle: int | float) -> "Vector2":
        return Vector2(self.x * cos(angle) - self.y * sin(angle), self.x * sin(angle) + self.y * cos(angle))

    def dot(self, other: "Vector2") -> int | float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2") -> int | float:
        return self.x * other.y - self.y * other.x