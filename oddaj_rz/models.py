from django.db import models
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    genitive = models.CharField(max_length=255)


class Location(models.Model):
    name = models.CharField(max_length=255)


class Target(models.Model):
    name = models.CharField(max_length=255)
    genitive = models.CharField(max_length=255)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    mission = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    locations = models.ManyToManyField(Location)


class Gift(models.Model):
    caregories = models.ManyToManyField(Category)
    bags = models.IntegerField()
    locations = models.ManyToManyField(Location)
    target = ArrayField(models.CharField(max_length=255), size=5)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = ArrayField(models.CharField(max_length=255), size=4)
    receipt_date = models.DateField()
    receipt_time = models.TimeField()
    note = models.CharField(max_length=255)
