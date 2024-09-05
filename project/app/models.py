from django.db import models
from .validators import *
# Create your models here.

class ItemInfo(models.Model):
    iten_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to="image", validators=[validate_image])
    item_resume = models.FileField(upload_to="file", validators=[validate_file])
