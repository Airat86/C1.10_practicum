class Any_Figure:  #класс для любой фигуры
    def __init__(self, x=0, y=0, height=0, weight=0):
        self.x = x
        self.y = y
        self.height = height
        self.weight = weight

    def __str__(self):
        return (f'Any_Figure({self.x}, {self.y}, {self.height}, {self.weight})')

r = Any_Figure(5, 10, 50, 100)
print(r)