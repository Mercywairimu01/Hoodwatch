from unicodedata import name
from django.test import TestCase

from .models import *

class NeighbourhoodTestClass(TestCase):

        def setUp(self):
            self.new_neighbourhood=NeighbourHood(name='Langata',occupant_count=201,admin='hood')
        def tearDown(self):
            NeighbourHood.objects.all().delete()


        # test for instance
        def test_instance(self):
            self.assertTrue(isinstance(self.new_neighbourhood,NeighbourHood))
            
        # test for save method
        def test_save_neighbourhood(self):
            self.new_neighbourhood.create_neighborhood()
            neighborhood=NeighbourHood.objects.all()
            self.assertTrue(len(neighborhood)>0)
            
        def test_delete_neighbourhood(self):
            self.new_neighbourhood.create_neighborhood()
            self.new_neighbourhood.delete_neighborhood()
            neighborhood=NeighbourHood.objects.all()
            self.assertEqual(len(neighborhood),0)
            
            
class Testpost(TestCase):
    def setUp(self):
        self.post = Post(title='Delani Studion', author= User.objects.create(username='mercy'),hood = NeighbourHood.objects.create(location='Ruiru',occupant_count=3))
        self.user = User(id=1, username='mercy', password='pre123456')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save(self):
        self.post.save()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.posts()
        self.assertTrue(len(posts) > 0)

class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.test_business = Business.objects.create(name='Spashop',bs_image='example.jpg',user='sareto',email='example@gmail.com',neighbourhood='kitengela')
        self.test_business.save()
        
    def test_save_method(self):
        self.test_business.save()
        test_business = Business.objects.all()
        self.assertTrue(len(test_business) > 0)
        
    def test_delete_method(self):
        self.Business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)
    def tearDown(self):
        Business.objects.all().delete() 