import unittest
from leetcode.problems.Lc0509_fibonacci_number import LC0509_Fibonacci_Number


class LC0509_Fibonacci_Number_Tests(unittest.TestCase):

    def test_LC0509_Fibonacci_Number_00(self):
        lc = LC0509_Fibonacci_Number()

        actual = lc.fib(0)
        self.assertEqual(0, actual)

    def test_LC0509_Fibonacci_Number_01(self):
        lc = LC0509_Fibonacci_Number()

        actual = lc.fib(1)
        self.assertEqual(1, actual)

    def test_LC0509_Fibonacci_Number_02(self):
        lc = LC0509_Fibonacci_Number()

        actual = lc.fib(2)
        self.assertEqual(1, actual)

    def test_LC0509_Fibonacci_Number_03(self):
        lc = LC0509_Fibonacci_Number()

        actual = lc.fib(3)
        self.assertEqual(2, actual)

    def test_LC0509_Fibonacci_Number_04(self):
        lc = LC0509_Fibonacci_Number()

        actual = lc.fib(4)
        self.assertEqual(3, actual)

    def test_LC0509_Fibonacci_Number_05(self):
        lc = LC0509_Fibonacci_Number()

        actual = lc.fib(42)
        self.assertEqual(267914296, actual)


