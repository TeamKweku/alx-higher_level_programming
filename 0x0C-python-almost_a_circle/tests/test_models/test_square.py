import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """a unittest to test the Square class """

    def test_init_with_valid_args(self):
        """test case with valid arguments """
        square = Square(5, 4, 3, 12)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 12)

    def test_init_with_invalid_arguments(self):
        """Test case with invalid arguments"""
        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(ValueError):
            Square(-5)

        with self.assertRaises(TypeError):
            Square(5.5)

    def test_str(self):
        """Test square string method """
        s1 = Square(5, 4, 3, 12)
        expected = "[Square] (12) 4/3 - 5"
        self.assertEqual(str(s1), expected)

    def test_update_method(self):
        """test the square update method"""
        s2 = Square(5)

        s2.update(10)
        self.assertEqual(s2.id, 10)

        s2.update(1, 2)
        self.assertEqual(s2.id, 1)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)

        s2.update(1, 2, 3, 4)
        self.assertEqual(s2.id, 1)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)

        s2.update(size=7, y=1, id=89)
        self.assertEqual(s2.width, 7)
        self.assertEqual(s2.y, 1)
        self.assertEqual(s2.id, 89)
