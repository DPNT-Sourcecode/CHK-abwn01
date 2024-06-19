from checkout_solution import checkout
import unittest


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ("@", -1),
            (1, -1),
            (True, -1),
            ("A", 50), ("AAAAA", 200), ("AAAAAA", 250), ("AAA", 130),
            ("B", 30), ("BB", 45),
            ("C", 20),
            ("D", 15),
            ("E", 40),
            ("EEB", 80),
            ("EEEBB", 150),
            ("F", 10),
            ("FFF", 20),
            ("FFFF", 30),
            ("FFFFFF", 40),
            ("FFFFFFF", 50),
            ("G", 20),
            ("H", 10), ("HHHHH", 45), ("HHHHHHHHHH", 80),
            ("I", 35),
            ("J", 60),
            ("K", 80), ("KK", 120),
            ("L", 90),
            ("M", 15),
            ("N", 40), ("NNNM", 120),
            ("O", 10),
            ("P", 50), ("PPPPP", 200),
            ("Q", 30), ("QQQ", 80),
            ("R", 50), ("RRRQ", 150),
            ("S", 30),
            ("T", 20),
            ("U", 40), ("UUUU", 120),
            ("V", 50), ("VV", 90), ("VVV", 130),
            ("W", 20),
            ("X", 90),
            ("Y", 10),
            ("Z", 50),
            ("STX", 45),
            ("STXYZ", 82),
            ("XYZS", 62)
        ]

    def test_checkout(self):
        for param, expected in self.test_cases:
            with self.subTest(param=param, expected=expected):
                result = checkout(param)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()


