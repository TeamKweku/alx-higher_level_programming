import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """a unittest to test the class Rectangle"""

    def test_init_with_valid_args(self):
        """test case with valid arguments"""
        rectangle = Rectangle(5, 10, 4, 3, 12)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 12)

    def test_init_with_no_args(self):
        """Test without arguments"""
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

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_with_string_to_one_arg(self):
        """Test case of passing a string as one arg"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_set_with_noninteger(self):
        """Test case for setting with a non-int value"""
        rectangle = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rectangle.width = 5.5

        with self.assertRaises(TypeError):
            rectangle.height = 2.5

    def test_set_x_y_valid_value(self):
        """test case for setting x or y valid arguments"""
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

    def test_area(self):
        """test the area of the the rectangle instance"""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_str(self):
        """Test case of __str__ method call"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_output)

    def test_update_valid_args(self):
        """Test case for update method with valid arguments"""
        rectangle = Rectangle(5, 10)

        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_update_with_partial_args(self):
        """Test case for update method with partial arguments"""
        rectangle = Rectangle(5, 10)
        rectangle.update(10, 15)

        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_update_with_no_args(self):
        """Test for an empty value call to update method"""
        rectangle = Rectangle(5, 10, 0, 0, 13)

        rectangle.update()

        self.assertEqual(rectangle.id, 13)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_update_with_kwargs(self):
        """Test for instance of kwargs passed to update method"""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(y=1, width=2, x=3, id=89)

        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 1)

    def test_to_dictionary(self):
        """ Test to dictionary function """
        rectangle = Rectangle(3, 2, 3, 2, 7)
        exp = {'id': 7, 'width': 3, 'height': 2, 'x': 3, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), exp)

class TestRectangleCreate(unittest.TestCase):
    """Testing the create method """
    def test_create_with_id(self):
        """ test create with id """
        rectangle = Rectangle.create(**{'id': 89})
        self.assertEqual(rectangle.id, 89)

    def test_create_with_width(self):
        """Test with width """
        rec = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.id, 89)

    def test_create_with_height(self):
        """test with height """
        r = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_create_with_x(self):
        """test with x value """
        r = Rectangle.create(**{
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3
        })
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_create_with_x(self):
        """test with y value """
        r = Rectangle.create(**{
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4,
        })
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
