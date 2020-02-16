from django.contrib.auth.models import User
from django.db import models
class Post(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    detail=models.TextField()
    pub_date=models.DateTimeField
    file=models.ImageField(upload_to="files/")
    recuiter=models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
