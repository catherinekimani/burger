from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=150)
    user_contact = models.EmailField(max_length=100)
    user_profile = CloudinaryField('image')
    location = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f'{self.user} Profile'

# product
class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(default=0, blank=False)
    description = models.TextField(max_length=600, blank=False)
    image = CloudinaryField('img')

    def __str__(self):
        return self.name