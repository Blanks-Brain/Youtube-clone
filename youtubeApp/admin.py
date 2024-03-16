from django.contrib import admin
from .models import Category,Channel,VideoDetail,VideoFiles
# Register your models here.

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(VideoFiles)
admin.site.register(VideoDetail)
