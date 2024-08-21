

from django.test import TestCase

from characters.models.mage.cabal import Cabal


class TestCabal(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        mage_setup(self.player)

    def test_cabal_creation(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.members.set(Mage.objects.all())
        cabal.leader = Mage.objects.first()
        cabal.save()
        self.assertEqual(cabal.members.count(), 5)
        self.assertIsNotNone(cabal.leader)

    def test_random(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.random(num_chars=5, new_characters=False)
        self.assertEqual(cabal.members.count(), 5)
        for mage in Mage.objects.all():
            self.assertIn(mage, cabal.members.all())
        cabal = Cabal.objects.create(name="Cabal 2")
        cabal.random(num_chars=5, new_characters=True)
        self.assertEqual(cabal.members.count(), 5)

    def test_exception(self):
        cabal = Cabal.objects.create(name="Cabal 10")
        with self.assertRaises(ValueError):
            cabal.random(num_chars=10, new_characters=False)

    def test_str(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        self.assertEqual(str(cabal), "Cabal 1")

class TestCabalDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.cabal = Cabal.objects.create(name="Test Cabal")

    def test_cabal_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/groups/{self.cabal.id}/")
        self.assertEqual(response.status_code, 200)

    def test_cabal_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/groups/{self.cabal.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/cabal/detail.html")
