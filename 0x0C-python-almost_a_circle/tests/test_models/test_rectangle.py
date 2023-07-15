import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """a unittest to test the class Rectangle"""

    def test_init_with_valid_args(self):
        """test case with valid arguments """
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_init_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_init_with_negative(self):
        """test case with negative width and height"""
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_set_with_valid_value(self):
        """test case of setting width or height to an
        instance of the class
        """
        rectangle = Rectangle(5, 10)
        rectangle.width = 15
        rectangle.height = 10
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 10)

    def test_set_with_negative_value(self):
        """test case of setting an instance with negative value"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.width = -5

        with self.assertRaises(ValueError):
            rectangle.height = -10
    
    def test_set_with_noninteger(self):
        """Test case for setting with a non-int value"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rectangle.width = 5.5

        with self.assertRaises(TypeError):
            rectangle.height = 2.5

    def test_set_x_y_valid_value(self):
        """ test case for setting x or y valid arguments"""
        rectangle = Rectangle(5, 10)
        rectangle.x = 3
        rectangle.y = 10
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 10)

    def test_set_x_y_non_int_value(self):
        """test case for setting x and y to a non integer"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rectangle.x = 3.5

        with self.assertRaises(TypeError):
            rectangle.y = 2.5

    def test_set_x_y_to_negative_value(self):
        """test case for negative values"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rectangle.x = -4

        with self.assertRaises(ValueError):
            rectangle.y = -4
