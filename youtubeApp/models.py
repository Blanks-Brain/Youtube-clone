from django.db import models
from django.conf import settings
# Create your models here.


User=settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.name
    
class Channel(models.Model):
    name = models.CharField(max_length = 150)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    channel_art=models.ImageField(upload_to="channel/", default='default_art.jpg')
    channel_icon=models.ImageField(upload_to='profile/', default='default_icon.png')
    slug = models.SlugField()
    description = models.TextField(blank=True, null = True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name