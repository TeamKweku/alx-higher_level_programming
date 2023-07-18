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

class TestBaseToJSONString(unittest.TestCase):
    """Unittest for the to_json_string method """
    
    def test_to_json_string_with_None(self):
        """Testing with None"""
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_with_empty_list(self):
        """testing with an empty list"""
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_with_dict(self):
        """testing with a dict id"""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_with_dict_str(self):
        """testing for return of to_json_string func """
        b1 = Base.to_json_string([{'id': 12}])
        self.assertEqual(type(b1), type('str'))

class TestBaseFromJSONString(unittest.TestCase):
    """Tesing the from_json_string function """
    
    def test_from_json_string_with_None(self):
        """Testing fo None as argument """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_with_string(self):
        """ Testing with string as argument """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_dict(self):
        """ Testing from_json_string with a dict """
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

    def test_from_json_string_with_dict(self):
        """ Testing from_json_string with dict's return """
        b1 = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(type(b1), type([]))
