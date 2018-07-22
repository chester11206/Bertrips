from django.db import models
from bertrips.settings import MEDIA_ROOT
from django.db.models.fields.files import ImageFieldFile

UPLOAD_ROOT = 'upload'
THUMB_ROOT = 'upload/thumb'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = UPLOAD_ROOT)
    country = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

