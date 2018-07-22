import os
from django.db import models
#from trips.utils import make_thumb
from bertrips.settings import MEDIA_ROOT
from trips.models import Post
from django.utils.translation import ugettext as _

# Create your models here.

UPLOAD_ROOT = 'photo'
THUMB_ROOT = 'photo/thumb'

class Media(models.Model):
    title = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = UPLOAD_ROOT)
    #thumb = models.ImageField(upload_to = THUMB_ROOT, blank = True)
    country = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add = True)
    #post = models.ForeignKey(Post)

    class Meta:
        verbose_name_plural = _('Media')
    '''
    def save(self):
        base, ext = os.path.splitext(os.path.basename(self.image.path))
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT + '/' + THUMB_ROOT, self.image.name))
        relate_thumb_path = os.path.join(THUMB_ROOT, base + '.thumb' + ext)
        thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
        thumb_pixbuf.save(thumb_path)
        self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
        super(Media, self).save()
	'''
    def __unicode__(self):
        return _('%s, uploaded at %s') % (self.title, self.date.strftime('%T %h %d, %Y'))

    def __str__(self):
        return self.title

# class Head(models.Model):
# 	name = models.CharField(max_length = 120)
# 	image = models.ImageField(upload_to = UPLOAD_ROOT)
# 	profile = models.TextField(blank=True)
#     facebook = models.URLField(blank = True)
#     instagram = models.URLField(blank = True)
#     date = models.DateTimeField(auto_now_add = True)

# 	def __unicode__(self):
# 		return _('%s, uploaded at %s') % (self.title, self.date.strftime('%T %h %d, %Y'))

# 	def __str__(self):
# 		return self.name

class Head(models.Model):
    name = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = UPLOAD_ROOT)
    profile = models.TextField(blank=True)
    content = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return _('%s, uploaded at %s') % (self.title, self.date.strftime('%T %h %d, %Y'))

    def __str__(self):
        return self.name

