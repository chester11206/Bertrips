from django.contrib import admin
from .models import Media, Head

# Register your models here.
class MediaAdmin(admin.StackedInline):
    model = Media
    admin.site.register(Media)

class HeadAdmin(admin.StackedInline):
    model = Head
    admin.site.register(Head)