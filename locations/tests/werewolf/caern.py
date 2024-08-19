from django.test import TestCase

from locations.models.werewolf.caern import Caern


# Create your tests here.
class TestCaern(TestCase):
    def test_gauntlet(self):
        caern_1 = Caern.objects.create(name="Test Caern 1", rank=1)
        self.assertEqual(caern_1.gauntlet, 4)
        caern_2 = Caern.objects.create(name="Test Caern 2", rank=2)
        self.assertEqual(caern_2.gauntlet, 4)
        caern_3 = Caern.objects.create(name="Test Caern 3", rank=3)
        self.assertEqual(caern_3.gauntlet, 3)
        caern_4 = Caern.objects.create(name="Test Caern 4", rank=4)
        self.assertEqual(caern_4.gauntlet, 3)
        caern_5 = Caern.objects.create(name="Test Caern 5", rank=5)
        self.assertEqual(caern_5.gauntlet, 2)
