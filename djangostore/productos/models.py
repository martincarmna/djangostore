from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)


    def __str__(self):
        return  self.category


class Productos(models.Model):
    name = models.CharField(max_length=50)
    descripción = models.TextField
    price = models.FloatField()
    avaliable = models.BooleanField()
    Category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    stock = models.IntegerField()

def __str__(self):
    return f"{ self.name } - $ { self.price }"

