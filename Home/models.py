from django.db import models


class Scrape(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    sponsored = models.CharField(max_length=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
