from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000, blank=False,null=True)
    drink = models.BooleanField(blank=False,null=True)
    kids = models.BooleanField(blank=False,null=True)
    smoke = models.BooleanField(blank=False,null=True)

def get_image_filename(instance, filename):
    title = instance.user.pk
    return "%d/%s" % (title, filename)

class Image(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200,default='default_title')
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')
