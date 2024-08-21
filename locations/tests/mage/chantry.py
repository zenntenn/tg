


from django.test import TestCase

from characters.models.core.human import Human
from characters.models.mage.faction import MageFaction
from items.models.mage.grimoire import Grimoire
from locations.models.mage.chantry import Chantry
from locations.models.mage.library import Library


class TestChantry(TestCase):
    def setUp(self) -> None:
        self.chantry = Chantry.objects.create(name="")
        self.library = Library.objects.create(rank=3)
        self.grimoire1 = Grimoire.objects.create()
        self.grimoire2 = Grimoire.objects.create()
        self.grimoire3 = Grimoire.objects.create()
        self.library.add_book(self.grimoire1)
        self.library.add_book(self.grimoire2)
        self.library.add_book(self.grimoire3)
        self.node1 = Node.objects.create(name="node1", rank=1)
        self.node2 = Node.objects.create(name="node2", rank=1)
        self.human = Human.objects.create(name="human")
        self.cabal = Cabal.objects.create(name="cabal")
        self.faction = MageFaction.objects.create(name="faction")
        self.player = User.objects.create_user(username="Test")
        mage_setup(self.player)
        grimoire_setup()

    def test_trait_cost(self):
        self.assertEqual(self.chantry.trait_cost("allies"), 2)
        self.assertEqual(self.chantry.trait_cost("arcane"), 2)
        self.assertEqual(self.chantry.trait_cost("backup"), 2)
        self.assertEqual(self.chantry.trait_cost("cult"), 2)
        self.assertEqual(self.chantry.trait_cost("elders"), 2)
        self.assertEqual(self.chantry.trait_cost("integrated_effects"), 2)
        self.assertEqual(self.chantry.trait_cost("library_rating"), 2)
        self.assertEqual(self.chantry.trait_cost("retainers"), 2)
        self.assertEqual(self.chantry.trait_cost("spies"), 2)
        self.assertEqual(self.chantry.trait_cost("node_rating"), 3)
        self.assertEqual(self.chantry.trait_cost("resources"), 3)
        self.assertEqual(self.chantry.trait_cost("enhancement"), 4)
        self.assertEqual(self.chantry.trait_cost("requisitions"), 4)
        self.assertEqual(self.chantry.trait_cost("reality_zone_rating"), 5)

    def test_has_node(self):
        self.chantry.node_rating = 1
        self.assertFalse(self.chantry.has_node())
        self.chantry.nodes.add(self.node1)
        self.assertTrue(self.chantry.has_node())

    def test_total_node(self):
        self.assertEqual(self.chantry.total_node(), 0)
        self.chantry.nodes.add(self.node1)
        self.assertEqual(self.chantry.total_node(), 1)
        self.chantry.nodes.add(self.node2)
        self.assertEqual(self.chantry.total_node(), 2)

    def test_create_nodes(self):
        self.chantry.random_faction()
        self.chantry.random_name()
        self.chantry.node_rating = 0
        self.chantry.create_nodes()
        self.assertEqual(self.chantry.nodes.count(), 0)
        self.assertEqual(self.chantry.total_node(), 0)
        self.chantry.node_rating = 12
        self.chantry.create_nodes()
        self.assertGreater(self.chantry.nodes.count(), 0)
        self.assertEqual(self.chantry.total_node(), 12)
        for node in self.chantry.nodes.all():
            self.assertEqual(node.parent, self.chantry)

    def test_has_library(self):
        self.chantry.library_rating = 3
        self.assertFalse(self.chantry.has_library())
        self.chantry.chantry_library = self.library
        self.chantry.save()
        self.assertTrue(self.chantry.has_library())

    def test_create_library(self):
        self.chantry.library_rating = 0
        self.assertFalse(self.chantry.has_library())
        self.chantry.create_library()
        self.assertTrue(self.chantry.has_library())
        self.assertEqual(self.chantry.chantry_library.num_books(), 0)
        self.chantry.library_rating = 4
        self.chantry.create_library()
        self.assertTrue(self.chantry.has_library())
        self.assertEqual(self.chantry.chantry_library.num_books(), 4)

    def test_set_library(self):
        library = Library.objects.create(name="Test Library", rank=0)
        self.assertFalse(self.chantry.has_library())
        self.chantry.set_library(library)
        self.assertTrue(self.chantry.has_library())

    def test_add_node(self):
        node = Node.objects.create(name="Test Node", rank=3)
        self.chantry.node_rating = 3
        self.assertFalse(self.chantry.has_node())
        self.chantry.add_node(node)
        self.assertTrue(self.chantry.has_node())

    def test_points_spent(self):
        self.assertEqual(self.chantry.points_spent(), 0)
        self.chantry.requisitions = 3
        self.assertEqual(self.chantry.points_spent(), 12)
        self.chantry.node_rating = 8
        self.assertEqual(self.chantry.points_spent(), 36)
        self.chantry.arcane = 1
        self.assertEqual(self.chantry.points_spent(), 38)

    def test_set_rank(self):
        self.chantry.set_rank(5)
        self.assertEqual(self.chantry.rank, 5)

    def test_has_faction(self):
        faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.chantry.has_faction())
        self.chantry.faction = faction
        self.chantry.save()
        self.assertTrue(self.chantry.has_faction())

    def test_set_faction(self):
        faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.chantry.has_faction())
        self.assertTrue(self.chantry.set_faction(faction))
        self.assertEqual(self.chantry.faction, faction)
        self.assertTrue(self.chantry.has_faction())

    def test_has_name(self):
        self.assertFalse(self.chantry.has_name())
        self.chantry.name = "Test"
        self.assertTrue(self.chantry.has_name())

    def test_set_name(self):
        self.assertFalse(self.chantry.has_name())
        self.assertTrue(self.chantry.set_name("Test Chantry"))
        self.assertTrue(self.chantry.has_name())

    def test_has_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.chantry_type = "war"
        self.assertTrue(self.chantry.has_chantry_type())

    def test_set_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.set_chantry_type("war")
        self.assertTrue(self.chantry.has_chantry_type())

    def test_has_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.season = "spring"
        self.assertTrue(self.chantry.has_season())

    def test_set_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.set_season("spring")
        self.assertTrue(self.chantry.has_season())

    def test_get_traits(self):
        self.chantry.allies = 2
        self.chantry.arcane = 3
        self.chantry.backup = 4
        self.chantry.cult = 5
        self.chantry.elders = 6
        self.chantry.integrated_effects = 7
        self.chantry.retainers = 8
        self.chantry.spies = 9
        self.chantry.resources = 10
        self.chantry.enhancement = 11
        self.chantry.requisitions = 12
        self.chantry.reality_zone_rating = 13
        self.chantry.node_rating = 14
        self.chantry.library_rating = 15
        self.chantry.save()

        result = self.chantry.get_traits()
        expected = {
            "allies": 2,
            "arcane": 3,
            "backup": 4,
            "cult": 5,
            "elders": 6,
            "integrated_effects": 7,
            "retainers": 8,
            "spies": 9,
            "resources": 10,
            "enhancement": 11,
            "requisitions": 12,
            "reality_zone": 13,
            "node_rating": 14,
            "library_rating": 15,
        }

        self.assertEqual(result, expected)


