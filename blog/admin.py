from django.contrib import admin
from .models import Post, ImageUploadForm


# Register your models here.
admin.site.register(Post)
admin.site.register(ImageUploadForm)
