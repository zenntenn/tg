from django.test import TestCase
from game.models import Chronicle


# Create your tests here.
class ChronicleTest(TestCase):
    def setUp(self):
        self.chronicle = Chronicle.objects.create(name="Test Chronicle")

    def test_add_story(self):
        self.assertEqual(self.chronicle.total_stories(), 0)
        self.chronicle.add_story("Test Story")
        self.assertEqual(self.chronicle.total_stories(), 1)
