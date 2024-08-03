from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class TestSignUpView(TestCase):
    """Class that Tests SignUpView"""

    def test_correct_template(self):
        self.client.get("/accounts/")
        self.assertTemplateUsed("registration/login.html")


class TestProfileView(TestCase):
    """Class that Tests the ProfileView"""

    def setUp(self) -> None:
        self.user1 = User.objects.create_user(
            "Test User 1", "test@user1.com", "testpass"
        )
        self.user2 = User.objects.create_user(
            "Test User 2", "test@user2.com", "testpass"
        )
        self.storyteller = User.objects.create_user(
            "Test Storyteller", "test@st.com", "testpass"
        )

        self.storyteller.profile.mta_st = True
        self.storyteller.profile.save()

    def test_template_logged_in(self):
        self.client.login(username="Test User 1", password="testpass")
        response = self.client.get("/accounts/")
        self.assertTemplateUsed(response, "accounts/index.html")
