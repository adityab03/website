from django.db import models

class Clothes(models.Model):
    brand = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    size = models.CharField(max_length=250)

    def __str__(self):
        return self.brand + ' - ' + self.type

class Designer(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    person = models.CharField(max_length=250)