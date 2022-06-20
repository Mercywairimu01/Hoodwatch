from django.test import TestCase
import datetime as dt
from .models import Neighborhood, Profile, Business, Post

# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighborhood(name='Ngong Road')

    def test_hood_instance(self):
        self.assertTrue(isinstance(self.hood, Neighborhood))

    def test_save_hood_method(self):
        self.hood.save_hood()
        hood_object = Neighborhood.objects.all()
        self.assertTrue(len(hood_object) > 0)

    def test_delete_hood_method(self):
        self.hood.save_hood()
        hood_object = Neighborhood.objects.all()
        self.hood.delete_hood()
        hood_object = Neighborhood.objects.all()
        self.assertTrue(len(hood_object) == 0)


class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Mama Mboga')

    def test_hood_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business_method(self):
        self.business.save_business()
        business_object = Business.objects.all()
        self.assertTrue(len(business_object) > 0)

    def test_delete_business_method(self):
        self.business.save_business()
        business_object = Business.objects.all()
        self.business.delete_business()
        business_object = Business.objects.all()
        self.assertTrue(len(business_object) == 0)


