from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Teacher, Student
from .views import user_login
import json

class TestLogin(TestCase):
    
      def setUp(self):
        self.client = Client()

      def test_user_login_status_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'template/login.html')
