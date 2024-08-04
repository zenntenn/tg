from characters.models.core import CharacterModel
from django.test import TestCase
from game.models import Chronicle, ObjectType, Scene, Story
from locations.models.core import LocationModel


# Create your tests here.
class ChronicleTest(TestCase):
    def setUp(self):
        self.chronicle = Chronicle.objects.create(name="Test Chronicle")

    def test_add_story(self):
        self.assertEqual(self.chronicle.total_stories(), 0)
        self.chronicle.add_story("Test Story")
        self.assertEqual(self.chronicle.total_stories(), 1)


class StoryTest(TestCase):
    def setUp(self):
        self.chronicle = Chronicle.objects.create(name="Test Chronicle")
        self.story = Story.objects.create(name="Test Story", chronicle=self.chronicle)
        self.location = LocationModel.objects.create(
            name="Test Location", chronicle=self.chronicle
        )

    def test_add_scene(self):
        self.assertEqual(self.story.total_scenes(), 0)
        self.assertEqual(self.story.total_locations(), 0)
        self.story.add_scene("Test Scene", self.location)
        self.assertEqual(self.story.total_scenes(), 1)
        self.assertEqual(self.story.total_locations(), 1)


class SceneTest(TestCase):
    def setUp(self):
        self.chronicle = Chronicle.objects.create(name="Test Chronicle")
        self.story = Story.objects.create(name="Test Story", chronicle=self.chronicle)
        self.location = LocationModel.objects.create(
            name="Test Location", chronicle=self.chronicle
        )
        self.scene = Scene.objects.create(
            name="Test Scene", story=self.story, location=self.location
        )
        self.char = CharacterModel.objects.create(
            name="Test Character", chronicle=self.chronicle
        )
        self.npc = CharacterModel.objects.create(
            name="Test NPC", chronicle=self.chronicle, npc=True
        )

    def test_close_scene(self):
        self.assertFalse(self.scene.finished)
        self.scene.close()
        self.assertTrue(self.scene.finished)
        self.scene.close()
        self.assertTrue(self.scene.finished)

    def test_add_character(self):
        self.assertEqual(self.scene.total_characters(), 0)
        self.assertEqual(self.story.total_pcs(), 0)
        self.assertEqual(self.story.total_npcs(), 0)
        self.scene.add_character(self.char)
        self.assertEqual(self.scene.total_characters(), 1)
        self.assertEqual(self.story.total_pcs(), 1)
        self.assertEqual(self.story.total_npcs(), 0)
        self.scene.add_character(self.npc)
        self.assertEqual(self.scene.total_characters(), 2)
        self.assertEqual(self.story.total_pcs(), 1)
        self.assertEqual(self.story.total_npcs(), 1)

    def test_add_post(self):
        self.scene.add_character(self.char)
        self.assertEqual(self.scene.total_posts(), 0)
        post = self.scene.add_post(self.char, "", "Here's a post message.")
        self.assertEqual(self.scene.total_posts(), 1)
        self.assertEqual(post.display_name, self.char.name)
        self.assertEqual(post.message, "Here's a post message.")
        self.assertEqual(str(post), "Test Character: Here's a post message.")


class TestChronicleDetailView(TestCase):
    def setUp(self):
        self.chronicle = Chronicle.objects.create(name="Test Chronicle")

    def test_chronicle_detail_view_status_code(self):
        response = self.client.get(f"/game/chronicle/{self.chronicle.id}")
        self.assertEqual(response.status_code, 200)

    def test_chronicle_detail_view_template(self):
        response = self.client.get(f"/game/chronicle/{self.chronicle.id}")
        self.assertTemplateUsed(response, "game/chronicle/detail.html")


class TestStoryDetailView(TestCase):
    def setUp(self):
        self.chronicle = Chronicle.objects.create(name="Test Chronicle")
        self.story = Story.objects.create(name="Test Story", chronicle=self.chronicle)

    def test_story_detail_view_status_code(self):
        response = self.client.get(f"/game/story/{self.story.id}")
        self.assertEqual(response.status_code, 200)

    def test_story_detail_view_template(self):
        response = self.client.get(f"/game/story/{self.story.id}")
        self.assertTemplateUsed(response, "game/story/detail.html")


class TestSceneDetailView(TestCase):
    def setUp(self):
        self.chronicle = Chronicle.objects.create(name="Test Chronicle")
        self.story = Story.objects.create(name="Test Story", chronicle=self.chronicle)
        self.scene = Scene.objects.create(name="Test Scene", story=self.story)

    def test_scene_detail_view_status_code(self):
        response = self.client.get(f"/game/scene/{self.scene.id}")
        self.assertEqual(response.status_code, 200)

    def test_scene_detail_view_template(self):
        response = self.client.get(f"/game/scene/{self.scene.id}")
        self.assertTemplateUsed(response, "game/scene/detail.html")


class TestObjectType(TestCase):
    def test_str(self):
        x = ObjectType.objects.create(name="Test", type="loc", gameline="mta")
        self.assertEqual(str(x), "Mage: the Ascension/Location/Test")
