from django.db import models

# Create your models here.


class Athlete(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    gold_medals = models.IntegerField()
    silver_medals = models.IntegerField()
    bronze_medals = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    without_bg = models.ImageField(upload_to='media/', blank=True, null=True, default="")
    date_of_birth = models.DateField()
    history = models.TextField(max_length=3000)
