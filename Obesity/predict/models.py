
from django.db import models


class PredResults(models.Model):

    gender = models.FloatField()
    age = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    family_history_with_overweight = models.FloatField()
    frequent_consumption_of_high_caloric_food = models.FloatField()
    frequency_of_consumption_of_vegetables = models.FloatField()
    number_of_main_meals = models.FloatField()
    consumption_of_food_between_meals = models.FloatField()
    smoke = models.FloatField()
    consumption_of_water_daily = models.FloatField()
    calories_consumption_monitoring = models.FloatField()
    physical_activity_frequency = models.FloatField()
    time_using_technology_devices = models.FloatField()
    consumption_of_alcohol = models.FloatField()
    MTRANS_Automobile = models.FloatField()
    MTRANS_Bike = models.FloatField()
    MTRANS_Motorbike = models.FloatField()
    MTRANS_Public_Transportation = models.FloatField()
    MTRANS_Walking = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification