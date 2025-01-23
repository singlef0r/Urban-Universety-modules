import calc
import unittest

class CalcTest(unittest.TestCase):
    def test_add(self, a, b):
        """
        Test for add function calculator
        :return:
        """
        self.assertEqual(calc.add(a,b), a+b)

    def test_sub(self, a, b):
        """
        Test for sub function calculator
        :return:
        """
        self.assertEqual(calc.sub(a, b), a - b)

    def test_mul(self, a, b):
        """
        Test for mul function calculator
        :return:
        """
        self.assertEqual(calc.mul(a, b), a * b)

    def test_div(self, a, b):
        """
        Test for div function calculator
        :return:
        """
        self.assertEqual(calc.div(a, b), a / b)

if __name__ == '__main__':
    unittest.main()
    # test_add(2, 5)
    # test_sub(2, 2)
    # test_mul(10, 11)
    # test_div(54, 6)