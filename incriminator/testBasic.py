import unittest
from django.test import Client

# Starter code for this basic test case found at:
# https://docs.djangoproject.com/en/2.1/topics/testing/tools/

class BasicTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        # Ensure that the homepage works and the server runs
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
