from django.db import models

# Create your models here.
class BasicDetail(models.Model):
    username = models.CharField(max_length=20,unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    pincode = models.CharField(max_length=250)

    def __str__(self):
        return self.username

