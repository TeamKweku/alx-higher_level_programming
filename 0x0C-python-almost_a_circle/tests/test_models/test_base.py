import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        """test without id assignment with the base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_init_with_id(self):
        """test a case of id assignment"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_init_wih_negative_id(self):
        """test a case of negative id number"""
        base = Base(-5)
        self.assertEqual(base.id, -5)

    def test_init_with_zero(self):
        """Test case when initializing with id of zero"""
        base = Base(0)
        self.assertEqual(base.id, 0)
