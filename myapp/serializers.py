from rest_framework import serializers

from myapp.models import UserData

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        # fields = ("__all__")
        exclude = ('id', )
