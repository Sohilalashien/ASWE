import copy

class Shape:
    "Interface with clone method"
    def clone(self):
        # Using deepcopy to ensure a deep copy of the object
        return copy.deepcopy(self)

class Circle(Shape):
    "A Concrete Class"
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

# The Client
circle = Circle(5)
clone_circle = circle.clone()

# Comparing the original object and the cloned object
print(circle)      
print(clone_circle) 
