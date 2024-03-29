from django.db import models
from django.conf import settings
import uuid
# Create your models here.


User=settings.AUTH_USER_MODEL


def channel_directory_path(instance, filename):
    return "video_files/channel_{0}/{1}".format(instance.channel.id, filename)

class Category(models.Model):
    name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.name
    
class Channel(models.Model):
    name = models.CharField(max_length = 150)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    channel_art=models.ImageField(upload_to="channel/", default='default_art.jpg')
    channel_icon=models.ImageField(upload_to='profile/', default='default_icon.jpg')
    slug = models.SlugField()
    description = models.TextField(blank=True, null = True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name
    

class VideoFiles(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to=channel_directory_path)
    channel = models.ForeignKey(Channel, on_delete = models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add = True)
    likes = models.ManyToManyField(User, related_name="video_liked")
    dislikes = models.ManyToManyField(User, related_name="video_disliked")
    
    def __str__(self):   
        return f"video_file_{self.id}"
    

class VideoDetail(models.Model):
    videofile = models.OneToOneField(VideoFiles, on_delete = models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    visibility=models.BooleanField(choices=((False, "private"),(True, "public")))
    thumbnail=models.ImageField(upload_to="thumbnail/")
    
    def __str__(self):
        return self.title