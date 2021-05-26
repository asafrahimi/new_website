from django.db import models

# Create your models here.

class Id(models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()


class Professions(models.Model):
    first_profession = models.CharField(max_length = 20)
    second_profession = models.CharField(max_length = 20)
    thrid_profession = models.CharField(max_length = 20)


class Adress(models.Model):
    city = models.CharField(max_length = 20)
    street = models.CharField(max_length = 20)
    num_home = models.IntegerField()
