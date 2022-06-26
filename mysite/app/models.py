from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name