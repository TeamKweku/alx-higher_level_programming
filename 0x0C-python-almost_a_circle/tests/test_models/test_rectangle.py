import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """a unittest to test the class Rectangle"""
    def setUp(self):
        """Initializing an instance of the Rectangle class"""
        self.rectangle = Rectangle(5, 10)

    def test_init_with_valid_args(self):
        """test case with valid arguments """
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.x, 0)
        self.assertEqual(self.rectangle.y, 0)

    def test_init_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_init_with_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

        with self.assertRaises(ValueError):
            Rectangle(5, 0)

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
        self.rectangle.width = 15
        self.rectangle.height = 10
        self.assertEqual(self.rectangle.width, 15)
        self.assertEqual(self.rectangle.height, 10)

    def test_set_with_negative_value(self):
        """test case of setting an instance with negative value"""
        with self.assertRaises(ValueError):
            self.rectangle.width = -5

        with self.assertRaises(ValueError):
            self.rectangle.height = -10

    def test_set_with_noninteger(self):
        """Test case for setting with a non-int value"""
        with self.assertRaises(TypeError):
            self.rectangle.width = 5.5

        with self.assertRaises(TypeError):
            self.rectangle.height = 2.5

    def test_set_x_y_valid_value(self):
        """ test case for setting x or y valid arguments"""
        self.rectangle.x = 3
        self.rectangle.y = 10
        self.assertEqual(self.rectangle.x, 3)
        self.assertEqual(self.rectangle.y, 10)

    def test_set_x_y_non_int_value(self):
        """test case for setting x and y to a non integer"""
        with self.assertRaises(TypeError):
            self.rectangle.x = 3.5

        with self.assertRaises(TypeError):
            self.rectangle.y = 2.5

    def test_set_x_y_to_negative_value(self):
        """test case for negative values"""
        with self.assertRaises(ValueError):
            self.rectangle.x = -4

        with self.assertRaises(ValueError):
            self.rectangle.y = -4
