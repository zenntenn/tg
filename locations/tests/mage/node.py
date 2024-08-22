from unittest import mock
from unittest.mock import Mock

from characters.models.core import MeritFlaw
from characters.models.mage import Resonance
from core.models import Noun
from django.test import TestCase
from django.urls import reverse
from game.models import ObjectType
from locations.models.mage import Node, NodeMeritFlawRating, NodeResonanceRating


class TestNode(TestCase):
    def setUp(self):
        node = ObjectType.objects.create(name="node", type="loc", gameline="mta")
        for i in range(1, 11):
            Resonance.objects.create(name=f"Resonance {i}")
        for i in range(1, 6):
            for j in [1, -1]:
                if j == 1:
                    t = "Merit"
                else:
                    t = "Flaw"
                tmp = MeritFlaw.objects.create(name=f"Node {t} {i}")
                tmp.add_rating(i * j)
                tmp.allowed_types.add(node)
        self.node = Node.objects.create(name="Test Node")
        for i in range(10):
            Noun.objects.create(name=f"Node Noun {i}")

    # def test_gauntlet_rating(self):
    #     self.assertEqual(self.node.gauntlet, 3)

    def test_add_resonance(self):
        res = Resonance.objects.order_by("?").first()
        self.assertEqual(self.node.resonance_rating(res), 0)
        self.assertTrue(self.node.add_resonance(res))
        self.assertEqual(self.node.resonance_rating(res), 1)

    def test_filter_resonance(self):
        self.assertEqual(len(self.node.filter_resonance()), 10)
        for res in Resonance.objects.order_by("?")[:3]:
            self.assertTrue(self.node.add_resonance(res))
        self.assertEqual(len(self.node.filter_resonance(maximum=0)), 7)

    def test_total_resonance(self):
        resonance = Resonance.objects.order_by("?")[:2]
        for res in resonance:
            self.node.add_resonance(res)
            self.node.add_resonance(res)
        self.assertEqual(self.node.total_resonance(), 4)
        self.assertNotEqual(self.node.total_resonance(), 5)
        self.node.add_resonance(resonance[1])
        self.assertEqual(self.node.total_resonance(), 5)

    def test_check_resonance(self):
        r = Resonance.objects.create(name="Test Res")
        self.assertTrue(self.node.check_resonance(r))
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.assertFalse(self.node.check_resonance(r))
        r2 = Resonance.objects.create(name="Test Res 2", forces=True)
        self.assertFalse(self.node.check_resonance(r2, sphere="life"))
        self.assertTrue(self.node.check_resonance(r2, sphere="forces"))
        self.assertTrue(self.node.check_resonance(r2))
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.assertFalse(self.node.check_resonance(r2, sphere="forces"))

    def test_has_resonance(self):
        self.node.rank = 1
        resonance = Resonance.objects.create(name="Test Resonance")
        self.node.add_resonance(resonance)
        self.assertTrue(self.node.has_resonance())

    def test_resonance_rating(self):
        resonance = Resonance.objects.create(name="Test Resonance")
        rating = 3
        NodeResonanceRating.objects.create(
            node=self.node, resonance=resonance, rating=rating
        )
        self.assertEqual(self.node.resonance_rating(resonance), rating)

    def test_set_rank(self):
        self.assertEqual(self.node.rank, 0)
        self.assertTrue(self.node.set_rank(3))
        self.assertEqual(self.node.rank, 3)
        self.assertEqual(self.node.points, 9)

    def test_resonance_postprocessing(self):
        merit1 = MeritFlaw.objects.create(name="Corrupted")
        merit1.add_rating(0)
        # merit2 = MeritFlaw.objects.create(name="Sphere Attuned")
        # merit2.add_rating(0)
        Resonance.objects.create(name="Corrupted")
        # Resonance.objects.create(
        #     name="Sphered",
        #     correspondence=True,
        #     entropy=True,
        #     forces=True,
        #     matter=True,
        #     life=True,
        #     time=True,
        #     prime=True,
        #     spirit=True,
        #     mind=True,
        # )
        self.node.merits_and_flaws.add(merit1)
        # self.node.merits_and_flaws.add(merit2)
        self.node.save()
        self.node.resonance_postprocessing()
        self.assertEqual(self.node.total_resonance(), 2)
        self.assertIn("Corrupted", [x.name for x in self.node.resonance.all()])
        # self.assertIn("Sphered", [x.name for x in self.node.resonance.all()])

    def test_add_mf(self):
        num = self.node.total_mf()
        self.assertFalse(
            self.node.add_mf(MeritFlaw.objects.get(name="Node Merit 3"), 4)
        )
        self.assertTrue(self.node.add_mf(MeritFlaw.objects.get(name="Node Merit 3"), 3))
        self.assertEqual(self.node.total_mf(), num + 3)

    def test_filter_mf(self):
        self.assertEqual(len(self.node.filter_mf()), 10)
        self.assertEqual(len(self.node.filter_mf(minimum=0)), 5)
        for mf in MeritFlaw.objects.all():
            if "Merit" in mf.name:
                self.node.add_mf(mf, mf.min_rating)
        self.assertEqual(len(self.node.filter_mf()), 5)
        self.assertEqual(len(self.node.filter_mf(maximum=0)), 5)
        for mf in MeritFlaw.objects.all():
            if "Flaw" in mf.name:
                self.node.add_mf(mf, mf.min_rating)
        self.assertEqual(len(self.node.filter_mf()), 0)

    def test_total_mf(self):
        self.assertEqual(self.node.total_mf(), 0)
        self.node.add_mf(MeritFlaw.objects.get(name="Node Merit 3"), 3)
        self.assertEqual(self.node.total_mf(), 3)
        self.node.add_mf(MeritFlaw.objects.get(name="Node Flaw 2"), -2)
        self.assertEqual(self.node.total_mf(), 1)

    def test_mf_rating(self):
        mf = MeritFlaw.objects.create(name="Test MF")
        mf.add_ratings([1, 2, 3])
        rating = 2
        NodeMeritFlawRating.objects.create(node=self.node, mf=mf, rating=rating)
        self.assertEqual(self.node.mf_rating(mf), rating)

    def test_set_size(self):
        self.assertEqual(self.node.size, 0)
        self.assertEqual(self.node.get_size_display(), "Average Room")
        self.assertTrue(self.node.set_size(2))
        self.assertEqual(self.node.size, 2)
        self.assertEqual(self.node.get_size_display(), "Large Building")
        self.assertTrue(self.node.set_size(-2))
        self.assertEqual(self.node.size, -2)
        self.assertEqual(self.node.get_size_display(), "Household Object")

    def test_set_ratio(self):
        self.assertEqual(self.node.ratio, 0)
        self.assertEqual(self.node.get_ratio_display(), "0.5")
        self.assertTrue(self.node.set_ratio(2))
        self.assertEqual(self.node.ratio, 2)
        self.assertEqual(self.node.get_ratio_display(), "1.0")
        self.assertTrue(self.node.set_ratio(-2))
        self.assertEqual(self.node.ratio, -2)
        self.assertEqual(self.node.get_ratio_display(), "0.0")

    def test_update_output(self):
        self.node.set_rank(2)
        self.assertEqual(self.node.ratio, 0)
        self.node.update_output()
        self.assertEqual(self.node.quintessence_per_week, 3)
        self.assertEqual(self.node.tass_per_week, 3)
        self.node.set_ratio(1)
        self.assertEqual(self.node.ratio, 1)
        self.node.update_output()
        self.assertEqual(self.node.quintessence_per_week, 4)
        self.assertEqual(self.node.tass_per_week, 2)

    def test_has_output_forms(self):
        self.assertFalse(self.node.has_output_forms())
        self.node.set_output_forms("Quintessence", "Tass")
        self.assertTrue(self.node.has_output_forms())

    def test_set_output_forms(self):
        self.assertFalse(self.node.has_output_forms())
        self.assertTrue(self.node.set_output_forms("Quintessence", "Tass"))
        self.assertTrue(self.node.has_output_forms())

    def test_has_output(self):
        self.node.set_rank(3)
        self.assertFalse(self.node.has_output())
        self.node.update_output()
        self.assertTrue(self.node.has_output())


