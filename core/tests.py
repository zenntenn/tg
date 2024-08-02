from django.contrib.auth.models import User
from django.test import TestCase, LiveServerTestCase
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from characters.models.core import CharacterModel

MAX_WAIT = 10
# Create your tests here.
class FunctionalTest(LiveServerTestCase):
    """Base case for Functional Tests"""

    def setUp(self) -> None:
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):  # pragma: no cover
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("id_character_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as exception:
                if time.time() - start_time > MAX_WAIT:
                    raise exception
                time.sleep(0.5)

    def clean_url(self, url):
        return url.replace(self.live_server_url + "/", "")
    
class TestHomeView(TestCase):
    """Manages Tests for the HomeView and Template"""

    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        User.objects.create_superuser("Test Admin", "admin@admin.com", "testadmin")

    def test_home_status_code(self):
        """Tests that the page exists"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        """Tests that the correct template is loaded"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "core/index.html")

    def test_includes_patreon(self):
        """Tests site contains link to Patreon"""
        response = self.client.get("/")
        self.assertContains(response, "Patron")
        self.assertContains(response, "https://www.patreon.com/bePatron?u=62722820")

    def test_includes_storytellers_vault(self):
        """Tests site contains Stoyteller's Vault logo"""
        response = self.client.get("/")
        self.assertContains(response, "Storyteller's Vault")
        self.assertContains(response, "stv.png")

    def test_includes_dark_pack(self):
        """Tests site contains Dark Pack Logo"""
        response = self.client.get("/")
        self.assertContains(response, "Dark Pack")
        self.assertContains(response, "dark_pack.png")

        self.assertTemplateUsed(response, "core/index.html")


class TestModel(TestCase):
    def setUp(self):
        # Model is abstract, using a descendant class to test methods
        self.model = CharacterModel.objects.create(name="")
        self.user = User.objects.create_user(username="Test User")

    def test_has_name(self):
        self.assertFalse(self.model.has_name())
        self.model.set_name("Test")
        self.assertTrue(self.model.has_name())

    def test_set_name(self):
        self.assertFalse(self.model.has_name())
        self.assertTrue(self.model.set_name("Test"))
        self.assertTrue(self.model.has_name())

    def test_has_description(self):
        self.assertFalse(self.model.has_description())
        self.model.set_description("Test")
        self.assertTrue(self.model.has_description())

    def test_set_description(self):
        self.assertFalse(self.model.has_description())
        self.assertTrue(self.model.set_description("Test"))
        self.assertTrue(self.model.has_description())

    def test_has_owner(self):
        self.assertFalse(self.model.has_owner())
        self.model.set_owner(self.user)
        self.assertTrue(self.model.has_owner())

    def test_set_owner(self):
        self.assertFalse(self.model.has_owner())
        self.assertTrue(self.model.set_owner(self.user))
        self.assertTrue(self.model.has_owner())

    def test_update_status(self):
        self.assertEqual(self.model.status, "Un")
        self.assertEqual(self.model.get_status_display(), "Unfinished")
        self.assertTrue(self.model.update_status("App"))
        self.assertEqual(self.model.status, "App")
        self.assertEqual(self.model.get_status_display(), "Approved")

    def test_toggle_display(self):
        self.assertTrue(self.model.display)
        self.assertTrue(self.model.toggle_display())
        self.assertFalse(self.model.display)
