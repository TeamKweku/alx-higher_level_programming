#!/usr/bin/python3
"""a module that defines a Square class which inherits from Rectancle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from the Rectangle class

    Attributes:
        size(int): size of the square
        x(int): x value
        y(int): y value
        id(int): id of an instance of the class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get width/ height of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set width/height of an instance"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the Square instance"""
        square_str = f"[Square] ({self.id}) {self.x}/{self.y} "
        square_str += f"- {self.width}"
        return square_str

    def update(self, *args, **kwargs):
        """method that assign attributes to an instance of the class
            
            Args:
                args: list of positional arguments
                kwargs: dict of key, value pair of arguments
        """
        if args and len(args) != 0:
            attr_names = ["id", "size", "x", "y"]

            for num, value in enumerate(args):
                setattr(self, attr_names[num], value)
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        method that returns the dictionary representation of Square
        """
        keys = ['id', 'size', 'x', 'y']
        values = [self.id, self.width, self.x, self.y]
        return dict(zip(keys, values))