class TestRandomNode(TestCase):
    def setUp(self):
        node = ObjectType.objects.create(name="node", type="loc", gameline="mta")
        for i in range(1, 11):
            Resonance.objects.create(name=f"Resonance {i}")
        for i in range(1, 6):
            for j in [1, -1]:
                if j == 1:
                    t = "Merit"
                else:
                    t = "Flaw"
                tmp = MeritFlaw.objects.create(name=f"Node {t} {i}")
                tmp.add_rating(i * j)
                tmp.allowed_types.add(node)
        self.node = Node.objects.create(name="")
        for i in range(10):
            Noun.objects.create(name=f"Node Noun {i}")

    def test_random_name(self):
        self.assertFalse(self.node.has_name())
        self.node.random_name()
        self.assertTrue(self.node.has_name())

    def test_random_rank(self):
        self.assertEqual(self.node.rank, 0)
        self.node.random_rank()
        self.assertNotEqual(self.node.rank, 0)

    def test_random_resonance(self):
        self.assertEqual(self.node.total_resonance(), 0)
        self.node.random_resonance()
        self.assertEqual(self.node.total_resonance(), 1)

    def test_random_mf(self):
        num = self.node.total_mf()
        while not self.node.random_mf(minimum=0):
            assert False
        self.assertGreater(self.node.total_mf(), num)

    def test_random_size(self):
        mocker = Mock()
        mocker.side_effect = [0, 2]
        with mock.patch("random.choice", mocker):
            self.node.random_size()
            self.assertEqual(self.node.size, 0)
            self.node.random_size()
            self.assertEqual(self.node.size, 2)

    def test_random_ratio(self):
        mocker = Mock()
        mocker.side_effect = [0, 2]
        with mock.patch("random.choice", mocker):
            self.node.random_ratio()
            self.assertEqual(self.node.ratio, 0)
            self.node.random_ratio()
            self.assertEqual(self.node.ratio, 2)

    def test_random_forms(self):
        self.assertFalse(self.node.has_output_forms())
        self.node.random_forms()
        self.assertTrue(self.node.has_output_forms())

    def test_random(self):
        self.assertEqual(self.node.points, 0)
        self.node.random()
        self.assertGreaterEqual(self.node.total_resonance(), self.node.rank)
        self.assertNotEqual(self.node.rank, 0)
        self.assertEqual(self.node.points, 0)
        self.assertTrue(self.node.has_resonance())
        self.assertTrue(self.node.has_output_forms())
        self.assertTrue(self.node.has_output())


class TestNodeDetailView(TestCase):
    def setUp(self) -> None:
        self.location = Node.objects.create(name="Test Node")
        self.url = self.location.get_absolute_url()

    def test_location_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/node/detail.html")


class TestNodeCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Node",
            "reality_zone": "Test RZ",
            "description": "Test",
            "rank": 2,
            "size": -1,
            "quintessence_per_week": 1,
            "quintessence_form": "quint",
            "tass_per_week": 3,
            "tass_form": "tass",
        }
        self.url = Node.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/node/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Node.objects.count(), 1)
        self.assertEqual(Node.objects.first().name, "Node")


class TestNodeUpdateView(TestCase):
    def setUp(self):
        self.node = Node.objects.create(
            name="Test Node",
            description="Test description",
        )
        self.valid_data = {
            "name": "Node Updated",
            "reality_zone": "Test RZ",
            "description": "Test",
            "rank": 2,
            "size": -1,
            "quintessence_per_week": 1,
            "quintessence_form": "quint",
            "tass_per_week": 3,
            "tass_form": "tass",
        }
        self.url = self.node.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/node/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.node.refresh_from_db()
        self.assertEqual(self.node.name, "Node Updated")
        self.assertEqual(self.node.description, "Test")
