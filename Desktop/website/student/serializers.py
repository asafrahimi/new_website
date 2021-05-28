from rest_framework import serializers
from .models import Id
from rest_framework.renderers import JSONRenderer

class IdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Id
        fields = ['name', 'last_name', 'age']
        #fields = "__all__"
