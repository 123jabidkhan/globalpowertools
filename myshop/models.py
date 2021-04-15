from django.db import models


# Create your models here.
class Query(models.Model):
    name =models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=100,null=True)



    