import unittest
from main import Senary


class TestSenary(unittest.TestCase):

    def test_addition(self):
        """
        10 (sen) --> 6 (dec)
        20 (sen) --> 12 (dec)
        18 (dec) --> 30 (sen)
        """
        a = Senary(10)
        b = Senary(20)
        result = a + b
        self.assertEqual(result.value, 30)
        self.assertEqual(int(result), 30)

    def test_subtraction(self):
        """
        10 (sen) --> 6 (dec)
        20 (sen) --> 12 (dec)
        6 - 12 = -6
        -6 (dec) --> -10 (sen)
        """
        a = Senary(10)
        b = Senary(20)
        result = a - b
        self.assertEqual(result.value, -10)
        self.assertEqual(int(result), -10)

    def test_from_senary(self):
        result = Senary.from_senary("120")
        self.assertEqual(result.value, 48)
        self.assertEqual(int(result), 48)

    def test_negative_from_senary(self):
        result = Senary.from_senary("-120")
        self.assertEqual(result.value, -48)
        self.assertEqual(int(result), -48)

    def test_to_senary(self):
        a = Senary(48)
        self.assertEqual(a.to_senary(), "120")

    def test_negative_to_senary(self):
        a = Senary(-48)
        self.assertEqual(a.to_senary(), "-120")


if __name__ == "__main__":
    unittest.main()