class TestRandomChantry(TestCase):
    def setUp(self) -> None:
        self.chantry = Chantry.objects.create(name="")
        self.player = User.objects.create_user(username="Test")
        mage_setup(self.player)
        grimoire_setup()

    def test_random_points(self):
        self.chantry.rank = 1
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 10)
        self.assertLessEqual(self.chantry.points, 20)
        self.chantry.rank = 2
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 21)
        self.assertLessEqual(self.chantry.points, 30)
        self.chantry.rank = 3
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 31)
        self.assertLessEqual(self.chantry.points, 70)
        self.chantry.rank = 4
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 71)
        self.assertLessEqual(self.chantry.points, 100)
        self.chantry.rank = 5
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 101)
        self.assertLessEqual(self.chantry.points, 200)

    def test_random_rank(self):
        self.assertEqual(self.chantry.rank, 0)
        self.chantry.random_rank()
        self.assertNotEqual(self.chantry.rank, 0)

    def test_random(self):
        self.assertFalse(self.chantry.has_faction())
        self.assertFalse(self.chantry.has_name())
        self.assertFalse(self.chantry.has_library())
        self.assertFalse(self.chantry.has_season())
        self.assertFalse(self.chantry.has_chantry_type())
        self.assertTrue(self.chantry.has_node())
        self.chantry.random()
        self.assertTrue(self.chantry.has_season())
        self.assertTrue(self.chantry.has_chantry_type())
        self.assertTrue(self.chantry.has_faction())
        self.assertTrue(self.chantry.has_name())
        self.assertGreater(self.chantry.points, 0)
        self.assertLessEqual(self.chantry.points - self.chantry.points_spent(), 1)

    def test_random_faction(self):
        self.assertFalse(self.chantry.has_faction())
        self.assertTrue(self.chantry.random_faction())
        self.assertTrue(self.chantry.has_faction())

    def test_random_name(self):
        self.assertEqual(self.chantry.name, "")
        m, _ = MageFaction.objects.get_or_create(name="Society of Ether")
        self.chantry.set_faction(m)
        self.assertTrue(self.chantry.random_name())
        self.assertIn("Laboratory", self.chantry.name)

    def test_random_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.random_chantry_type()
        self.assertTrue(self.chantry.has_chantry_type())

    def test_random_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.random_season()
        self.assertTrue(self.chantry.has_season())

    def test_random_populate(self):
        chantry = Chantry.objects.create(
            name="Test Chantry",
            season="spring",
            chantry_type="college",
            leadership_type="anarchy",
            rank=1,
        )
        chantry.random_points()
        chantry.random_faction()
        chantry.random_populate()

        # Check that the number of members in the chantry is at least 3.
        self.assertGreaterEqual(chantry.members.count(), 3)

        # Check that the total number of points of the cabals' members
        # is less than or equal to the chantry's points.
        total_cabal_points = sum(
            sum(x.chantry for x in cabal.members.all())
            for cabal in self.chantry.cabals.all()
        )
        self.assertLessEqual(total_cabal_points, chantry.points)

        # Check that each cabal has at least 3 members.
        for cabal in chantry.cabals.all():
            self.assertGreaterEqual(cabal.members.count(), 3)

    def test_random_leadership_type(self):
        chantry = Chantry.objects.create()
        chantry.random_leadership_type()

        leadership_choices = [choice[0] for choice in Chantry.LEADERSHIP_CHOICES]

        self.assertIn(chantry.leadership_type, leadership_choices)




class TestChantryDetailView(TestCase):
    def setUp(self) -> None:
        self.location = Chantry.objects.create(name="Test Chantry")

    def test_chantry_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_chantry_detail_view_templates(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "wod/locations/mage/chantry/detail.html")
 


