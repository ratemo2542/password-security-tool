import unittest
from password_tool import generate, score

class PasswordTests(unittest.TestCase):
    def test_generator_length_and_classes(self):
        value = generate(24)
        self.assertEqual(len(value), 24)
        self.assertTrue(any(c.islower() for c in value))
        self.assertTrue(any(c.isupper() for c in value))
        self.assertTrue(any(c.isdigit() for c in value))

    def test_length_validation(self):
        with self.assertRaises(ValueError): generate(5)

    def test_score_feedback(self):
        label, tips = score("abc")
        self.assertEqual(label, "Very weak")
        self.assertTrue(tips)

if __name__ == "__main__": unittest.main()
