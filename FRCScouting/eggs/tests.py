from django.test import TestCase
from .views import get_dog

class DogTestCase(TestCase):
    def test_get_dog(self):
        self.assertNotEqual(get_dog(), None)
