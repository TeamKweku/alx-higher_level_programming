#!/usr/bin/python3
"""a module that defines a rectangle class that inherites from base class"""
from models.base import Base


class Rectangle(Base):
    """
    a class that defines a rectangle

    Attributes:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value(int): the width of the rectangle

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value(int): the height of the rectangle

        Raises:
            TypeError: if `value` is not an integer
            ValueError: is `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Returns x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets x of the rectangle instance

        Args:
            value(int): x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Returns value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of y

        Args:
            value(int): value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle

        Returns:
            int: area of the rectangle
        """

        return self.__width * self.__height

    def display(self):
        """method that prints to stdout the rectangle with the
        `#` character
        """
        print("\n" * self.__y, end="")

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """method that defines the string rep of an instance of the
        rectangle class
        """
        rectangle_str = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        rectangle_str += f" - {self.__width}/{self.__height}"
        return rectangle_str

    def update(self, *args, **kwargs):
        """a method that updates the arguments of each attribute of the class

        Args:
            args: a list of positional arguments
            kwargs: a dict of key, value pair
        """
        if args and len(args) != 0:
            attr_names = ["id", "width", "height", "x", "y"]

            for index, arg in enumerate(args):
                if index < len(attr_names):
                    setattr(self, attr_names[index], arg)
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        a method that returns the dict representation of the
        Rectangle
        """
        keys = ['id', 'width', 'height', 'x', 'y']
        values = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(keys, values))
