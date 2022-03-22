class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter
    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius
    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.radius * self.radius


small_circle = Circle(20)
big_circle = Circle(100)


print(small_circle.calculate_area())
print(big_circle.calculate_area())
print(f'Big Circle Circumferance: {big_circle.calculate_circumference()}')
print(f"the area of sector in big circle is: {big_circle.calculate_area_of_sector(90)}")