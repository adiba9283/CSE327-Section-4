from django.test import TestCase

import unittest
from .models import ClassAssignment

# Create your tests here.

class TestClassAssignment(unittest.TestCase):

    def __str__(self):
        return self.assignment_name

    def test_urls(self):
        return pass

    def test_views(self):
        return pass
    
if __name__=='__main__':
    unittest.main()
