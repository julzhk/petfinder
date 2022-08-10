from django.test import Client, TestCase

from petgallery.models import AnimalTypes, get_access_token


class TestAPI(TestCase):
    client = Client()

    def test_first(self):
        self.assertEqual(1, 1)

    def test_route(self):
        response = self.client.get('/petapi')
        self.assertEqual(response.status_code, 200)


class Testgallery(TestCase):
    client = Client()

    def test_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_access_token(self):
        token = get_access_token()
        self.assertTrue(token)

    def test_get_animals_list(self):
        animals = AnimalTypes()
        types = [a.name for a in animals.animals]
        self.assertEqual(set(types), {'Dog', 'Cat', 'Rabbit', 'Small & Furry', 'Horse', 'Bird', 'Scales, Fins & Other', 'Barnyard'})
