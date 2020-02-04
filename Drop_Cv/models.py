from django.db import models
class Resume(models.Model):
    id=models.IntegerField(primary_key=True)
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    file=models.FileField(upload_to="files/")

    def __str__(self):
        return self.full_name
    #def email(self):
     #   return self.email
    #def message(self):
     #   return self.message[:100]


