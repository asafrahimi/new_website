from rest_framework import serializers
from .models import Id

class IdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Id
        fields = ('name', 'last_name')
        #fields = '__all__'
