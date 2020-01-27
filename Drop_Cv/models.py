from django.db import models

class Resume(models.Model):
    FullName=models.CharField(max_length=255)
    Email=models.CharField(max_length=320)
    Message=models.TextField()
    Image=models.ImageField(upload_to='images/')

