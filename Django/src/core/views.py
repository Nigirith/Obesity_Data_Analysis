from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

import pandas as pd
import json

my_data = pd.read_csv("D://Thomas//Bureau//Python for Data Analysis//Obesity_Data_Analysis//ObesityDataSet_raw_and_data_sinthetic.csv")

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = json.loads(my_data.to_json())
        return Response(data)