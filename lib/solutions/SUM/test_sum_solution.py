from sum_solution import compute
import unittest


class TestCompute(unittest.TestCase):

    def test_compute(self):
        self.assertEqual(compute(1, 2), 3)
        self.assertEqual(compute(1, 1), 2)
        self.assertEqual(compute(100, 1000), 1100)


if __name__ == "__main__":
    unittest.main()
