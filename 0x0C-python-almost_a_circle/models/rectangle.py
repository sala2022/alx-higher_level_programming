#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.validate_value("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.validate_value("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        self.validate_value("y", value)
        self.__y = value

    def validate_value(self, attribute, value):
        """Validate attribute values."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))
        if (attribute == 'width' or attribute == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(attribute))
        if (attribute == 'x' or attribute == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters."""
        print('\n' * self.y, end="")
        pattern = [' ' * self.x + "{}".format(self.print_symbol) *
                   self.width for _ in range(self.height)]
        print('\n'.join(pattern))

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle."""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

