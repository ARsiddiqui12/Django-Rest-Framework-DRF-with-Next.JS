from django.db import models

class Appuser(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

class Businfo(models.Model):
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    numberofseats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
