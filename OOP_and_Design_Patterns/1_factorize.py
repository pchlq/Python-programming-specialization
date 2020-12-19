import unittest

class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        cases = ['string', 1.5]
        for x in cases:
            with self.subTest(x=x):
                with self.assertRaises(TypeError):
                    factorize(x)

    def test_negative(self):
        cases = [-1, -10, -100]
        for x in cases:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        for x in [0, 1]:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        cases = [3, 13, 29]
        for x in cases:
            with self.subTest(x=x):
                d = 2
                while d * d <= x and x % d != 0:
                    d += 1
                is_prime = d * d > x

                self.assertTrue(is_prime)
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        for x, res in (6, (2, 3)), (26, (2, 13)), (121, (11, 11)):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), res)

    def test_many_multipliers(self):
        for x, res in (
            1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)
        ):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), res)


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass
