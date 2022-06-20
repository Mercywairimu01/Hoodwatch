from django.db import models
from PIL import Image
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    occupant_count=models.IntegerField()
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_img = models.ImageField(upload_to='images/')
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)
   

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
    @classmethod
    def update_neighborhood(cls,neighborhood_id,location):
      return cls.objects.filter(id=neighborhood_id).update(location=location)

    @classmethod
    def update_occupants(cls,neighborhood_id,occupant_count):
        return cls.objects.filter(id=neighborhood_id).update(occupant_count)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    about = models.TextField(max_length=254, blank=True)
    image = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, **kwargs):
        super().save( **kwargs)
        img= Image.open(self. image.path)
        
        if img.height > 250 or img.width > 250:
            output_size = (250, 2500)
            img.thumbnail(output_size)
            img.save(self. image.path)


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    bs_image = models.ImageField(upload_to='images/',blank=True, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        return cls.objects.filter(id=business_id)

    @classmethod
    def update_business(cls,business_id,location):
      return cls.objects.filter(id=business_id).update(location=location)

    @classmethod
    def search_business(cls,search_name):
        search_results = cls.objects.filter(Q(name__icontains=search_name))
        return search_results

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    description=models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post')
    
    
    def __str__(self):
     return self.title

    @classmethod
    def save_post(self):
        self.save()

    @classmethod
    def delete_post(self):
        self.delete()
    @classmethod    
    def user_post(cls,username):
        posts= cls.objects.filter(author_id=username)
        return posts

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Meta:
      ordering = ['-id']
