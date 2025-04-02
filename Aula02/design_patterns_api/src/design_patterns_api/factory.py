from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass


class Circle(Shape):
    def draw(self) -> str:
        return "Circle area:"
    
    
class Rectangle(Shape):
    def draw(self) -> str:
        return "Rectangle area:"


def shape_factory(shape_type: str) -> Shape:
    shapes = {
        "circle": Circle,
        "rectangle": Rectangle,
    }
    shape_class = shapes.get(shape_type.lower())
    if not shape_class:
        raise ValueError(f"Invalid shape type: {shape_type}")
    
    return shape_class()


if __name__ == "__main__": 
    shape1 = shape_factory("circle")
    print(shape1.draw())

    shape2 = shape_factory("rectangle")
    print(shape2.draw())