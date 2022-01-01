from django.test import TestCase

import unittest

from .models import MessageToTeacher

# Create your tests here.

class TestMessageToTeacher(unittest.TestCase):

    def __str__(self):
        return self.message
    
    def test_urls(self):
        pass

    def test_views(self):
        pass

if __name__ == '__main__':
    unittest.main()

