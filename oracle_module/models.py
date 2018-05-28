from django.db import models


# Create your models here.
class Customer(models.Model):
    ID = models.IntegerField(primary_key=True)
    NAME = models.CharField(max_length=20)

    class Meta:
        db_table = 'CUSTOMER'
