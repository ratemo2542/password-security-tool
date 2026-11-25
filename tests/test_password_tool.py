import unittest
import main

class PasswordTests(unittest.TestCase):
    def test_generator_length_and_required_classes(self):
        password, alphabet_size = main.generate(24)
        self.assertEqual(len(password), 24)
        self.assertGreater(alphabet_size, 0)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(not c.isalnum() for c in password))

    def test_minimum_length(self):
        with self.assertRaises(ValueError):
            main.generate(11)

    def test_no_symbols(self):
        password, _ = main.generate(16, symbols=False)
        self.assertTrue(password.isalnum())

if __name__ == "__main__":
    unittest.main()
