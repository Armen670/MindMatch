from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=False)
    second_name = models.CharField(max_length=50,blank=False)
    desc = models.CharField(max_length=1000,blank=False)
    drink = models.BooleanField(blank=False)
    kids = models.BooleanField(blank=False)
    smoke = models.BooleanField(blank=False)

def get_image_filename(instance, filename):
    title = instance.user.pk
    return "post_images/%d/%s" % (title, filename)


class Images(models.Model):
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,verbose_name='Image')
