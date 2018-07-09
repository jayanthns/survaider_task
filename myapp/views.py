from django.shortcuts import render
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from myapp.models import UserData
from myapp.serializers import UserDataSerializer
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

RACE_DATA = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
RELATIONSHIP_DATA = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']
SEX_DATA = ['Female', 'Male']

# Create your views here.
class SexCountAPIView(APIView):

    def get(self, request):
        query_set = UserData.objects.all().values_list('sex', 'relationship')
        result_list = [name[0] for name in query_set]
        result_list1 = [name[1] for name in query_set]
        from collections import Counter
        response_dict = {
            'result1': Counter(result_list),
            'result2': Counter(result_list1),
        }
        return Response(response_dict, status=status.HTTP_200_OK)


class UserDataAPIView(APIView):
    
    serializer_class = UserDataSerializer

    def get(self, request):
        # query_set = UserData.objects.all()
        columns_obj = a = [{"Header": f.name.title().replace('_', ' '), "accessor": f.name} for f in UserData._meta.get_fields()]
        int_list = ['id', 'age', 'fnlwgt', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']
        for a in columns_obj:
            a['id'] = a['accessor']
        del columns_obj[0]

        if 'userdata' in cache:
            # get results from cache
            serializer = cache.get('userdata')
            print("CALLED CACHE METHOD")
        else:
            serializer = UserDataSerializer(UserData.objects.all(), many=True).data
            # store data in cache
            cache.set('userdata', serializer, timeout=CACHE_TTL)
            print("NOT CALLED CACHE METHOD")

        response_dict = {
            "data": serializer,
            "columns": columns_obj,
            "race_data": RACE_DATA,
            "sex_data": SEX_DATA,
            "relationship_data": RELATIONSHIP_DATA
        }
        return Response(response_dict, status=status.HTTP_200_OK)


"""
loadtest -n 5 -k http://localhost:8000/api/get_user_data
"""