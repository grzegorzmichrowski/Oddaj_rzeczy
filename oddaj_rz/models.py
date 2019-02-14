from django.db import models
from django.contrib.postgres.fields import ArrayField
from multiselectfield import MultiSelectField

# Create your models here.


CATEGORIES = (
    (1, "ubrania"),
    (2, "jedzenie"),
    (3, "meble"),
    (4, "zabawki"),
    (5, "sprzęt AGD"),
    (6, "książki")
)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    target_mission = models.CharField(max_length=255)
    things_categories = MultiSelectField(choices=CATEGORIES)


class Gift(models.Model):
    caregory = models.CharField(max_length=255)
    number_of_bags = models.IntegerField()
    location = models.CharField(max_length=255)
    target = ArrayField(models.CharField(max_length=255), size=5)
    institution = models.CharField(max_length=255)
    address = ArrayField(models.CharField(max_length=255), size=4)
    receipt_date = models.DateField()
    receipt_time = models.TimeField()
    note = models.CharField(max_length=255)