"""Simple tests for the app."""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Simple test class."""

    def test_add(self):
        """Test add."""
        self.assertEqual(calc.add(1, 1), 2)

    def test_subtract(self):
        """Test subtract."""
        self.assertEqual(calc.subtract(1, 1), 0)
