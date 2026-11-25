import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import generate

class PasswordTests(unittest.TestCase):
    def test_length(self):
        password, _ = generate(18)
        self.assertEqual(len(password), 18)
    def test_minimum(self):
        with self.assertRaises(ValueError):
            generate(8)
    def test_symbols_can_be_disabled(self):
        password, _ = generate(16, False)
        self.assertTrue(password.isalnum())
if __name__ == "__main__":
    unittest.main()
