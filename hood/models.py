from django.db import models
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
      return cls.objects_filter(id=neighborhood_id).update(location=location)

    @classmethod
    def update_occupants(cls,neighborhood_id,occupant_count):
        return cls.objects_filter(id=neighborhood_id).update(occupant_count)



