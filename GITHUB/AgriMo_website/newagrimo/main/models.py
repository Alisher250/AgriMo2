from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Odor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Humidity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Raindrop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Light(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Moisture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Temperature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Pressure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Sunradiation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    min = models.IntegerField(null=True, blank=True)
    minper = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    dayper = models.IntegerField(null=True, blank=True)
    week = models.IntegerField(null=True, blank=True)
    weekper = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    monthper = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    yearper = models.IntegerField(null=True, blank=True)

class Shapes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shape = models.TextField()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.BigIntegerField(null=True, blank=True)
    profession = models.CharField(blank=True, max_length=100)
    geolocation1 = models.CharField(blank=True, max_length=250)
    geolocation2 = models.CharField(blank=True, max_length=250)
    city = models.CharField(blank=True, max_length=250)
    region = models.CharField(blank=True, max_length=250)
    farm = models.CharField(blank=True, max_length=250)
    odor = models.ManyToManyField(Odor, blank=True)
    humidity = models.ManyToManyField(Humidity, blank=True)
    temperature = models.ManyToManyField(Temperature, blank=True)
    raindrop = models.ManyToManyField(Raindrop, blank=True)
    light = models.ManyToManyField(Light, blank=True)
    moisture = models.ManyToManyField(Moisture, blank=True)
    pressure = models.ManyToManyField(Pressure, blank=True)
    sunradiation = models.ManyToManyField(Sunradiation, blank=True)
    shapes = models.ManyToManyField(Shapes, blank=True)

class Shop(models.Model):
    photo = models.ImageField(upload_to='items')
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=25990)

class Statistics(models.Model):
    name = models.IntegerField(default=0)
    value = models.IntegerField(default=0)

class Info(models.Model):
    number = models.ForeignKey(Statistics, on_delete=models.CASCADE)
    information = models.TextField()

class Table(models.Model):
    farmname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    typeofcrop = models.CharField(max_length=200)
    startdate = models.CharField(max_length=200)
    enddate = models.CharField(max_length=200)
    yieldtons = models.CharField(max_length=200)
    totalarea = models.CharField(max_length=200)
    totalproduction = models.CharField(max_length=200)
    totalcrops = models.CharField(max_length=200)
    soilcondition = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    diseasepercentage = models.CharField(max_length=200)
    yieldpercentage = models.CharField(max_length=200)
    waterlevel = models.CharField(max_length=200)
    income = models.CharField(max_length=200)
    expenses = models.CharField(max_length=200)
    farmprofit = models.CharField(max_length=200)

class Review(models.Model):
    writer = models.CharField(max_length=100)
    specialist = models.ForeignKey('Specialists', on_delete=models.CASCADE)

class Specialists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='items', blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, default="Astana", blank=True)
    age = models.IntegerField(default=41, blank=True)
    experience = models.IntegerField(default=10, blank=True)
    rating = models.IntegerField(default=3, blank=True, null=True)
    comments = models.ManyToManyField('Review', blank=True)