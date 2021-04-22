class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def get_perimeter(self):
        return ((self.x + self.y) * 2)


data = Rectangle(int(input("Введите длинну: ")), int(input("Введите ширину: ")))
print("Площадь:",data.get_area(), "  Периметр:",data.get_perimeter())