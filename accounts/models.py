from django.db import models

# Create your models here.
class AccountDetail(models.Model):
    Country = models.CharField(max_length=45,default='India')
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    pincode = models.CharField(max_length=6)
    Phoneno = models.CharField(max_length=10)
    Telephone = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.Address