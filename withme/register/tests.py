from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")  
        self.login_url = reverse("login") 

    def test_register_user_success(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "test1",
            "date_of_birth": "2000-01-01",
            "city": "London",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, "testuser")

    def test_register_missing_field(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            # password missing
            "date_of_birth": "2000-01-01",
            "city": "London",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_duplicate_username(self):
        CustomUser.objects.create_user(
            username="testuser", email="a@test.com", password="test1"
        )
        data = {
            "username": "testuser",
            "email": "b@test.com",
            "password": "test1",
            "date_of_birth": "2000-01-01",
            "city": "London",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        """A registered user can log in successfully"""
        CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="test1"
        )
        data = {"username": "testuser", "password": "test1"}
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)

    def test_login_wrong_password(self):
        CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="test1"
        )
        data = {"username": "testuser", "password": "wrong"}
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_nonexistent_user(self):
        data = {"username": "nouser", "password": "test1"}
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_email(self):
        """Registration fails if email is invalid"""
        data = {
            "username": "user1",
            "email": "email",
            "password": "test1",
            "date_of_birth": "2000-01-01",
            "city": "London",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_blank_fields(self):
        data = {
            "username": "",
            "email": "",
            "password": "",
            "date_of_birth": "",
            "city": "",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
