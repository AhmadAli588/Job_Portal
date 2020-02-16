from django.db import models
class Resume(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    file=models.FileField(upload_to="files/")

    def __str__(self):
        return self.full_name



