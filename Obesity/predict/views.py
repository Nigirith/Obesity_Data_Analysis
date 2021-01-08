from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

def predict(request):
    return render(request, 'predict.html')

def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        gender = float(request.POST.get('gender'))
        age = float(request.POST.get('age'))
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        family_history_with_overweight = float(request.POST.get('family_history_with_overweight'))
        frequent_consumption_of_high_caloric_food = float(request.POST.get('frequent_consumption_of_high_caloric_food'))
        frequency_of_consumption_of_vegetables = float(request.POST.get('frequency_of_consumption_of_vegetables'))
        number_of_main_meals = float(request.POST.get('number_of_main_meals'))
        consumption_of_food_between_meals = float(request.POST.get('consumption_of_food_between_meals'))
        smoke = float(request.POST.get('smoke'))
        consumption_of_water_daily = float(request.POST.get('consumption_of_water_daily'))
        calories_consumption_monitoring = float(request.POST.get('calories_consumption_monitoring'))
        physical_activity_frequency = float(request.POST.get('physical_activity_frequency'))
        time_using_technology_devices = float(request.POST.get('time_using_technology_devices'))
        consumption_of_alcohol = float(request.POST.get('consumption_of_alcohol'))
        means_of_transport = float(request.POST.get('means_of_transport'))

        MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking = 0,0,0,0,0

        if means_of_transport == 0:
            MTRANS_Automobile = 1
        elif means_of_transport == 1:
            MTRANS_Bike = 1
        elif means_of_transport == 2:
            MTRANS_Motorbike = 1
        elif means_of_transport == 3:
            MTRANS_Public_Transportation = 1
        else:
            MTRANS_Walking = 1

        MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking = float(MTRANS_Automobile), float(MTRANS_Bike), float(MTRANS_Motorbike), float(MTRANS_Public_Transportation), float(MTRANS_Walking)

        # Unpickle model
        model = pd.read_pickle("D:/Thomas/Bureau/Python for Data Analysis/Obesity_Data_Analysis/new_model.pickle")
        # Make prediction
        result = model.predict([[gender, age, height, weight,family_history_with_overweight, frequent_consumption_of_high_caloric_food, frequency_of_consumption_of_vegetables, number_of_main_meals,consumption_of_food_between_meals, smoke, consumption_of_water_daily, calories_consumption_monitoring,physical_activity_frequency, time_using_technology_devices, consumption_of_alcohol, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking]])

        classification = result[0]

        PredResults.objects.create(gender=gender, age=age, height=height, weight=weight, family_history_with_overweight=family_history_with_overweight, frequent_consumption_of_high_caloric_food=frequent_consumption_of_high_caloric_food, frequency_of_consumption_of_vegetables=frequency_of_consumption_of_vegetables, number_of_main_meals=number_of_main_meals, consumption_of_food_between_meals=consumption_of_food_between_meals, smoke=smoke, consumption_of_water_daily=consumption_of_water_daily, calories_consumption_monitoring=calories_consumption_monitoring, physical_activity_frequency=physical_activity_frequency, time_using_technology_devices=time_using_technology_devices, consumption_of_alcohol=consumption_of_alcohol, MTRANS_Automobile=MTRANS_Automobile, MTRANS_Bike=MTRANS_Bike, MTRANS_Motorbike=MTRANS_Motorbike, MTRANS_Public_Transportation=MTRANS_Public_Transportation, MTRANS_Walking=MTRANS_Walking, classification=classification)

        return JsonResponse({'result': classification, 'gender': gender, 'age': age, 'height': height, 'weight': weight, 'family_history_with_overweight': family_history_with_overweight, 'frequent_consumption_of_high_caloric_food': frequent_consumption_of_high_caloric_food, 'frequency_of_consumption_of_vegetables': frequency_of_consumption_of_vegetables, 'number_of_main_meals': number_of_main_meals, 'consumption_of_food_between_meals': consumption_of_food_between_meals, 'smoke': smoke, 'consumption_of_water_daily': consumption_of_water_daily, 'calories_consumption_monitoring': calories_consumption_monitoring, 'physical_activity_frequency': physical_activity_frequency, 'time_using_technology_devices': time_using_technology_devices, 'consumption_of_alcohol': consumption_of_alcohol, 'MTRANS_Automobile': MTRANS_Automobile, 'MTRANS_Bike': MTRANS_Bike, 'MTRANS_Motorbike': MTRANS_Motorbike, 'MTRANS_Public_Transportation': MTRANS_Public_Transportation, 'MTRANS_Walking': MTRANS_Walking}, safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)