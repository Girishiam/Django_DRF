from django.test import SimpleTestCase

from app import cal

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding two numbers together"""
        res = cal.cal(5, 6)
        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        """Test subtracting two numbers"""
        res = cal.subtract(10, 5)
        self.assertEqual(res, 5)
