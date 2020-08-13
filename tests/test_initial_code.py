from unittest import TestCase
from interview_code.initial_code import returns_true

class InitialCodeTests(TestCase):

    def test_returns_true(self):
        self.assertTrue(returns_true)

if __name__ == '__main__':
    unittest.main()
