from django.db import models

# Create your models here.
class DiningTable(models.Model):
    table_no =  models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'Table No.{self.table_no}'

class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    table = models.OneToOneField(DiningTable,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} : {self.pk} '