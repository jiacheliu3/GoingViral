from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    population = models.IntegerField()
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)


class Airport(models.Model):
    city_name = models.CharField(max_length=200)
    country = models.OneToOneField(Country, related_name='country')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.city_name


class Airline(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    # Date time fields
    departure = models.DateField()
    arrival = models.DateField()

    # Relative models
    from_airport = models.OneToOneField(Airport, related_name='from_airport',default=None)
    to_airport = models.OneToOneField(Airport, related_name='to_airport',default=None)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    infection_rate = models.FloatField()
    cure_rate = models.FloatField()
    susceptible_rate = models.FloatField()
    death_rate = models.FloatField()

    def __str__(self):
        return self.name
