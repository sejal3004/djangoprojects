from django.db import models

# Create your models here.

class workouts(models.Model):
    w_id = models.IntegerField()
    workouts = models.TextField()
    calories_pmints = models.IntegerField()
    time = models.IntegerField()
    