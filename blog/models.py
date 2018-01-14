from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
# Post model.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

def publish(self):
    self.published_date = timeone.now()
    self.save()

def _str_(self):
    return self.title

# SliderImageUploadModel.
class ImageUploadForm(models.Model):
    image = forms.ImageField()
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
