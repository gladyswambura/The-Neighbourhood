from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def save_profile(self):
        self.save()
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def delete_profile(self):
        self.delete()


    def __str__(self):
        return f'{self.user.username} -profile'


class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    description = models.TextField()
    health_officer = models.CharField(max_length=60, null=True, blank=True)
    police_officer = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


