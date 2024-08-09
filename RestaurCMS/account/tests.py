from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = "test@example.com"
        password = "testpass123"
        first_name = "Test"
        last_name = "TEST"
        phone_number = "+1234567890"
        username = "test"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            username=username,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.phone_number, phone_number)
        self.assertEqual(user.username, username)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for i, (email, expected) in enumerate(sample_emails):
            user = get_user_model().objects.create_user(
                email=email,
                username=f"testEmail{i}",
                password="test123",
                phone_number=f"+123456789{i}",
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user without email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                username="test",
                password="test123",
                phone_number="+1234567890",
            )

    def test_new_user_without_username_raises_error(self):
        """Test creating user without username raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                username=None,
                password="test123",
                phone_number="+1234567890",
            )
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                username="",
                password="test123",
                phone_number="+1234567890",
            )
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                username=" ",
                password="test123",
                phone_number="+1234567890",
            )

    def test_new_user_without_password_raises_error(self):
        """Test creating user without password raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                username="test",
                password=None,
                phone_number="+1234567890",
            )
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                username="test",
                password="",
                phone_number="+1234567890",
            )
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="test@example.com",
                username="test",
                password=" ",
                phone_number="+1234567890",
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            email="test@example.com",
            username="test",
            password="test123",
            phone_number="+1234567890",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


"""
Tests for the django admin modifications.
"""


# class AdminSiteTests(TestCase):
#     """Tests for the django admin."""

#     def setUp(self):
#         """Create user and Client."""
#         self.client = Client()
#         self.admin_user = get_user_model().objects.create_superuser(
#             email="admin@example.com",
#             username="admin",
#             password="test123",
#             phone_number="1234567890",
#         )
#         self.client.force_login(self.admin_user)
#         self.user = get_user_model().objects.create_user(
#             email="user@example.com",
#             username="user",
#             password="test123",
#             phone_number="0987654321",
#         )

#     def test_users_listed(self):
#         """Test that users are listed on user page."""
#         url = reverse("admin:account_customuser_changelist")
#         url = url.replace("/admin/", "/myDashboard/")  # Adjust the URL path
#         res = self.client.get(url)

#         self.assertEqual(res.status_code, 200)  # Ensure the status code is 200
#         self.assertContains(res, self.user.email)
#         self.assertContains(res, self.user.username)
#         self.assertContains(res, self.admin_user.email)
#         self.assertContains(res, self.admin_user.username)
#         self.assertTemplateUsed(res, "admin/auth/user/change_list.html")
