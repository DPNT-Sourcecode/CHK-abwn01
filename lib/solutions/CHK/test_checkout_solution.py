from checkout_solution import checkout
import unittest


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ("A", 50),
            ("B", 30),
            ("C", 20),
            ("D", 15),
            ("AAA", 130),
            ("BB", 45),
            ("Z", -1),
            (1, -1),
            (True, -1),
            ("AAAAA", 200),
            ("AAAAAA", 250),
            ("E", 40),
            ("EEB", 80),
            ("EEEBB", 150),
            ("F", 10),
            ("FFF", 20),
            ("FFFF", 30)
        ]

    def test_checkout(self):
        for param, expected in self.test_cases:
            with self.subTest(param=param, expected=expected):
                result = checkout(param)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()



