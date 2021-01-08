
from django.db import models


class PredResults(models.Model):

    gender = models.CharField(max_length=30)
    age = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    family_history_with_overweight = models.CharField(max_length=30)
    frequent_consumption_of_high_caloric_food = models.CharField(max_length=30)
    frequency_of_consumption_of_vegetables = models.FloatField()
    number_of_main_meals = models.FloatField()
    consumption_of_food_between_meals = models.CharField(max_length=30)
    smoke = models.CharField(max_length=30)
    consumption_of_water_daily = models.FloatField()
    calories_consumption_monitoring = models.CharField(max_length=30)
    physical_activity_frequency = models.FloatField()
    time_using_technology_devices = models.FloatField()
    consumption_of_alcohol = models.CharField(max_length=30)
    means_of_transport = models.CharField(max_length=30, default="TEST")
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification