import unittest
from src.solution import largest_divisor

class TestLargestDivisorSpec(unittest.TestCase):

    # 1. Precondition: n > 1
    def test_precondition_invalid_input(self):
        with self.assertRaises(ValueError):
            largest_divisor(1)
        with self.assertRaises(ValueError):
            largest_divisor(0)
        with self.assertRaises(ValueError):
            largest_divisor(-5)

    # 2. res must be a divisor of n
    def test_result_is_divisor(self):
        for n in [10, 21, 50, 99]:
            res = largest_divisor(n)
            self.assertEqual(n % res, 0)

    # 3. res < n
    def test_result_less_than_n(self):
        for n in [8, 12, 27]:
            res = largest_divisor(n)
            self.assertLess(res, n)

    # 4. No larger divisor exists in (res+1 ... n-1)
    def test_no_larger_divisor_exists(self):
        for n in [18, 40, 72]:
            res = largest_divisor(n)
            for k in range(res + 1, n):
                self.assertNotEqual(n % k, 0)

    # 5. 1 <= res <= n-1
    def test_result_in_bounds(self):
        for n in [9, 16, 25, 100]:
            res = largest_divisor(n)
            self.assertTrue(1 <= res <= n - 1)


if __name__ == "__main__":
    unittest.main()
