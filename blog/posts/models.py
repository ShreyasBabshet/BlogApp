from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
  title=models.CharField(max_length=100)
  body=models.CharField(max_length=100000)
  images=models.ImageField(upload_to='images',default="")
  created_at=models.DateTimeField(default=datetime.now,blank=True)

