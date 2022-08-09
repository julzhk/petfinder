from django.test import TestCase, Client
from django.test import Client, TestCase


class TestAPI(TestCase):
    client = Client()

    def test_first(self):
        self.assertEqual(1, 1)

    def test_route(self):
        response = self.client.get('/petapi' )
        self.assertEqual(response.status_code, 200)

class Testgallery(TestCase):
    client = Client()


    def test_route(self):
        response = self.client.get('/' )
        self.assertEqual(response.status_code, 200)
