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

        if gender == 0:
            g = "Female"
        else:
            g = "Male"

        age = float(request.POST.get('age'))
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))

        family_history_with_overweight = float(request.POST.get('family_history_with_overweight'))

        if family_history_with_overweight == 0:
            fhwo = "No"
        else:
            fhwo = "Yes"

        frequent_consumption_of_high_caloric_food = float(request.POST.get('frequent_consumption_of_high_caloric_food'))

        if frequent_consumption_of_high_caloric_food == 0:
            favc = "No"
        else:
            favc = "Yes"
            
        frequency_of_consumption_of_vegetables = float(request.POST.get('frequency_of_consumption_of_vegetables'))
        number_of_main_meals = float(request.POST.get('number_of_main_meals'))
        consumption_of_food_between_meals = float(request.POST.get('consumption_of_food_between_meals'))

        if consumption_of_food_between_meals == 0:
            caec = "No"
        elif consumption_of_food_between_meals == 1:
            caec = "Sometimes"
        elif consumption_of_food_between_meals == 2:
            caec = "Frequently"
        else:
            caec = "Always"

        smoke = float(request.POST.get('smoke'))

        if smoke == 0:
            s = "No"
        else:
            s = "Yes"

        consumption_of_water_daily = float(request.POST.get('consumption_of_water_daily'))
        calories_consumption_monitoring = float(request.POST.get('calories_consumption_monitoring'))

        if calories_consumption_monitoring == 0:
            scc = "No"
        else:
            scc = "Yes"

        physical_activity_frequency = float(request.POST.get('physical_activity_frequency'))
        time_using_technology_devices = float(request.POST.get('time_using_technology_devices'))
        consumption_of_alcohol = float(request.POST.get('consumption_of_alcohol'))

        if consumption_of_alcohol == 0:
            calc = "No"
        elif consumption_of_alcohol == 1:
            calc = "Sometimes"
        elif consumption_of_alcohol == 2:
            calc = "Frequently"
        else:
            calc = "Always"
        
        means_of_transport = float(request.POST.get('means_of_transport'))
        MTRANS_Automobile = 0
        MTRANS_Bike = 0
        MTRANS_Motorbike = 0
        MTRANS_Public_Transportation = 0
        MTRANS_Walking = 0

        if means_of_transport == 0:
            MTRANS_Automobile = 1
            mtrans = "Automobile"
        elif means_of_transport == 1:
            MTRANS_Bike = 1
            mtrans = "Bike"
        elif means_of_transport == 2:
            MTRANS_Motorbike = 1
            mtrans = "Motorbike"
        elif means_of_transport == 3:
            MTRANS_Public_Transportation = 1
            mtrans = "Public Transportation"
        else:
            MTRANS_Walking = 1
            mtrans = "Walking"

        MTRANS_Automobile = float(MTRANS_Automobile)
        MTRANS_Bike = float(MTRANS_Bike)
        MTRANS_Motorbike = float(MTRANS_Motorbike)
        MTRANS_Public_Transportation = float(MTRANS_Public_Transportation)
        MTRANS_Walking = float(MTRANS_Walking)


        # Unpickle model
        model = pd.read_pickle("D:/Thomas/Bureau/Python for Data Analysis/Obesity_Data_Analysis/new_model.pickle")
        # Make prediction
        result = model.predict([[gender, age, height, weight,family_history_with_overweight, frequent_consumption_of_high_caloric_food, frequency_of_consumption_of_vegetables, number_of_main_meals,consumption_of_food_between_meals, smoke, consumption_of_water_daily, calories_consumption_monitoring,physical_activity_frequency, time_using_technology_devices, consumption_of_alcohol, MTRANS_Automobile, MTRANS_Bike, MTRANS_Motorbike, MTRANS_Public_Transportation, MTRANS_Walking]])

        classification = result[0]

        if classification == 0:
            c = "Normal Weight"
        elif classification == 1:
            c = "Overweight Level I"
        elif classification == 2:
            c = "Overweight Level II"
        elif classification == 3:
            c = "Obesity Level I"
        elif classification == 4:
            c = "Obesity Level II"
        elif classification == 5:
            c = "Obesity Level III"
        else:
            c = "Insufficient Weight"

        PredResults.objects.create(gender=g, age=age, height=height, weight=weight, family_history_with_overweight=fhwo, frequent_consumption_of_high_caloric_food=favc, frequency_of_consumption_of_vegetables=frequency_of_consumption_of_vegetables, number_of_main_meals=number_of_main_meals, consumption_of_food_between_meals=caec, smoke=s, consumption_of_water_daily=consumption_of_water_daily, calories_consumption_monitoring=scc, physical_activity_frequency=physical_activity_frequency, time_using_technology_devices=time_using_technology_devices, consumption_of_alcohol=calc, means_of_transport=mtrans, classification=c)

        return JsonResponse({'result': c, 'gender': g, 'age': age, 'height': height, 'weight': weight, 'family_history_with_overweight': fhwo, 'frequent_consumption_of_high_caloric_food': favc, 'frequency_of_consumption_of_vegetables': frequency_of_consumption_of_vegetables, 'number_of_main_meals': number_of_main_meals, 'consumption_of_food_between_meals': caec, 'smoke': s, 'consumption_of_water_daily': consumption_of_water_daily, 'calories_consumption_monitoring': scc, 'physical_activity_frequency': physical_activity_frequency, 'time_using_technology_devices': time_using_technology_devices, 'consumption_of_alcohol': calc, 'means_of_transport': mtrans}, safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)